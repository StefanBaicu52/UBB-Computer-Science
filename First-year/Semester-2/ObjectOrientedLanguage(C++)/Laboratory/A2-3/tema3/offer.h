#ifndef OFFER_H
#define OFFER_H

typedef struct {
    char* type;           // Dynamically allocated string
    char* destination;    // Dynamically allocated string
    char* departureDate;  // Dynamically allocated string (Format: "YYYY-MM-DD")
    double price;
} Offer;

Offer* createOffer(const char* type, const char* destination, const char* departureDate, double price);
void destroyOffer(Offer* offer);
void printOffer(const Offer* offer);

#endif // OFFER_H
