#ifndef SERVICE_H
#define SERVICE_H

#include "repository.h"

typedef struct {
    Repository* repo;

    // Undo/Redo Stack
    Repository** undoStack;
    int undoSize;
    int undoCapacity;

    Repository** redoStack;
    int redoSize;
    int redoCapacity;

} Service;

// Service Functions
Service* createService(Repository* repo);
void destroyService(Service* service);

// Offer Management
void serviceAddOffer(Service* service, const char* type, const char* destination, const char* departureDate, double price);
void serviceDeleteOffer(Service* service, const char* destination, const char* departureDate);
Offer** serviceGetAllOffers(Service* service, int* count);

// Filtering
Offer** serviceFilterByDestination(Service* service, const char* search, int* count);
Offer** serviceFilterByDate(Service* service, const char* date, int* count);

// Undo/Redo
void serviceUndo(Service* service);
void serviceRedo(Service* service);

#endif // SERVICE_H
