#!/usr/bin/env bash
# This will flash and resintall micropython on the ESP8266
esptool.py --port /dev/tty.usbserial-0001 erase_flash && esptool.py --port /dev/tty.usbserial-0001 --baud 460800 write_flash --flash_size=detect -fm dout 0 esp8266-20230426-v1.20.0.bin
