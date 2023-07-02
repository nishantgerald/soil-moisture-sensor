import machine
from time import sleep

# Assigning pin to GPIO-05
pin = machine.Pin(5, machine.Pin.OUT)

#Setting number of iterations
iterations = 10

def LED_flash(iterations=10): 
    for i in range(1,iterations):
        print(i)
        pin.on()
        sleep (0.1)
        pin.off()
        sleep (0.1)

def main():
    LED_flash(iterations)
    
if __name__ == "__main__":
    main()