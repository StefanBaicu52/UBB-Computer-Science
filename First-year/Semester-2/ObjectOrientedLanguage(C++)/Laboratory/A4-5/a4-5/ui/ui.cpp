#include <iostream>
#include "ui.h"
#include "../service/service.h"
#include "../dynamic_vector/dynamic_vector.h"
#include "../validation/validation.h"

using namespace std;

int UI::main_menu() {

    int mode;
    cout << "\n\n";
    cout << "   =====[KEEP CALM AND ADOPT A PET]===== \n\n";
    cout << "CHOOSE USER OR SHUT DOWN SESSION:\n";
    cout << "|1| admin\n";
    cout << "|2| user\n";
    cout << "|3| SHUT DOWN\n\n";

    cout << "Input: ";
    try
    {
        cin >> mode;
        if (mode < 1 || mode > 3)
            throw std::runtime_error("\n\nInvalid input! Must be between 1 and 3.");
    }
    catch (exception& e)
    {
        cout << e.what() << endl;
        return -1;
    }

    switch (mode)
    {
        case 1:
        {
            admin_menu();
            break;
        }
        case 2:
        {
            user_menu();
            break;
        }
        case 3:
        {
            cout<< "SHUTTING DOWN... ";
            return 0;
            break;
        }
        default:
            // This is a catch-all branch for cases not covered
            cout << "\n\nInvalid input! Please choose between 1, 2, or 3." << endl;
        return -1;
    }
    return 0;
}

void UI::admin_menu()
{
    while (true)
    {
        int option;

        cout << "\n\n";
        cout << "      [[USER: admin]]\n";
        cout << "   =====[MAIN MENU]=====\n\n";
        cout << "CHOOSE OPTION:\n";
        cout << "|1| ADD DOG\n";
        cout << "|2| DELETE DOG\n";
        cout << "|3| UPDATE DOG\n";
        cout << "|4| SEE ALL DOGS\n";
        cout << "|5| LOG OUT\n\n";

        cout << "Input: ";
        try
        {
            cin >> option;
            if (option < 1 || option > 5)
                throw std::runtime_error("\n\nInvalid input! Must be between 1 and 3.");  // Using std::runtime_error
        }
        catch (exception& e)
        {
            cout << e.what() << endl;
        }

        switch (option)
        {
        case 1:
        {
            adm_op1();
            break;
        }
        case 2:
        {
            adm_op2();
            break;
        }
        case 3:
        {
            adm_op3();
            break;
        }
        case 4:
        {
            adm_op4();
            break;
        }
        case 5:
        {
            cout << "LOGGING OUT. ";
            return;
            break;
        }
            default:
                // This is a catch-all branch for cases not covered
                    cout << "\n\nInvalid input! Please choose between 1, 2, or 3." << endl;
        }
    }
}

void UI::adm_op1()
{
    string breed, name, photograph, age_input;
    int age;

    cout << "\n\n";
    cout << "     [[USER: admin]]\n";
    cout << "   =====[ADD DOG]=====\n\n";
    cout << "PLEASE PROVIDE THE FOLLOWING INFORMATION:\n";

    // Validation for breed
    while (true) {
        cout << "Input breed: ";
        cin >> breed;
        if (!is_only_letters(breed)) {
            cout << "\nInvalid input! Breed must contain only letters.\n";
        } else {
            break;
        }
    }

    // Validation for name
    while (true) {
        cout << "Input name: ";
        cin >> name;
        if (!is_only_letters(name)) {
            cout << "\nInvalid input! Name must contain only letters.\n";
        } else {
            break;
        }
    }

    // Validation for age (as string to avoid issues with special characters)
    while (true) {
        cout << "Input age: ";
        cin >> age_input;

        // Check if age is a valid number
        if (!is_only_digits(age_input)) {
            cout << "\nInvalid input! Age must be a number.\n";
        } else {
            age = stoi(age_input); // Convert valid input to int
            if (age < 0 || age > 100) {
                cout << "\nInvalid input! Age must be between 0 and 100.\n";
            } else {
                break;  // If age is valid, exit the loop
            }
        }
    }

    // Validation for photograph link
    while (true) {
        cout << "Input photograph link (just the part after https://kcaaap.com/dogs-photos/): ";
        cin >> photograph;

        if (!serv.photoIsUnique(photograph)) {
            cout << "\nInvalid input! Photograph link is not unique!" << endl;
            return;  // Exit the function if the link is not unique
        }

        if (photograph.empty()) {
            cout << "\nInvalid input! Photograph link cannot be empty.\n";
        } else {
            break;  // Exit the loop if the input is valid
        }
    }

    // If everything is valid, add the dog
    bool returnValue = serv.adminAddService(breed, name, age, photograph);
    if (returnValue)
        cout << "\nSuccessfully added the dog!" << endl;
    else
        cout << "\nSomething went wrong while trying to add.." << endl;

    return;
}

void UI::adm_op2()
{
    string photograph;
    cout << "\n\n";
    cout << "       [[USER: admin]]\n";
    cout << "   =====[REMOVE DOG]=====\n\n";
    cout << "PLEASE PROVIDE THE FOLLOWING INFORMATION:\n";

    // Validation for photograph link
    while (true) {
        cout << "Input photograph link of the dog you wish deleted (just the part after https://kcaaap.com/dogs-photos/): ";
        cin >> photograph;

        // Check if the photograph link is valid and exists
        bool res = serv.photoIsUnique(photograph);
        if (res) {
            cout << "\nInvalid input! Photograph link does not exist.\n";
        } else {
            break;  // If the link is valid, exit the loop
        }
    }

    // Check if the dog is adopted
    if (!serv.isAdopted(photograph)) {
        char answer;
        while (true) {
            cout << "\nWait! This dog has not been adopted yet! Are you sure you want to remove it? Enter (y/n): ";
            cin >> answer;

            // Validate response 'y' or 'n'
            if (answer != 'y' && answer != 'n') {
                cout << "\nInvalid input! Must be 'y' or 'n'. Please enter again.\n";
            } else {
                break;  // If the input is valid, exit the loop
            }
        }

        if (answer == 'n') {
            cout << "\nOperation cancelled.\n";
            return;  // If the answer is 'n', cancel the operation
        }
    }

    // If everything is valid, try to remove the dog
    bool returnValue = serv.adminRemoveService(photograph);
    if (returnValue)
        cout << "\nSuccessfully removed the dog!\n";
    else
        cout << "\nSomething went wrong while trying to remove..\n";
}

void UI::adm_op3()
{
    string photograph, name, breed, age_input;
    int age;

    cout << "\n\n";
    cout << "     [[USER: admin]]\n";
    cout << "   =====[UPDATE DOG]=====  \n\n";
    cout << "PLEASE PROVIDE THE FOLLOWING INFORMATION:\n";
    cout << "Input photograph link of the dog you wish to update (just the part after https://kcaaap.com/dogs-photos/): ";
    cin >> photograph;

    bool res = serv.photoIsUnique(photograph);
    if (res) {
        cout << "Invalid input! Photograph link does not exist\n";
    } else {
        // Validation for name
        while (true) {
            cout << "Input new name: ";
            cin >> name;
            if (!is_only_letters(name)) {
                cout << "\nInvalid input! Name must contain only letters.\n";
            } else {
                break;
            }
        }

        // Validation for breed
        while (true) {
            cout << "Input new breed: ";
            cin >> breed;
            if (!is_only_letters(breed)) {
                cout << "\nInvalid input! Breed must contain only letters.\n";
            } else {
                break;
            }
        }

        // Validation for age (as string to avoid issues with special characters)
        while (true) {
            cout << "Input new age: ";
            cin >> age_input;

            // Check if age is a valid number
            if (!is_only_digits(age_input)) {
                cout << "\nInvalid input! Age must be a number.\n";
            } else {
                age = stoi(age_input); // Convert valid input to int
                if (age < 0 || age > 100) {
                    cout << "\nInvalid input! Age must be between 0 and 100.\n";
                } else {
                    break;  // If age is valid, exit the loop
                }
            }
        }

        // After validating all information, update the dog
        int returnValue = serv.adminUpdateService(photograph, name, breed, age);
        if (returnValue)
            cout << "\nSuccessfully updated the dog!";
        else
            cout << "\nSomething went wrong while trying to update..\n";
    }

    return;
}

void UI::adm_op4()
{
    cout << "\n\n";
    cout << "       [[USER: admin]]\n";
    cout << "   =====[SEE ALL DOGS]=====\n\n";
    cout << "ALL DOGS FOUND:\n";

    DynamicArray<class Dog>& dogs = serv.getServiceDogs();
    for (int i = 0; i < dogs.getSize(); i++)
    {
        cout << '[' << i + 1 << ']' << '\n' << dogs[i].dog_to_string();
    }
    cout << "\nThat's all!";
}




///-----------------------------------------------------UI USER-----------------------------------------------------///
void UI::user_menu()
{
    while (true)
    {
        int option;
        string input;
        cout << "   [[USER: user]]\n";
        cout << "   [MAIN MENU]\n\n";
        cout << "CHOOSE OPTION:\n";
        cout << "|1| SEE DOGS ONE BY ONE\n";
        cout << "|2| SEE ALL DOGS OF A GIVEN BREED YOUNGER THAN AN AGE\n";
        cout << "|3| SEE ADOPTION LIST\n";
        cout << "|4| LOG OUT\n\n";

        cout << "Input: ";

        bool valid_input = false;

        while (!valid_input)
        {
            cout << "Input: ";
            cin >> input;

            if (!is_only_digits(input)) {
                cout << "\nInvalid input! Please enter a number between 1 and 4.\n";
                continue;
            }

            try {
                option = stoi(input);           // convertim stringul la int

                if (option < 1 || option > 4)
                    cout << "\nInvalid input! Please enter a number between 1 and 4.\n";
                else
                    valid_input = true;
            }
            catch (exception& e) {
                cout << "\nError converting input. Try again.\n";
            }
        }

        switch (option)
        {
        case 1:
        {
            user_op1();
            break;
        }
        case 2:
        {
            user_op2();
            break;
        }
        case 3:
        {
            user_op3();
            break;
        }
        case 4:
        {
            cout << "LOGGING OUT. ";
            return;
            break;
        }
            default:
                // This is a catch-all branch for cases not covered
                    cout << "\n\nInvalid input!Please choose between 1, 2, or 3."<< endl;
        }
    }
}

void UI::user_op1()
{
    DynamicArray<Dog>& dogs = serv.getServiceDogs();
    int totalDogs = dogs.getSize();

    if (totalDogs == 0) {
        std::cout << "\nNo dogs available!\n";
        return;
    }

    std::cout << "\n   [[USER: user]]";
    std::cout << "\n   [SEE UNADOPTED DOGS]\n\n";

    int index = 0;

    while (true) {
        // dacă toți câinii au fost adoptați, ieșim
        bool allAdopted = true;
        for (int i = 0; i < totalDogs; ++i) {
            if (!dogs[i].get_adopted()) {
                allAdopted = false;
                break;
            }
        }
        if (allAdopted) {
            std::cout << "\nAll dogs have been adopted!\n";
            break;
        }

        index = index % totalDogs;

        if (!dogs[index].get_adopted()) {
            std::cout << "------------------------------------------\n";
            std::cout << dogs[index].dog_to_string() << "\n";

            std::string input;
            char answer;

            std::cout << "Do you want to adopt this dog?(y = yes, n = next, q = quit): ";
            std::cin >> input;

            while (input.length() != 1 || (input[0] != 'y' && input[0] != 'n' && input[0] != 'q')) {
                std::cout << "Invalid input! Please enter 'y', 'n' or 'q': ";
                std::cin >> input;
            }

            answer = input[0];

            if (answer == 'y') {
                bool adopted = serv.userAdoptService(dogs[index].get_photograph());

                if (adopted) {
                    std::cout << "You have successfully adopted the dog!\n";
                } else {
                    std::cout << "Failed to adopt. The dog may already be adopted.\n";
                }
            } else if (answer == 'q') {
                std::cout << "Exiting dog list.\n";
                break;
            } else {
                std::cout << "Skipping to next dog...\n";
            }
        }

        index++;
    }

    std::cout << "\nReturning to main menu...\n";
}


void UI::user_op2()
{
    std::cout << "   [[USER: user]]\n";
    std::cout << "   [SEE DOGS OF A GIVEN BREED YOUNGER THAN AN AGE]\n\n";

    std::string breed;
    std::string age_str;
    int age;

    // === VALIDARE BREED ===
    while (true) {
        std::cout << "Input breed (leave empty for all breeds): ";
        std::cin.ignore();  // curatam bufferul
        std::getline(std::cin, breed);

        if (breed.empty() || is_only_letters(breed)) {
            break;
        } else {
            std::cout << "Invalid input! Breed must contain only letters.\n";
        }
    }

    // === VALIDARE AGE ===
    while (true) {
        std::cout << "Input max age: ";
        std::cin >> age_str;

        if (!is_only_digits(age_str)) {
            std::cout << "Invalid input! Age must be numeric.\n";
            continue;
        }

        age = std::stoi(age_str);
        if (!is_valid_age_input(age)) {
            std::cout << "Invalid age! Must be between 1 and 100.\n";
            continue;
        }

        break;  // input corect
    }

    // === CEREM DE LA SERVICE ===
    DynamicArray<Dog> filteredDogs = serv.getDogsByBreedAndAge(breed, age);

    if (filteredDogs.getSize() == 0) {
        std::cout << "\nNo dogs found matching the criteria.\n";
    } else {
        std::cout << "\nDOGS FOUND:\n";
        for (int i = 0; i < filteredDogs.getSize(); i++) {
            std::cout << '[' << i + 1 << "]\n" << filteredDogs[i].dog_to_string() << '\n';
        }
    }

    std::cout << "\nReturning to main menu...\n";
}




void UI::user_op3()
{
    std::cout << "   [[USER: user]]\n";
    std::cout << "   [ADOPTION LIST]\n\n";

    DynamicArray<Dog>& adoptedDogs = serv.getUserAdoptionList();

    if (adoptedDogs.getSize() == 0) {
        std::cout << "You haven't adopted any dogs yet.\n";
    } else {
        std::cout << "ALL ADOPTED DOGS:\n";
        for (int i = 0; i < adoptedDogs.getSize(); i++) {
            std::cout << '[' << i + 1 << "]\n" << adoptedDogs[i].dog_to_string() << '\n';
        }
    }

    std::cout << "\nReturning to main menu...\n";
}
