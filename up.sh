#reset: 8
#gpio0: 11
#Script to upload initial firmware to the onboard ESP8266
#After initial firmware is loaded, updates can be done esphome utility




gpio -g mode 8 out
gpio -g mode 11 out
echo taking pin 0 to low
gpio -g write 11 0
echo taking reset to high
gpio -g write 8 1
sleep 1
echo taking reset to low
gpio -g write 8 0
sleep 1
echo taking reset to high - should enter program mode
gpio -g write 8 1
sleep 1
esptool --baud 115200 --chip esp8266 --port /dev/serial0 write_flash 0x0 ./firmware.bin
echo Reseting
gpio -g write 8 0
gpio -g write 11 1 
sleep 1
gpio -g write 8 1
echo done
