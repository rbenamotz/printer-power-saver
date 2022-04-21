#!/usr/bin/env python3

import serial, time
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
    update_serial()
    b = True
    while True:
        try:
            GPIO.output(STATUS_LED,b)
            b = not b
            main_loop()
        except KeyboardInterrupt as k:
            GPIO.cleanup()
            print ("Good bye")
            break
        except Exception as e:
            GPIO.cleanup()
            print(e)
            break


def main_loop():
    l = ser.readline().decode().strip()
    if not l:
        return
    print(l)
    l = "SHUTDOWN"
    if (l=="SHUTDOWN"):
        print("Shutting down")
        b = True
        for i in range(20):
            GPIO.output(STATUS_LED,b)
            b = not b
            time.sleep(0.05)
        GPIO.cleanup()
        call("sudo shutdown -h now", shell=True)
        quit()
    #print("Unknown command: " + l)

if __name__ == "__main__":
    main()
