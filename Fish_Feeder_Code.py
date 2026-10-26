from machine import Pin, deepsleep
from time import sleep

motor = Pin(0, Pin.OUT)

sleep(1)  # allow power to settle

motor.on()
sleep(5)
motor.off()

deepsleep(12 * 60 * 60 * 1000) # Device enters deepsleep for 12 hours