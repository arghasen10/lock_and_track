from time import sleep
import magnetometer
import servo

starting_angle = magnetometer.get_magnetometer_reading()
print('starting_angle', starting_angle)
flag = 0
count = 0
rotate_ccw = 0.0001
rotate_cw = -0.17
destination_angle = starting_angle + 90

while True:
    angle_val = magnetometer.get_magnetometer_reading()
    if angle_val > destination_angle:
        while angle_val > destination_angle:
            angle_val = magnetometer.get_magnetometer_reading()
            servo.rotate(rotate_ccw)
    elif angle_val < destination_angle:
        while angle_val < destination_angle:
            angle_val = magnetometer.get_magnetometer_reading()
            servo.rotate(rotate_cw)
    servo.stop()
    break

ending_angle = magnetometer.get_magnetometer_reading()
print('ending_angle', ending_angle)