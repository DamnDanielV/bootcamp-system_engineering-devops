#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>


/**
 * zombie_p - create a zombie process
 * Return: pid, child parent
 */
pid_t zombie_p(void)
{
	pid_t wa;

	wa = fork();

	if (wa)
	{
		printf("Zombie process created, PID: %d\n", wa);
		return (wa);
	}

	return (0);
}

/**
 * main - entry point
 * Return: 0
 */
int main(void)
{
	int i = 0;
	pid_t wa;

	while (i < 5)
	{
		wa = zombie_p();

		if (wa == 0)
			exit(0);
		i++;
	}
	pause();

	return (0);
}
