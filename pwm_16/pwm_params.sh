#!/bin/bash

dutycycle=$2
period=$1
#echo 1000000000 > /sys/class/pwm/pwmchip0/pwm0/period
echo "$period" > /sys/class/pwm/pwmchip2/pwm1/period
echo "$dutycycle" > /sys/class/pwm/pwmchip2/pwm1/duty_cycle

