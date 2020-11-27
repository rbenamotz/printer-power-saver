#reset: 8
#gpio0: 11
#Script to upload initial firmware to the onboard ESP8266
#After initial firmware is loaded, updates can be done esphome utility




gpio -g mode 8 out
gpio -g mode 11 out
gpio -g write 11 low
gpio -g write 8 high
sleep 1
gpio -g write 8 low
sleep 1
gpio -g write 8 high
esptool --baud 115200 --chip esp8266 --port /dev/serial0 write_flash 0x0 ./firmware.bin
gpio -g write 8 low
gpio -g write 11 high 
sleep 1
gpio -g write 8 high
