#!/usr/bin/python
# import
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18


# Define some device constants
LCD_WIDTH = 2    # Maximum characters per line
# LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
# 1s
# 1ms = 0.001s
# 1us = 0.000001s = 0.001ms
# E_PULSE = 0.005  # 5 ms
E_PULSE = 0.0005  # 500 us
E_DELAY = 0.0005


def main():
    # Main program block

    print("Setup")
    # GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT)  # RS
    GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
    GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
    GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
    GPIO.setup(LCD_D7, GPIO.OUT)  # DB7
    print("Setup ... Done")

    # lcd_byte(0b0011_0011, LCD_CMD)  # 0x33 110011 Initialise
    # Initialise display
    lcd_init()
    print("lcd_init ... Done")

    # while True:
    print("display ... Rasbperry Pi")
    lcd_string("ab", LCD_LINE_1)
    # lcd_string("Pi1", LCD_LINE_2)
    # time.sleep(3)  # 3 second delay
    # while True:

    #     # Send some test
    #     print("display ... Rasbperry Pi")
    #     lcd_string("Rasbperry Pi", LCD_LINE_1)
    #     lcd_string("16x2 LCD Test", LCD_LINE_2)

    #     time.sleep(3)  # 3 second delay

    #     # Send some text
    #     print("display ... 1234567890123456")
    #     lcd_string("1234567890123456", LCD_LINE_1)
    #     lcd_string("abcdefghijklmnop", LCD_LINE_2)

    #     time.sleep(3)  # 3 second delay


def lcd_init():
    # Initialise display
    lcd_byte(0b0011_0011, LCD_CMD)  # 0x33 110011 Initialise
    lcd_byte(0b0011_0010, LCD_CMD)  # 0x32 110010 Initialise
    lcd_byte(0b0000_0110, LCD_CMD)  # 0x06 000110 Cursor move direction
    # 0x0C 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0b0000_1100, LCD_CMD)
    # 0x28 101000 Data length, number of lines, font size
    lcd_byte(0b0010_1000, LCD_CMD)
    lcd_byte(0b0000_0001, LCD_CMD)  # 0x01 000001 Clear display
    time.sleep(E_DELAY)


def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    GPIO.output(LCD_RS, mode)  # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    # if bits & 0x10 == 0x10:
    if bits & 0b0001_0000 == 0b0001_0000:
        GPIO.output(LCD_D4, True)
    # if bits & 0x20 == 0x20:
    if bits & 0b0010_0000 == 0b0010_0000:
        GPIO.output(LCD_D5, True)
    # if bits & 0x40 == 0x40:
    if bits & 0b0100_0000 == 0b0100_0000:
        GPIO.output(LCD_D6, True)
    # if bits & 0x80 == 0x80:
    if bits & 0b1000_0000 == 0b1000_0000:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()


def lcd_toggle_enable():
    # Toggle enable
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)


def lcd_string(message, line):
    # Send string to display

    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


if __name__ == '__main__':
    print("Starting")
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        # lcd_byte(0x01, LCD_CMD)
        # lcd_string("Goodbye!", LCD_LINE_1)
        GPIO.cleanup()
