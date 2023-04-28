from machine import Pin
from time import sleep, sleep_ms, sleep_us

# Define GPIO to LCD mapping
LCD_RS = 16
LCD_E = 17
LCD_D4 = 18
LCD_D5 = 19
LCD_D6 = 20
LCD_D7 = 21

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 500
E_DELAY = 500

# Initialize GPIO pins
rs = Pin(LCD_RS, Pin.OUT)
e = Pin(LCD_E, Pin.OUT)
d4 = Pin(LCD_D4, Pin.OUT)
d5 = Pin(LCD_D5, Pin.OUT)
d6 = Pin(LCD_D6, Pin.OUT)
d7 = Pin(LCD_D7, Pin.OUT)

def lcd_init():
    # Initialise display
    lcd_byte(0x33, LCD_CMD)  # 0x33 110011 Initialise
    lcd_byte(0x32, LCD_CMD)  # 0x32 110010 Initialise
    lcd_byte(0x06, LCD_CMD)  # 0x06 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 0x0C 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 0x28 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 0x01 000001 Clear display
    sleep_us(E_DELAY)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    rs.value(mode)  # RS

    # High bits
    d4.value(bool(bits & 0x10))
    d5.value(bool(bits & 0x20))
    d6.value(bool(bits & 0x40))
    d7.value(bool(bits & 0x80))

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    d4.value(bool(bits & 0x01))
    d5.value(bool(bits & 0x02))
    d6.value(bool(bits & 0x04))
    d7.value(bool(bits & 0x08))

    # Toggle 'Enable' pin
    lcd_toggle_enable()

def lcd_toggle_enable():
    # Toggle enable
    sleep_us(E_DELAY)
    e.value(1)
    sleep_us(E_PULSE)
    e.value(0)
    sleep_us(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message + " " * (LCD_WIDTH - len(message))
    print("lcd_string(" + message + ")")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def main():
    # Main program block

    print("Setup")
    print("Setup ... Done")

    # Initialise display
    lcd_init()
    print("lcd_init ... Done")

    while True:
        # Send some test
        print("display ... Raspberry Pi")
        lcd_string("Raspberry Pi", LCD_LINE_1)
        lcd_string("16x2 LCD Test", LCD_LINE_2)

        sleep(2)

        # Send some text
        print("display ... 1234567890123456")
        lcd_string("1234567890123456", LCD_LINE_1)
        lcd_string("abcdefghijklmnop", LCD_LINE_2)

        sleep(2)

if __name__ == '__main__':
    print("Starting")
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!", LCD_LINE_1)
        print("Goodbye!")
        
