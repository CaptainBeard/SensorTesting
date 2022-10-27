import RPLCD as RPLCD
import Adafruit_DHT
from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

temp = (
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
)

lcd.create_char(0, temp)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("{0:0.1f}\x00C".format(temperature))
        lcd.cursor_pos = (0, 8)
        lcd.write_string("{0:0.1f}%".format(humidity))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("%s" %time.strftime("%H:%M:%S"))
        lcd.cursor_pos = (1, 9)
        lcd.write_string("%s" %time.strftime("%d.%m"))