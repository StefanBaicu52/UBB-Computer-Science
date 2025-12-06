#include "dynamic_array.h"
#include <stdlib.h>
#include <stdio.h>

DynamicArray* createArray(int capacity) {
    DynamicArray* arr = (DynamicArray*)malloc(sizeof(DynamicArray));
    arr->data = (Offer**)malloc(capacity * sizeof(Offer*));
    arr->size = 0;
    arr->capacity = capacity;
    return arr;
}

void destroyArray(DynamicArray* arr) {
    for (int i = 0; i < arr->size; i++) {
        destroyOffer(arr->data[i]);
    }
    free(arr->data);
    free(arr);
}

void resizeArray(DynamicArray* arr) {
    arr->capacity *= 2;
    arr->data = (Offer**)realloc(arr->data, arr->capacity * sizeof(Offer*));
}

void addOffer(DynamicArray* arr, Offer* offer) {
    if (arr->size == arr->capacity) {
        resizeArray(arr);
    }
    arr->data[arr->size++] = offer;
}

void removeOffer(DynamicArray* arr, int index) {
    if (index < 0 || index >= arr->size) return;
    destroyOffer(arr->data[index]);
    for (int i = index; i < arr->size - 1; i++) {
        arr->data[i] = arr->data[i + 1];
    }
    arr->size--;
}

void updateOffer(DynamicArray* arr, int index, Offer* newOffer) {
    if (index < 0 || index >= arr->size) return;
    destroyOffer(arr->data[index]);
    arr->data[index] = newOffer;
}

Offer** getAllOffers(DynamicArray* arr, int* count) {
    *count = arr->size;
    return arr->data;
}
