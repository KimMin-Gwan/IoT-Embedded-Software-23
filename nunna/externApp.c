#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <fcntl.h> 
#include <linux/kdev_t.h>

#define	LED_FILE_NAME "/dev/led_driver"
#define STEPMOTOR_FILE_NAME "/dev/step_motor_driver"
#define PHOTOREGISTER_FILE_NAME "/dev/photoregister_driver"

extern "C"{
	Export void ledOn(){
		int fd;
		char *led_onoff;

		fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0){
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		led_onoff = 0;
		write(fd, &led_onoff, strlen(led_onoff));

		close(fd);
	}

	Export void ledOff(){
		int fd;
		char *led_onoff;

		fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0){
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		led_onoff = 1;
		write(fd, &led_onoff, strlen(led_onoff));

		close(fd);
	}

	Export void stepMotorCW(){
		int fd;
		char *sm_run;

      fd = open(STEPMOTOR_FILE_NAME, O_RDWR);
      if(fd < 0){
         fprintf(stderr, "Device Open Error\n");
         return -1;
      }
	  
	  sm_run = 1;
	  write(fd, &sm_run, strlen(sm_run));

	  close(fd);
	}

	Export void stepMotorCCW(){
		int fd;
		char *sm_run;

      fd = open(STEPMOTOR_FILE_NAME, O_RDWR);
      if(fd < 0){
         fprintf(stderr, "Device Open Error\n");
         return -1;
      }
	  
	  sm_run = 2;
	  write(fd, &sm_run, strlen(sm_run));

	  close(fd);
	}

}






	