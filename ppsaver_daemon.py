#!/usr/bin/env python3

import serial
from subprocess import call
import RPi.GPIO as GPIO

SERIAL_PORT = '/dev/serial0'
SERIAL_RATE = 9600
STATUS_LED = 25

ser = None

def update_serial():
    global ser
    if (ser != None):
        return
    ser = serial.Serial(port = SERIAL_PORT, baudrate = SERIAL_RATE, timeout = 1)

def main():
    print("PPSaver Daemon")
    print("Listening to port " + SERIAL_PORT)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STATUS_LED,GPIO.OUT)
    b = True
    while True:
        try:
            GPIO.output(STATUS_LED,b)
            b = not b
            main_loop()
        except Exception as e:
            print(e)


def main_loop():
    update_serial()
    l = ser.readline().decode().strip()
    if not l:
        return
    if (l=="SHUTDOWN"):
        print("Shutting down")
        call("sudo shutdown -h now", shell=True)
        GPIO.cleanup()
        quit()
    print("Unknown command: " + l)

if __name__ == "__main__":
    main()
