import RPLCD as RPLCD
#from RPLCD import CharLCD, cleared, cursor
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
lcd.clear()


smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string("\x00")


# Time and date
#while True:
#    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
#    
#    lcd.cursor_pos = (1, 0)
#    lcd.write_string("Date: %s" %time.strftime("%d/%m/%Y"))
