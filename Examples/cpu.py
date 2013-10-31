##########################################################
## Show your current CPU usage on your PiGlow!          ##
##                                                      ##
## Requires psutil - sudo apt-get install python-psutil ##
##                                                      ##
## Example by Jason - @Boeeerb                          ##
##########################################################

from piglow import PiGlow
from time import sleep
import psutil

piglow = PiGlow()

while True:

    cpu = psutil.cpu_percent()
    piglow.all(0)

    if cpu < 1:
        piglow.white(0)
    elif cpu < 10:
        piglow.white(5)
    elif cpu < 20:
        piglow.white(10)
        piglow.blue(20)
    elif cpu < 40:
        piglow.white(10)
        piglow.blue(35)
        piglow.green(35)
    elif cpu < 60:
        piglow.white(20)
        piglow.blue(40)
        piglow.green(40)
        piglow.yellow(40)
    elif cpu < 80:
        piglow.white(20)
        piglow.blue(40)
        piglow.green(40)
        piglow.yellow(40)
        piglow.orange(100)
    else:
        piglow.all(20)
    sleep(0.2)
