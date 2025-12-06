#ifndef REPOSITORY_H
#define REPOSITORY_H

#include "dynamic_array.h"

typedef struct {
    DynamicArray* offers;
} Repository;

// Repository Functions
Repository* createRepository();
void destroyRepository(Repository* repo);
void repoAddOffer(Repository* repo, Offer* offer);
void repoDeleteOffer(Repository* repo, const char* destination, const char* departureDate);
Offer** repoGetAllOffers(Repository* repo, int* count);

#endif // REPOSITORY_H
