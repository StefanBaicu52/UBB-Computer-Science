#include "repository.h"
#include <string.h>
#include <stdlib.h>

Repository* createRepository() {
    Repository* repo = (Repository*)malloc(sizeof(Repository));
    if (repo == NULL) {
        return NULL; // Allocation failed
    }
    repo->offers = createArray(10);
    return repo;
}

void destroyRepository(Repository* repo) {
    if (repo == NULL) return;

    destroyArray(repo->offers); // Free dynamic array
    free(repo); // Free repository struct
}

void repoAddOffer(Repository* repo, Offer* offer) {
    if (repo == NULL || offer == NULL) return;

    addOffer(repo->offers, offer);
}

void repoDeleteOffer(Repository* repo, const char* destination, const char* departureDate) {
    if (repo == NULL || destination == NULL || departureDate == NULL) return;

    int count;
    Offer** allOffers = getAllOffers(repo->offers, &count);

    for (int i = 0; i < count; i++) {
        if (strcmp(allOffers[i]->destination, destination) == 0 &&
            strcmp(allOffers[i]->departureDate, departureDate) == 0) {

            // Free the memory of the offer being deleted
            destroyOffer(allOffers[i]);

            // Remove from the dynamic array
            removeOffer(repo->offers, i);
            return;
            }
    }
}

Offer** repoGetAllOffers(Repository* repo, int* count) {
    if (repo == NULL || count == NULL) return NULL;

    return getAllOffers(repo->offers, count);
}
