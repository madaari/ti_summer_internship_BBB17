##only for exporting pin 22 port 9 as pwm output
##by: udit kumar agarwal
echo BB-PWM0 > /sys/devices/platform/bone_capemgr/slots
echo "done!!"
echo 0 > /sys/class/pwm/pwmchip0/export
ls /sys/class/pwm/pwmchip0/pwm0/ | grep "export"
