//
// thread_3.c - Utilizare semafor pentru sincronizare
//
// 1. Generati 100.000 de numere aleatoare si calculati suma lor utilizand 100 thread-uri.
//

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define NUM_THR 100
#define CHUNK_SIZE 1000
#define MAX_NUM 100000

int sum = 0;
int numbers[MAX_NUM];

sem_t sem;

// Rutina de start
void* do_sum(void *a)
{
	int min = *(int *)a;
	//printf("min = %d\n", min);
	
	int i;
	int max = min + CHUNK_SIZE;
	for (i = min; i < max; i++)
	{
		sem_wait(&sem);
		sum += numbers[i];
		sem_post(&sem);
	}

	return NULL;
}


int main(int argc, char *argv[])
{
	pthread_t t[NUM_THR];

	// cream un semafor
	sem_init(&sem, 1, 1);

	// generam 100.000 numere aleatoare
	int i;
	srand(time(NULL));
	for (i = 0; i < MAX_NUM; i++)
	{
		numbers[i] = rand() % 20;
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

	// verificam suma
	int check_sum = 0;
	for (i = 0; i < MAX_NUM; i++)
	{
		check_sum += numbers[i];
	}

	printf("Suma verificata: %d\n", check_sum);

	// distrugem semaforul
	sem_destroy(&sem);

	return 0;
}
