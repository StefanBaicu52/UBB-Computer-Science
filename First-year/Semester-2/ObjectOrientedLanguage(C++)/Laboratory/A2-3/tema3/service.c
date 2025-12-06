#include "service.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Create a Service instance
Service* createService(Repository* repo) {
    Service* service = (Service*)malloc(sizeof(Service));
    service->repo = repo;

    // Initialize Undo/Redo Stack
    service->undoCapacity = 10;
    service->undoSize = 0;
    service->undoStack = (Repository**)malloc(service->undoCapacity * sizeof(Repository*));

    service->redoCapacity = 10;
    service->redoSize = 0;
    service->redoStack = (Repository**)malloc(service->redoCapacity * sizeof(Repository*));

    return service;
}

// Destroy the Service
void destroyService(Service* service) {
    for (int i = 0; i < service->undoSize; i++) {
        destroyRepository(service->undoStack[i]);
    }
    free(service->undoStack);

    for (int i = 0; i < service->redoSize; i++) {
        destroyRepository(service->redoStack[i]);
    }
    free(service->redoStack);

    free(service);
}

// Save the current state for Undo/Redo
void saveState(Repository* src, Repository* dest) {
    destroyArray(dest->offers);
    dest->offers = createArray(src->offers->capacity);

    for (int i = 0; i < src->offers->size; i++) {
        Offer* copy = createOffer(
            src->offers->data[i]->type,
            src->offers->data[i]->destination,
            src->offers->data[i]->departureDate,
            src->offers->data[i]->price
        );
        addOffer(dest->offers, copy);
    }
}

// Push current state to Undo Stack
void pushUndo(Service* service) {
    if (service->undoSize == service->undoCapacity) {
        service->undoCapacity *= 2;
        service->undoStack = realloc(service->undoStack, service->undoCapacity * sizeof(Repository*));
    }
    service->undoStack[service->undoSize] = createRepository();
    saveState(service->repo, service->undoStack[service->undoSize]);
    service->undoSize++;
}

// Push current state to Redo Stack
void pushRedo(Service* service) {
    if (service->redoSize == service->redoCapacity) {
        service->redoCapacity *= 2;
        service->redoStack = realloc(service->redoStack, service->redoCapacity * sizeof(Repository*));
    }
    service->redoStack[service->redoSize] = createRepository();
    saveState(service->repo, service->redoStack[service->redoSize]);
    service->redoSize++;
}

// Add an Offer
void serviceAddOffer(Service* service, const char* type, const char* destination, const char* departureDate, double price) {
    pushUndo(service);
    Offer* offer = createOffer(type, destination, departureDate, price);
    repoAddOffer(service->repo, offer);
}

// Delete an Offer
void serviceDeleteOffer(Service* service, const char* destination, const char* departureDate) {
    pushUndo(service);
    repoDeleteOffer(service->repo, destination, departureDate);
}

// Get all Offers
Offer** serviceGetAllOffers(Service* service, int* count) {
    return repoGetAllOffers(service->repo, count);
}

// Filter Offers by Destination
Offer** serviceFilterByDestination(Service* service, const char* search, int* count) {
    int total;
    Offer** allOffers = serviceGetAllOffers(service, &total);
    Offer** filteredOffers = (Offer**)malloc(total * sizeof(Offer*));
    *count = 0;

    for (int i = 0; i < total; i++) {
        if (strstr(allOffers[i]->destination, search) != NULL) {
            filteredOffers[(*count)++] = allOffers[i];
        }
    }
    return filteredOffers;
}

// Filter Offers by Date (After given date)
Offer** serviceFilterByDate(Service* service, const char* date, int* count) {
    int total;
    Offer** allOffers = serviceGetAllOffers(service, &total);
    Offer** filteredOffers = (Offer**)malloc(total * sizeof(Offer*));
    *count = 0;

    for (int i = 0; i < total; i++) {
        if (strcmp(allOffers[i]->departureDate, date) > 0) { // Lexicographic comparison
            filteredOffers[(*count)++] = allOffers[i];
        }
    }
    return filteredOffers;
}

// Undo the last operation
void serviceUndo(Service* service) {
    if (service->undoSize == 0) {
        printf("No more undo actions available.\n");
        return;
    }

    pushRedo(service);
    service->undoSize--;
    saveState(service->undoStack[service->undoSize], service->repo);
}

// Redo the last undone operation
void serviceRedo(Service* service) {
    if (service->redoSize == 0) {
        printf("No more redo actions available.\n");
        return;
    }

    pushUndo(service);
    service->redoSize--;
    saveState(service->redoStack[service->redoSize], service->repo);
}
