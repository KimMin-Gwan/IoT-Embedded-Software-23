cmd_/root/raspberry/app/IoT-Embedded-Software-23/Device_Driver/step_motor/Module.symvers :=  sed 's/ko$$/o/'  /root/raspberry/app/IoT-Embedded-Software-23/Device_Driver/step_motor/modules.order | scripts/mod/modpost -m -a    -o /root/raspberry/app/IoT-Embedded-Software-23/Device_Driver/step_motor/Module.symvers -e -i Module.symvers -T - 