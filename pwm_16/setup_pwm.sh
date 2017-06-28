##only for exporting pin 22 port 9 as pwm output
##by: udit kumar agarwal
echo BB-PWM2 > /sys/devices/platform/bone_capemgr/slots
echo "done!!"
echo 1 > /sys/class/pwm/pwmchip2/export
ls /sys/class/pwm/pwmchip2/pwm1/ | grep "export"
