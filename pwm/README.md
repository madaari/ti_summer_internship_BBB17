##Error:
<pre>
debian@beaglebone:/sys/class/pwm/pwmchip0/pwm0$ uname -a
Linux beaglebone 4.4.68-ti-r107 #1 SMP Fri Jun 2 05:07:11 UTC 2017 armv7l GNU/Linux
debian@beaglebone:/sys/class/pwm/pwmchip0/pwm0$ sudo python
[sudo] password for debian: 
Python 2.7.9 (default, Aug 13 2016, 17:56:53) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import Adafruit_BBIO.PWM as PWM
>>> PWM.start("P9_22",50,1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Problem with the cape manager
>>> exit()
</pre>
##Possible Explaination of error<br>
Adafruit library requires universal_cape to be loaded for proper working and pin muxing is handled by bone_capemgr, thus, problem with bone cape mgr suggest a possible issue with pin muxing between universl cape and Adafruit_BBIO.PWM .<br>
<br>

##Temporary Solution<br>
Untill, Adafruit releases a patch for this, we can currently use the following bash scripts to control pwm.<br>
These set of scripts will initiate pwm using bash on pin 22 port 9.<br>
First run setup_pwm.sh // This will export the dtbo, and will enable pwmchip0<br>
then run pwm_params.sh as pwm_params.sh <period> <duty_cycle> //to set period and duty_cycle(in nano seconds) of pwm signal<br>
then run enable_pwm.sh to turn on pwm signal<br>
then disable_pwm to turn off pwm signal<br>
