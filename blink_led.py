from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    on = False
    for i in range(0,20):
    
        if not on:
            GP.setLED(1)
        else:
            GP.setLED(0)
        on = not on
        time.sleep(1)

finally:
    GP.cleanup()
