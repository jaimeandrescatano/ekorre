# import RPi.GPIO as GPIO

"""
Manejo de excepciones


"""
import sys


try:
    import RPi.GPIO as GPIO
    
except RuntimeError:
    falla0 = sys.exc_info()[0] # - me da el tipo del error
    falla1 = sys.exc_info()[1] # - me da el valor del error
    
    print falla0
    print falla1
    
    # print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
