#include "ui.h"
#include <iostream>
#include "../validation/validation.h"
#include "../repository/AdoptionList.h"
#include "../exceptions/exceptions.h"

using namespace std;

int UI::main_menu() {
    int mode;
    cout << "\n\n===== [KEEP CALM AND ADOPT A PET] =====\n";
    cout << "CHOOSE USER OR SHUT DOWN SESSION:\n";
    cout << "|1| admin\n|2| user\n|3| SHUT DOWN\n";

    cout << "Input: ";
    cin >> mode;

    try {
        UIValidator::validate_main_menu(mode); // validam inputul
    } catch (const UIException& e) {
        cout << e.what() << endl;
        return -1;
    }

    switch (mode) {
        case 1: admin_menu(); break;
        case 2: user_menu(); break;
        case 3: cout << "SHUTTING DOWN...\n"; return 0;
    }

    return 0;
}

void UI::admin_menu() {
    while (true) {
        int option;
        cout << "\n[ADMIN MENU]\n";
        cout << "|1| ADD DOG\n|2| DELETE DOG\n|3| UPDATE DOG\n|4| SEE ALL DOGS\n|5| LOG OUT\n";
        cout << "Input: ";

        string input;
        cin >> input;

        try {
            UIValidator::validate_admin_menu(input);    // validam inputul
            option = std::stoi(input);  // convertesc inputul intr un numar
        } catch (const UIException& e) {
            cout << e.what() << endl;
            continue;   // daca validarea facuta esueaza continuam sa cerem input
        }

        switch (option) {
            case 1: adm_op1(); break;
            case 2: adm_op2(); break;
            case 3: adm_op3(); break;
            case 4: adm_op4(); break;
            case 5: cout << "LOGGING OUT.\n"; return;
            default:
                cout << "Invalid option! Please choose a number between 1 and 5.\n";
            break;
        }
    }
}

void UI::adm_op1() {
    cout << "Enter dog details (name, breed, age, photograph): ";
    string name, breed, age_str, photograph;
    int age;

    // Citirea datelor
    cin >> name >> breed >> age_str >> photograph;

    try {
        // Verificam daca inputurile nu sunt goale
        if (name.empty() || breed.empty() || age_str.empty() || photograph.empty()) {
            throw UIException("All fields must be filled in.");
        }

        // validam daca varsta e un numar valid
        UIValidator::validate_digits_only(age_str);  // Validam ca este un numar
        age = std::stoi(age_str);  // Convertim in integer
        UIValidator::validate_age(age);  // Validam varsta

        // Cream obiectul Dog cu datele citite
        Dog dog(name, breed, age, photograph);

        // Validam cainele
        DogValidator::validate(dog);

        // Verificam unicitatea fotografiei
        if (!serv.photoIsUnique(dog.get_photograph())) {
            throw UIException("Photograph link must be unique!");
        }

        // Adaugam cainele
        serv.addDog(dog);
        cout << "Dog successfully added!\n";
    } catch (const UIException& e) {
        cout << e.what() << endl;
    } catch (const std::exception& e) {
        cout << "Error: " << e.what() << endl;
    }
}

void UI::adm_op2() {
    string photograph;
    cout << "\n[ADMIN MENU]\n";
    cout << "Input photograph link of the dog to remove: ";
    cin >> photograph;

    if (serv.photoIsUnique(photograph)) {
        cout << "Invalid input! Photograph link does not exist.\n";
        return;
    }

    if (!serv.isAdopted(photograph)) {
        char answer;
        while (true) {
            cout << "This dog is not adopted. Are you sure you want to remove it? (y/n): ";
            cin >> answer;
            if (answer == 'y') break;
            if (answer == 'n') { cout << "Operation cancelled.\n"; return; }
            cout << "Invalid input! Must be 'y' or 'n'.\n";
        }
    }

    bool returnValue = serv.adminRemoveService(photograph);
    cout << (returnValue ? "Successfully removed the dog!\n" : "Something went wrong while trying to remove..\n");
}

void UI::adm_op3() {
    string photograph, name, breed, age_str;
    int age;

    cout << "\n[ADMIN MENU]\n";
    cout << "Input photograph link of the dog you wish to update: ";
    cin >> photograph;

    // Verificam daca fotografia exista
    if (serv.photoIsUnique(photograph)) {
        cout << "Invalid input! Photograph link does not exist\n";
        return;
    }

    // Citim numele cainelui si validam imediat
    cout << "Input new name: ";
    while (true) {
        cin >> name;
        try {
            UIValidator::validate_letters_only(name);  // Validam ca numele contine doar litere
            break;  // Iesim din bucla daca este valid
        } catch (const UIException& e) {
            cout << e.what() << " Please enter a valid name: ";
        }
    }

    // Citim rasa cainelui si validam imediat
    cout << "Input new breed: ";
    while (true) {
        cin >> breed;
        try {
            UIValidator::validate_letters_only(breed);  // Validam ca rasa contine doar litere
            break;  // Iesim din bucla daca este valid
        } catch (const UIException& e) {
            cout << e.what() << " Please enter a valid breed: ";
        }
    }

    // Citim varsta si validam
    cout << "Input new age: ";
    while (true) {
        cin >> age_str;
        try {
            UIValidator::validate_digits_only(age_str);  // Validam ca varsta este un numar
            age = stoi(age_str);  // Convertim varsta la integer
            UIValidator::validate_age(age);  // Verificam daca varsta este intr-un interval valid
            break;  // Iesim din bucla daca este valid
        } catch (const UIException& e) {
            cout << e.what() << " Please enter a valid age: ";
        } catch (const std::invalid_argument& e) {
            cout << "Input must be a valid number for age! Please try again: ";
        }
    }

    // Actualizam cainele in baza de date
    bool returnValue = serv.adminUpdateService(photograph, name, breed, age);
    cout << (returnValue ? "Successfully updated the dog!\n" : "Something went wrong while trying to update..\n");
}

void UI::adm_op4() {
    cout << "\n[ADMIN MENU]\n";
    cout << "SEE ALL DOGS\n";
    vector<Dog>& dogs = serv.getServiceDogs();
    for (size_t i = 0; i < dogs.size(); i++) {
        cout << '[' << i + 1 << "]\n" << dogs[i].dog_to_string();
    }
    cout << "\nThat's all!\n";
}

void UI::user_menu() {
    string format;
    cout << "Choose adoption file format (csv/html): ";
    cin >> format;

    try {
        UIValidator::validate_save_mode(format);
    } catch (const UIException& e) {
        cout << e.what() << " Defaulting to CSV.\n";
        format = "csv";
    }

    if (format == "csv")
        serv.setAdoptionList(new CSVOutput());
    else
        serv.setAdoptionList(new HTMLOutput());

    while (true) {
        string input;
        cout << "\n[USER MENU]\n";
        cout << "|1| SEE DOGS ONE BY ONE\n|2| SEE DOGS BY BREED AND AGE\n|3| SEE ADOPTION LIST\n|4| OPEN ADOPTION FILE\n|5| LOG OUT\n";
        cout << "Input: ";
        cin >> input;

        try {
            UIValidator::validate_user_menu(input);
        } catch (const UIException& e) {
            cout << e.what() << endl;
            continue;
        }

        int option = std::stoi(input);

        switch (option) {
            case 1: user_op1(); break;
            case 2: user_op2(); break;
            case 3: user_op3(); break;
            case 4: user_op4(); break;
            case 5: cout << "LOGGING OUT.\n"; return;
        }
    }
}

void UI::user_op1() {
    vector<Dog>& dogs = serv.getServiceDogs();
    int totalDogs = dogs.size();

    if (totalDogs == 0) {
        cout << "No dogs available!\n";
        return;
    }

    cout << "\n[USER MENU]\n";
    cout << "SEE UNADOPTED DOGS\n";
    int index = 0;

    while (true) {
        bool allAdopted = all_of(dogs.begin(), dogs.end(), [](const Dog& d) { return d.get_adopted(); });
        if (allAdopted) {
            cout << "All dogs have been adopted!\n";
            break;
        }

        index %= totalDogs;
        if (!dogs[index].get_adopted()) {
            cout << "------------------------------------------\n";
            cout << dogs[index].dog_to_string();

            string input;
            cout << "Adopt this dog? (y = yes, n = next, q = quit): ";
            cin >> input;
            while (input != "y" && input != "n" && input != "q") {
                cout << "Invalid input! Please enter 'y', 'n' or 'q': ";
                cin >> input;
            }

            if (input == "y") {
                bool adopted = serv.userAdoptService(dogs[index].get_photograph());
                cout << (adopted ? "Successfully adopted!\n" : "Failed to adopt.\n");
            } else if (input == "q") {
                cout << "Exiting dog list.\n";
                break;
            } else {
                cout << "Next dog...\n";
            }
        }

        index++;
    }

    cout << "Returning to main menu...\n";
}

void UI::user_op2() {
    cout << "\n[USER MENU]\n";
    cout << "SEE DOGS BY BREED AND AGE\n";
    string breed, age_str;
    int age;

    cin.ignore();
    while (true) {
        cout << "Input breed (leave empty for all): ";
        getline(cin, breed);
        try {
            if (!breed.empty())
                UIValidator::validate_letters_only(breed);
            break;
        } catch (const UIException& e) {
            cout << e.what() << endl;
        }
    }

    while (true) {
        cout << "Input max age: ";
        cin >> age_str;
        try {
            UIValidator::validate_digits_only(age_str);
            age = stoi(age_str);
            UIValidator::validate_age(age);
            break;
        } catch (const UIException& e) {
            cout << e.what() << endl;
        }
    }

    vector<Dog> filteredDogs = serv.getDogsByBreedAndAge(breed, age);
    if (filteredDogs.empty()) {
        cout << "No dogs found matching the criteria.\n";
    } else {
        for (size_t i = 0; i < filteredDogs.size(); i++) {
            cout << '[' << i + 1 << "]\n" << filteredDogs[i].dog_to_string();
        }
    }

    cout << "Returning to main menu...\n";
}

void UI::user_op3() {
    cout << "\n[USER MENU]\n";
    cout << "ADOPTION LIST\n";
    vector<Dog>& adoptedDogs = serv.getUserAdoptionList();
    if (adoptedDogs.empty()) {
        cout << "You haven't adopted any dogs yet.\n";
    } else {
        for (size_t i = 0; i < adoptedDogs.size(); i++) {
            cout << '[' << i + 1 << "]\n" << adoptedDogs[i].dog_to_string();
        }
    }
    cout << "Returning to main menu...\n";
}

void UI::user_op4() {
    serv.openAdoptionFile();
}
