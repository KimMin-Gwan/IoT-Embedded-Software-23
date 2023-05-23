#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#include <vector>
#include <numeric>

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

	// led 켜기
	Export void ledOn(){
		int fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0){
			fprintf(stderr, "Device Open Error : %s\n", LED_FILE_NAME);
			return -1;
		}

		char led_onoff = 0;
		write(fd, &led_onoff, sizeof(char));

		close(fd);
	}

	// led 끄기
	Export void ledOff(){
		int fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0){
			fprintf(stderr, "Device Open Error : %s\n", LED_FILE_NAME);
			return -1;
		}

		char led_onoff = 1;
		write(fd, &led_onoff, sizeof(char));

		close(fd);
	}

	// 스텝모터 정방향 회전
	Export void stepMotorCW(){
      int fd = open(STEPMOTOR_FILE_NAME, O_RDWR);
      if(fd < 0){
         fprintf(stderr, "Device Open Error : %s\n", STEPMOTOR_FILE_NAME);
         return -1;
      }
	  
	 char sm_run = 1;
	  write(fd, &sm_run, sizeof(char));

	  close(fd);
	}

	// 스텝모터 역방향 회전
	Export void stepMotorCCW(){
      int fd = open(STEPMOTOR_FILE_NAME, O_RDWR);
      if(fd < 0){
         fprintf(stderr, "Device Open Error : %s\n", STEPMOTOR_FILE_NAME);
         return -1;
      }
	  
	  char sm_run = 2;
	  write(fd, &sm_run, sizeof(char));

	  close(fd);
	}

	// 조도센서 밝기 가져오기
	Export int getBrightness(){
		int fd = open(PHOTOREGISTER_FILE_NAME, O_RDWR);
		if(fd < 0){
			fprintf(stderr, "Device Open Error : %s\n", PHOTOREGISTER_FILE_NAME);
			return -1;
		}

		read(fd, &brightness, sizeof(int));
		close(fd);

		return brightness;
	}

	// 조도센서로 LED 제어
	Export void ledRun(){
		int fd = open(LED_FILE_NAME, O_RDWR);

    	if(fd < 0){
			fprintf(stderr, "Device Open Error : %s\n", LED_FILE_NAME);
			return -1;
			}

		int brightness = getBrightness();

		if(data != 1){
			fprintf(stderr, "Failed to read from Photo Register Device");
			return -1;
		}

		char led_state = write(fd, &brightness, sizeof(int));

		if(led_state != 1){
			fprintf(stderr, "Failed to write to LED Device");
			return -1;
		}

		close(fd);
	}

	// 조도센서로 스텝모터 제어
	Export void stepMotorRun(){
		int fd = open(STEP_MOTOR_FILE_NAME, O_RDWR);

    	if(fd < 0){
			fprintf(stderr, "Device Open Error : %s\n", STEPMOTOR_FILE_NAME);
			return -1;
			}

		int brightness = getBrightness();

		if(data != 1){
			fprintf(stderr, "Failed to read from Photo Register Device");
			return -1;
		}

		char step_motor_state = write(fd, &brightness, sizeof(int));

		if(step_motor_state != 1){
			fprintf(stderr, "Failed to write to Step Motor Device");
			return -1;
		}

		close(fd);
	}


}






	