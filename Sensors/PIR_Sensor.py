import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)     #Input PIR-sensorille
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)     #Output LEDille
while True:
    i = GPIO.input(11)
    if i == 0:
        print("Ei vaaraa"), i
        GPIO.output(3, 0)   #LEDi pois
        time.sleep(1)
    elif i == 1:            #Jos PIR-sensorissa tapahtuu
        print("Hälyytys"), i
        GPIO.output(3, 1)   #LEDi päälle
        time.sleep(1)