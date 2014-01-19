#!/usr/bin/python

# Remote control ESC using DSMX - POC for DIY DRONES
# /blogs/remote-control-a-esc-pwm-using-a-dsmx-receiver-with-rpi-gpio

from serial import Serial 
from smbus import SMBus 
from math import floor
from time import sleep
from struct import unpack 

Names={'THR':0, 'AIL':1, 'ELE':2, 'RUD':3, 'GEA':4, 'AUX1':5, 'AUX2':6}

Channel = 'THR'
ChannelOffset = 1900

PWMFreq = 400 
PWMChannel = 0
I2CAddress = 0x40

# SMBus: 0 or 1 - depends on RPi revision
I2CBus = SMBus(1)

def PWM_freq(freq):
   MODE1 = 0x00
   PRESCALE = 0xFE

   prescaleval = 25000000.0
   prescaleval /= 4096.0 
   prescaleval /= float(freq)
   prescale = floor(prescaleval - 0.5)

   oldmode = I2C_read(MODE1);
   I2C_write(MODE1, (oldmode & 0x7F) | 0x10)
   I2C_write(PRESCALE, int(prescale))
   I2C_write(MODE1, oldmode)
   sleep(0.005)
   I2C_write(MODE1, oldmode | 0x80)


def PWM_set(channel, off):
   LED0_ON_L = 0x06
   LED0_ON_H = 0x07
   LED0_OFF_L = 0x08
   LED0_OFF_H = 0x09

   on = 0
   I2C_write(LED0_ON_L + 4 * channel, on & 0xFF)
   I2C_write(LED0_ON_H + 4 * channel, on >> 8)
   I2C_write(LED0_OFF_L + 4 * channel, off & 0xFF)
   I2C_write(LED0_OFF_H + 4 * channel, off >> 8)


def I2C_read(reg):
   try:
      return I2CBus.read_byte_data(I2CAddress, reg)
   except IOError, err:
      print err

def I2C_write(reg, value):
   try:
      I2CBus.write_byte_data(I2CAddress, reg, value)
   except IOError, err:
      print err


