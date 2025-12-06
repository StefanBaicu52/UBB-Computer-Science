#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "repository.h"
#include "service.h"

void printMenu() {
    printf("\n--- Menu ---\n");
    printf("1. Add Offer\n");
    printf("2. Delete Offer\n");
    printf("3. Display All Offers\n");
    printf("4. Filter Offers by Destination\n");
    printf("5. Filter Offers by Date\n");
    printf("6. Undo\n");
    printf("7. Redo\n");
    printf("8. Exit\n");
    printf("Choose an option: ");
}

void printOffers(Offer** offers, int count) {
    for (int i = 0; i < count; i++) {
        printf("Offer Type: %s\n", offers[i]->type);
        printf("Destination: %s\n", offers[i]->destination);
        printf("Departure Date: %s\n", offers[i]->departureDate);
        printf("Price: %.2f\n", offers[i]->price);
        printf("------------\n");
    }
}

int main() {
    Repository* repo = createRepository();
    Service* service = createService(repo);

    int choice;
    char type[100], destination[100], departureDate[100];
    double price;
    int count;

    while (1) {
        printMenu();
        scanf("%d", &choice);
        getchar();  // Consume newline left by scanf

        switch (choice) {
            case 1:
                // Add Offer
                printf("Enter Offer Type: ");
                fgets(type, 100, stdin);
                type[strcspn(type, "\n")] = 0; // Remove newline character

                printf("Enter Destination: ");
                fgets(destination, 100, stdin);
                destination[strcspn(destination, "\n")] = 0;

                printf("Enter Departure Date (YYYY-MM-DD): ");
                fgets(departureDate, 100, stdin);
                departureDate[strcspn(departureDate, "\n")] = 0;

                printf("Enter Price: ");
                scanf("%lf", &price);

                serviceAddOffer(service, type, destination, departureDate, price);
                printf("Offer added successfully!\n");
                break;

            case 2:
                // Delete Offer
                printf("Enter Destination to delete: ");
                fgets(destination, 100, stdin);
                destination[strcspn(destination, "\n")] = 0;

                printf("Enter Departure Date (YYYY-MM-DD) to delete: ");
                fgets(departureDate, 100, stdin);
                departureDate[strcspn(departureDate, "\n")] = 0;

                serviceDeleteOffer(service, destination, departureDate);
                printf("Offer deleted successfully!\n");
                break;

            case 3:
                // Display All Offers
                {
                    Offer** offers = serviceGetAllOffers(service, &count);
                    printf("\n--- All Offers ---\n");
                    printOffers(offers, count);
                    free(offers);
                }
                break;

            case 4:
                // Filter Offers by Destination
                printf("Enter destination to filter: ");
                fgets(destination, 100, stdin);
                destination[strcspn(destination, "\n")] = 0;

                Offer** filteredOffers = serviceFilterByDestination(service, destination, &count);
                printf("\n--- Filtered Offers by Destination ---\n");
                printOffers(filteredOffers, count);
                free(filteredOffers);
                break;

            case 5:
                // Filter Offers by Date
                printf("Enter date to filter (YYYY-MM-DD): ");
                fgets(departureDate, 100, stdin);
                departureDate[strcspn(departureDate, "\n")] = 0;

                Offer** filteredByDate = serviceFilterByDate(service, departureDate, &count);
                printf("\n--- Filtered Offers by Date ---\n");
                printOffers(filteredByDate, count);
                free(filteredByDate);
                break;

            case 6:
                // Undo
                serviceUndo(service);
                printf("Undo action performed!\n");
                break;

            case 7:
                // Redo
                serviceRedo(service);
                printf("Redo action performed!\n");
                break;

            case 8:
                // Exit
                destroyService(service);
                destroyRepository(repo);
                printf("Exiting...\n");
                return 0;

            default:
                printf("Invalid option, try again.\n");
        }
    }

    return 0;
}
