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
	EXPORT void ledOn()
	{
		int fd = open(LED_FILE_NAME, O_RDWR);

		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error : %s\n", LED_FILE_NAME);
			return;
		}

		char led_control = 0;
		write(fd, &led_control, sizeof(char));

		close(fd);
		return;
	}

	// led 끄기
	EXPORT void ledOff()
	{
		int fd = open(LED_FILE_NAME, O_RDWR);

		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error : %s\n", LED_FILE_NAME);
			return;
		}

		char led_control = 1;
		write(fd, &led_control, sizeof(char));

		close(fd);
		return;
	}

	// 스텝모터 정방향 회전
	EXPORT void stepMotorCW()
	{
		int fd = open(SM_FILE_NAME, O_RDWR);

		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error : %s\n", SM_FILE_NAME);
			return;
		}
		char sm_control = 1;
		write(fd, &sm_control, sizeof(char));
		close(fd);
		return;
	}

	// 스텝모터 역방향 회전
	EXPORT void stepMotorCCW()
	{
		int fd = open(SM_FILE_NAME, O_RDWR);

		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error : %s\n", SM_FILE_NAME);
			return;
		}

		char sm_control = 2;
		write(fd, &sm_control, sizeof(char));

		close(fd);
		return;
	}

	// 조도센서 밝기 가져오기
	EXPORT int getBrightness()
	{
		int fd = open(PHOTOREGISTER_FILE_NAME, O_RDWR);

		if (fd < 0)
		{
			fprintf(stderr, "Device Open Error : %s\n", PHOTOREGISTER_FILE_NAME);
			return -1;
		}

		int brightness;
		read(fd, &brightness, sizeof(int));
		close(fd);

		return brightness;
	}

	// 조도센서 테스트용 (조도센서 값 출력)
	EXPORT void printPhotoregisterValue()
	{
		int fd = open(PHOTOREGISTER_FILE_NAME, O_RDWR);
		if (fd < 0)
		{
			fprintf(stderr, "Can't open %s\n", LED_FILE_NAME);
			return;
		}

		char value;
		read(fd, &value, sizeof(char));
		printf("Value : %s", value);

		close(fd);
		return;
	}
}
