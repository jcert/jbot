from GPIO import GPIO as gp

from enum import Enum

import time


class Direction(Enum):
    FWD  = 1    #forward
    BWD  = 2    #
    RCW  = 3    #clockwise 
    RCCW = 4    #counterclockwise
    


class PinMode(Enum):
    RASPI  = 1    #raspi crazy pin numbering  
    HEADER = 2    #as it is on the board


myPinMode = PinMode.RASPI

if myPinMode == PinMode.RASPI:
    CAM_SERVO1 = 2
    CAM_SERVO2 = 25

    ECHO_SERVO1 = 10
    SERVO_PINS = [CAM_SERVO1,CAM_SERVO2,ECHO_SERVO1]

    MOTOR_R_FWD = 20 
    MOTOR_R_BWD = 21
    MOTOR_R_PWM = 16

    MOTOR_L_FWD = 19
    MOTOR_L_BWD = 26
    MOTOR_L_PWM = 13

    TRACKING_L1 = 3
    TRACKING_L2 = 5
    TRACKING_R1 = 4
    TRACKING_R2 = 18

    IR_L = 12
    IR_R = 17

    BUZZER = 8

    SEEKLIGHT_L = 7
    SEEKLIGHT_R = 6

    RGB_R = 22  
    RGB_G = 27
    RGB_B = 24
elif myPinMode == PinMode.HEADER:
    CAM_SERVO1 = 2
    CAM_SERVO2 = 2

    ECHO_SERVO1 = 2

    MOTOR_R_FWD = 2 
    MOTOR_R_BWD = 2
    MOTOR_R_PWM = 2

    MOTOR_L_FWD = 2
    MOTOR_L_BWD = 2
    MOTOR_L_PWM = 2

    TRACKING_L1 = 2
    TRACKING_L2 = 2
    TRACKING_R1 = 2
    TRACKING_R2 = 2

    IR_L = 2
    IR_R = 2

    BUZZER = 2

    SEEKLIGHT_L = 2
    SEEKLIGHT_R = 2

    RGB_R = 2  
    RGB_G = 2
    RGB_B = 2






def write_angle(pin, angle_degree):
    if type(pin)==list:
        for p in pin:
            write_angle(p, angle_degree)
            
    if pin not in SERVO_PINS:
        raise ValueError('pin must be in SERVO_PINS, i.e. be connected to a servo motor.')

    if angle_degree<=90 and angle_degree>=-90:
        GPIO.output(pin, GPIO.LOW) 
        time.sleep(0.02)

        GPIO.output(pin, GPIO.HIGH) 
        time.sleep(0.0015+0.0005*angle_degree/90)

        GPIO.output(pin, GPIO.LOW) 
    else:
        raise ValueError('angle_degree should be from -90 to 90.')


def move(d: Direction):
    MOTOR_R = [MOTOR_R_FWD,MOTOR_R_BWD,MOTOR_R_PWM]
    MOTOR_L = [MOTOR_L_FWD,MOTOR_L_BWD,MOTOR_L_PWM]
    if   d == Direction.FWD:
        GPIO.output(MOTOR_R+MOTOR_L, GPIO.LOW)
        GPIO.output([MOTOR_R_FWD,MOTOR_L_FWD], GPIO.HIGH)
    elif d == Direction.BWD:
        GPIO.output(MOTOR_R+MOTOR_L, GPIO.LOW)
        GPIO.output([MOTOR_R_BWD,MOTOR_L_BWD], GPIO.HIGH)
    elif d == Direction.RCW:
        GPIO.output(MOTOR_R+MOTOR_L, GPIO.LOW)
        GPIO.output([MOTOR_R_FWD,MOTOR_L_BWD], GPIO.HIGH)
    elif d == Direction.RCCW:
        GPIO.output(MOTOR_R+MOTOR_L, GPIO.LOW)
        GPIO.output([MOTOR_R_BWD,MOTOR_L_FWD], GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(MOTOR_R+MOTOR_L, GPIO.LOW)    
    pass




GPIO.setmode(GPIO.BOARD)

OUT_PINS = [CAM_SERVO1,CAM_SERVO2,ECHO_SERVO1,MOTOR_R_FWD,MOTOR_R_BWD,MOTOR_R_PWM,
            MOTOR_L_FWD,MOTOR_L_BWD,MOTOR_L_PWM,BUZZER]

TRACKING_L1,TRACKING_L2,TRACKING_R1,TRACKING_R2 
IR_L,IR_R
SEEKLIGHT_L,SEEKLIGHT_R
RGB_R,RGB_G,RGB_B

GPIO.setup(OUT_PINS, GPIO.OUT, initial=GPIO.LOW)
