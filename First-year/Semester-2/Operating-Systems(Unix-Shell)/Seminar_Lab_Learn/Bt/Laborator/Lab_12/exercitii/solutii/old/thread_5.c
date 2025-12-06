//
// thread_5.c - Fara sincronizare
//
// 2. Cititi 100.000 de numere dintr-un fisier binar cu numere aleatoare si determinati
// numarul de divizori ai lui 5 utilizand 100 thread-uri.
//

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/stat.h> 
#include <fcntl.h>
#include <unistd.h>

#define NUM_THR 100
#define CHUNK_SIZE 1000
#define MAX_NUM 100000

int sum = 0;
int numbers[MAX_NUM];

// Rutina de start
void* do_sum(void *a)
{
	int min = *(int *)a;
	//printf("min = %d\n", min);

	int i;
	int max = min + CHUNK_SIZE;
	for (i = min; i < max; i++)
	{
		sum += numbers[i];
	}

	free(a);

	return NULL;
}


int main(int argc, char *argv[])
{
	pthread_t t[NUM_THR];

	// // generam 100.000 numere aleatoare
	// int i;
	// srand(time(NULL));
	// for (i = 0; i < MAX_NUM; i++)
	// {
	// 	numbers[i] = rand() % 20;
	// }

	// deschidem fisierul binar
	int fd = open("random-file.bin", O_RDONLY);

	// citim 100.000 numere
	int i;
	for (i = 0; i < MAX_NUM; i++)
	{
		read(fd, &numbers[i], 2);
	}

	// cream 100 thread-uri
	for (i = 0; i < NUM_THR; i++)
	{
		int *n = (int *)malloc(sizeof(int));
		*n = i * CHUNK_SIZE;
		pthread_create(&t[i], NULL, do_sum, n);
	}

	// asteptam terminarea thread-urilor
	for (i = 0; i < NUM_THR; i++)
	{
		pthread_join(t[i], NULL);
	}

	// afisam rezultatul
	printf("Suma calculata:  %d\n", sum);

	close(fd);

	return 0;
}
