/*

// dllmain.cpp : DLL 애플리케이션의 진입점을 정의합니다.
#include "pch.h"

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

*/

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
    EXPORT void ledOn()
    {
        int fd = open(LED_FILE_NAME, O_RDWR);
        if (fd < 0)
        {
            fprintf(stderr, "Can't open %s\n", LED_FILE_NAME);
            return;
        }
        char data = 1;

        write(fd, &data, sizeof(char));
    }

    EXPORT void ledOff()
    {
        int fd = open(LED_FILE_NAME, O_RDWR);
        if (fd < 0)
        {
            fprintf(stderr, "Can't open %s\n", LED_FILE_NAME);
            return;
        }

        char data = 0;

        write(fd, &data, sizeof(char));
    }
}

