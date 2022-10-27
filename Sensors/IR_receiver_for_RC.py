import RPi.GPIO as GPIO
from datetime import datetime

#Static program vars
pin = 15 #Input pin of sensor (GPIO.BOARD)
Buttons = ["0x1807fd06fL", "0x300ffb04fL", "0x300ffa857L"]
ButtonNames = ["r0" ,     "r1" ,         "r2" ,         "r3" ,        "r4" ,         "g0" ,        "g1" ,   "g2" ,         "3" ,          "g4" ,         "b0" ,         "b1" ,         "b2" ,         "b3" ,         "b4" ,         "w0" ,         "w1" ,         "w2" ,         "w3" ,   "w4" ,         "up" ,        "down" ,     "off" ,     "on"]

#Sets up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

#Gets binary value
def getBinary():
    #Internal vars
    num1s = 0 #Number of consecutive 1s read
    binary = 1 #The bianry value
    command = [] #The list to store pulse times in
    previousValue = 0 #The last value
    value = GPIO.input(pin) #The current value
    
    #Waits for the sensor to pull pin low
    while value:
        value = GPIO.input(pin)
        
    #Records start time
    startTime = datetime.now()
    
    while True:
        #If change detected in value
        if previousValue != value:
            now = datetime.now()
            pulseTime = now - startTime #Calculate the time of pulse
            startTime = now #Reset start time
            command.append((previousValue, pulseTime.microseconds)) #Store recorded data
            
        #Updates consecutive 1s variable
        if value:
            num1s += 1
        else:
            num1s = 0
        
        #Breaks program when the amount of 1s surpasses 10000
        if num1s > 10000:
            break
            
        #Re-reads pin
        previousValue = value
        value = GPIO.input(pin)
        
    #Converts times to binary
    for (typ, tme) in command:
        if typ == 1: #If looking at rest period
            if tme > 1000: #If pulse greater than 1000us
                binary = binary *10 +1 #Must be 1
            else:
                binary *= 10 #Must be 0
            
    if len(str(binary)) > 34: #Sometimes, there is some stray characters
        binary = int(str(binary)[:34])
        
    return binary
    
#Conver value to hex
def convertHex(binaryValue):
    tmpB2 = int(str(binaryValue),2) #Tempary propper base 2
    return hex(tmpB2)
    
while True:
    inData = convertHex(getBinary()) #Runs subs to get incomming hex value
    for button in range(len(Buttons)):#Runs through every value in list
        if hex(Buttons[button]) == inData: #Checks this against incomming
            print(ButtonsNames[button]) #Prints corresponding english name for button
            