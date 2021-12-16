import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17
SPEED_OF_SOUND = 34300

print("Initializing Ultrasonic Sensor")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

print("Taking Measurement")

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)


while GPIO.input(ECHO) == 0 :
    pulse_start = time.time()

while GPIO.input(ECHO) == 1 :
   pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = round(pulse_duration * (SPEED_OF_SOUND / 2), 2)

print("DISTANCE: ",distance,"cm")

print("Continuous Detection")

d = []
for i in range(0,9):
    d.append(distance)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0 :
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1 :
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = round(pulse_duration * (SPEED_OF_SOUND / 2), 2)

    GPIO.cleanup()
    return distance


def view_real_time_distance():
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = round(pulse_duration * (SPEED_OF_SOUND / 2), 2)

        dist = 0

        for i in range(0,(len(d)-1)):
            d[i] = d[i+1]
            d[len(d)-1] = distance
            print(d)

            for i in range(0,len(d)):
                dist = dist + d[i] 

        avg_dist = dist / len(d)

        print("DISTANCE: ",avg_dist,"cm")
        time.sleep(0.05)

        GPIO.cleanup()