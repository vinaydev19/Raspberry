#!/usr/bin/python

import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_lines = 2

# Raspberry Pi pin configuration:
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initialize the LCD Class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_lines, lcd_backlight)

# Print a two-line message
lcd.message = "Edkits\nElectronics"
time.sleep(5)

# Clear the display
lcd.clear()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           