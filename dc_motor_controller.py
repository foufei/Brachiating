import RPi.GPIO as GPIO
from time import sleep

class DCMotorController():
    def __init__(self,motor_a,motor_b,motor_e):
        # Pins for Motor Driver Inputs 
        self.motor_a = motor_a
        self.motor_b = motor_b
        self.motor_e = motor_e

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)              # GPIO Numbering
        GPIO.setup(self.motor_a,GPIO.OUT)        # All pins as Outputs
        GPIO.setup(self.motor_b,GPIO.OUT)
        GPIO.setup(self.motor_e,GPIO.OUT)
 
    def forward(self,sec):
        # Going forwards
        GPIO.output(self.motor_a,GPIO.HIGH)
        GPIO.output(self.motor_b,GPIO.LOW)
        GPIO.output(self.motor_e,GPIO.HIGH)
        print("Going forwards")
    
        sleep(sec)

    def backward(self,sec):
        # Going backwards
        GPIO.output(self.motor_a,GPIO.LOW)
        GPIO.output(self.motor_b,GPIO.HIGH)
        GPIO.output(self.motor_e,GPIO.HIGH)
        print("Going backwards")
    
        sleep(sec)

    def stop(self):
        GPIO.output(self.motor_e,GPIO.LOW)
        GPIO.output(self.motor_b,GPIO.LOW)
        print("Stop")

    def destroy(self):  
        GPIO.cleanup()


if __name__ == '__main__':    
    controller1 = DCMotorController(21,20,16)
    controller2 = DCMotorController(7,25,8)
    try:
        controller1.forward(5)
        controller1.stop()

    except KeyboardInterrupt:
        controller1.destroy()

    