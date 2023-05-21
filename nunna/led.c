#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/stat.h> 
#include <fcntl.h> 
#include <linux/kdev_t.h>
#include <linux/poll.h>

#define	KEY_NAME	“/dev/LED_DRIVER”
#define TIMEOUT 5

int main(void){
	int key_fd, retval;
	char key, led_onoff = 0;
	struct pollfd events;	

	key_fd = open(KEY_NAME, O_RDWR|O_NONBLOCK);	
	if (key_fd < 0)					
	{
		fprintf(stderr, "Device Open Error\n");
		return -1;
	}

	while (1)

	{   //KEY_NAME 이벤트 감시 준비
		events.fd = key_fd; 
		events.events = POLLIN; 

        //poll system call 호출
		retval = poll(events, 1, TIMEOUT * 1000);  
	                
		if (retval < 0)	//호출 오류
		{
			fprintf(stderr, “poll error\n”);
			return -1;
		}

		if (retval == 0) //이벤트 발생x
		{
			// puts(“LED off”);
			// led_onoff = 0;		
			// write(fd, &led_onoff, 1);	
            puts("")
        }

		if (events.revents & POLLIN)
		{
            
			led_onoff = 1;		
			write(key_fd, &led_onoff, 1);	
			read(key_fd, &key, 1);	
            printf(“key : %d\n”, key);	// Print the number of switch on			sleep(2);			// LED on during 2 seconds
		}
	}
	led_onoff = 0;
	write(key_fd, &led_onoff, 1);
	close(key_fd);
}
