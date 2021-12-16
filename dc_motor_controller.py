import RPi.GPIO as GPIO
from time import sleep

class DCMotorController():

    def __init__(self):
        # Pins for Motor Driver Inputs 
        self.Motor1A = 21
        self.Motor1B = 20
        self.Motor1E = 16

        self.Motor2A = 7
        self.Motor2B = 25
        self.Motor2E = 8

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)              # GPIO Numbering
        GPIO.setup(self.Motor1A,GPIO.OUT)        # All pins as Outputs
        GPIO.setup(self.Motor1B,GPIO.OUT)
        GPIO.setup(self.Motor1E,GPIO.OUT)

        GPIO.setup(self.Motor2A,GPIO.OUT)      
        GPIO.setup(self.Motor2B,GPIO.OUT)
        GPIO.setup(self.Motor2E,GPIO.OUT)
    
    def forward(self,sec):
        # Going forwards
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        print("Going forwards")
    
        sleep(sec)

    def backward(self,sec):
        # Going backwards
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        print("Going backwards")
    
        sleep(sec)

    def stop(self):
        GPIO.output(self.Motor1E,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.LOW)
        print("Stop")

    def destroy(self):  
        GPIO.cleanup()

if __name__ == '__main__':    
    controller = DCMotorController()
    try:
        controller.forward(5)
        controller.stop()

    except KeyboardInterrupt:
        controller.destroy()

    