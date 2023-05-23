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
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <linux/kdev_t.h>

#define LED_FILE_NAME "/dev/led_driver"
#define SM_FILE_NAME "/dev/step_motor_driver"
#define PHOTOREGISTER_FILE_NAME "/dev/photoregister_driver"

extern "C"
{	
	// led 켜기
	Export void ledOn()
	{
		int fd;
		char led_control;

		fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		led_control = 0;
		write(fd, &led_control, sizeof(char));

		close(fd);
	}

	// led 끄기
	Export void ledOff()
	{
		int fd;
		char led_control;

		fd = open(LED_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		led_control = 1;
		write(fd, &led_control, sizeof(char));

		close(fd);
	}

	
	// 스텝모터 정방향 회전
	Export void stepMotorCW()
	{
		int fd;
		char sm_run;

		fd = open(SM_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		sm_run = '1';
		write(fd, &sm_run, sizeof(char));

		close(fd);
	}

	// 스텝모터 역방향 회전
	Export void stepMotorCCW()
	{
		int fd;
		char sm_run;

		fd = open(SM_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		sm_run = '2';
		write(fd, &sm_run, sizeof(char));

		close(fd);
	}

	// 조도센서 밝기 가져오기
	Export int getBrightness()
	{
		int fd;
		int brightness;

		fd = open(PHOTOREGISTER_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error\n");
			return -1;
		}

		read(fd, &brightness, sizeof(int));
		close(fd);

		return brightness;
	}
}
