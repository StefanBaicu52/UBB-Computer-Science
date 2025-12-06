#ifndef DYNAMIC_ARRAY_H
#define DYNAMIC_ARRAY_H

#include "offer.h"

typedef struct {
    Offer** data;   // Array of pointers to Offers
    int size;
    int capacity;
} DynamicArray;

DynamicArray* createArray(int capacity);
void destroyArray(DynamicArray* arr);
void addOffer(DynamicArray* arr, Offer* offer);
void removeOffer(DynamicArray* arr, int index);
void updateOffer(DynamicArray* arr, int index, Offer* newOffer);
Offer** getAllOffers(DynamicArray* arr, int* count);

#endif // DYNAMIC_ARRAY_H
