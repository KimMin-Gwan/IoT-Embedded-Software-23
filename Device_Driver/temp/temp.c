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
    //led 켜기
    EXPORT void ledOn()
    {
        int fd = open(LED_FILE_NAME, O_RDWR);
        if (fd < 0)
        {
            fprintf(stderr, "Can't open %s\n", LED_FILE_NAME);
            return;
        }
        char data = 0;

        write(fd, &data, sizeof(char));

        close(fd);
    }

    // led 끄기
    EXPORT void ledOff()
    {
        int fd = open(LED_FILE_NAME, O_RDWR);
        if (fd < 0)
        {
            fprintf(stderr, "Can't open %s\n", LED_FILE_NAME);
            return;
        }

        char data = 1;

        write(fd, &data, sizeof(char));

        close(fd);
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
        fprintf("Value : %d", value);

        close(fd);
    }
}