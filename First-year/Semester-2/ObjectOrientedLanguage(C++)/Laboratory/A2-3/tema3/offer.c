#include "offer.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Offer* createOffer(const char* type, const char* destination, const char* departureDate, double price) {
    Offer* offer = (Offer*)malloc(sizeof(Offer));
    offer->type = strdup(type);
    offer->destination = strdup(destination);
    offer->departureDate = strdup(departureDate);
    offer->price = price;
    return offer;
}

void destroyOffer(Offer* offer) {
    if (!offer) return;
    free(offer->type);
    free(offer->destination);
    free(offer->departureDate);
    free(offer);
}

void printOffer(const Offer* offer) {
    printf("Type: %s | Destination: %s | Date: %s | Price: $%.2f\n",
           offer->type, offer->destination, offer->departureDate, offer->price);
}
