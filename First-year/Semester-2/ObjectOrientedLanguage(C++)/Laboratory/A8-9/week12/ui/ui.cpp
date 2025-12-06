// #include "ui.h"
// #include <iostream>
// #include "../validation/validation.h"
// #include "../repository/AdoptionList.h"
// #include "../exceptions/exceptions.h"
//
// using namespace std;
//
// int UI::main_menu() {
//     int mode;
//     cout << "\n\n===== [KEEP CALM AND ADOPT A PET] =====\n";
//     cout << "CHOOSE USER OR SHUT DOWN SESSION:\n";
//     cout << "|1| admin\n|2| user\n|3| SHUT DOWN\n";
//
//     cout << "Input: ";
//     cin >> mode;
//
//     try {
//         UIValidator::validate_main_menu(mode);
//     } catch (const UIException& e) {
//         cout << e.what() << endl;
//         return -1;
//     }
//
//     switch (mode) {
//         case 1: admin_menu(); break;
//         case 2: user_menu(); break;
//         case 3: cout << "SHUTTING DOWN...\n"; return 0;
//     }
//
//     return 0;
// }
//
// void UI::admin_menu() {
//     while (true) {
//         int option;
//         cout << "\n[ADMIN MENU]\n";
//         cout << "|1| ADD DOG\n|2| DELETE DOG\n|3| UPDATE DOG\n|4| SEE ALL DOGS\n|5| LOG OUT\n";
//         cout << "Input: ";
//
//         string input;
//         cin >> input;
//
//         try {
//             UIValidator::validate_admin_menu(input);
//             option = stoi(input);
//         } catch (const UIException& e) {
//             cout << e.what() << endl;
//             continue;
//         }
//
//         switch (option) {
//             case 1: adm_op1(); break;
//             case 2: adm_op2(); break;
//             case 3: adm_op3(); break;
//             case 4: adm_op4(); break;
//             case 5: cout << "LOGGING OUT.\n"; return;
//         }
//     }
// }
//
// void UI::adm_op1() {
//     cout << "Enter dog details (name, breed, age, photograph): ";
//     string name, breed, age_str, photograph;
//     int age;
//
//     cin >> name >> breed >> age_str >> photograph;
//
//     try {
//         if (name.empty() || breed.empty() || age_str.empty() || photograph.empty())
//             throw UIException("All fields must be filled in.");
//
//         UIValidator::validate_digits_only(age_str);
//         age = stoi(age_str);
//         UIValidator::validate_age(age);
//
//         Dog dog(name, breed, age, photograph);
//         DogValidator::validate(dog);
//
//         if (!serv.photoIsUnique(dog.get_photograph()))
//             throw UIException("Photograph link must be unique!");
//
//         serv.addDog(dog);
//         cout << "Dog successfully added!\n";
//     } catch (const exception& e) {
//         cout << "Error: " << e.what() << endl;
//     }
// }
//
// void UI::adm_op2() {
//     string photograph;
//     cout << "\n[ADMIN MENU]\n";
//     cout << "Input photograph link of the dog to remove: ";
//     cin >> photograph;
//
//     if (serv.photoIsUnique(photograph)) {
//         cout << "Invalid input! Photograph link does not exist.\n";
//         return;
//     }
//
//     if (!serv.isAdopted(photograph)) {
//         char answer;
//         while (true) {
//             cout << "This dog is not adopted. Are you sure you want to remove it? (y/n): ";
//             cin >> answer;
//             if (answer == 'y') break;
//             if (answer == 'n') { cout << "Operation cancelled.\n"; return; }
//             cout << "Invalid input! Must be 'y' or 'n'.\n";
//         }
//     }
//
//     bool returnValue = serv.adminRemoveService(photograph);
//     cout << (returnValue ? "Successfully removed the dog!\n" : "Failed to remove the dog.\n");
// }
//
// void UI::adm_op3() {
//     string photograph, name, breed, age_str;
//     int age;
//
//     cout << "\n[ADMIN MENU]\n";
//     cout << "Input photograph link of the dog you wish to update: ";
//     cin >> photograph;
//
//     if (serv.photoIsUnique(photograph)) {
//         cout << "Invalid input! Photograph link does not exist\n";
//         return;
//     }
//
//     cout << "Input new name: ";
//     while (true) {
//         cin >> name;
//         try {
//             UIValidator::validate_letters_only(name);
//             break;
//         } catch (const UIException& e) {
//             cout << e.what() << " Try again: ";
//         }
//     }
//
//     cout << "Input new breed: ";
//     while (true) {
//         cin >> breed;
//         try {
//             UIValidator::validate_letters_only(breed);
//             break;
//         } catch (const UIException& e) {
//             cout << e.what() << " Try again: ";
//         }
//     }
//
//     cout << "Input new age: ";
//     while (true) {
//         cin >> age_str;
//         try {
//             UIValidator::validate_digits_only(age_str);
//             age = stoi(age_str);
//             UIValidator::validate_age(age);
//             break;
//         } catch (const exception& e) {
//             cout << "Invalid input! Try again: ";
//         }
//     }
//
//     bool returnValue = serv.adminUpdateService(photograph, name, breed, age);
//     cout << (returnValue ? "Successfully updated the dog!\n" : "Failed to update the dog.\n");
// }
//
// void UI::adm_op4() {
//     cout << "\n[ADMIN MENU]\n";
//     cout << "SEE ALL DOGS\n";
//     vector<Dog>& dogs = serv.getServiceDogs();
//     for (size_t i = 0; i < dogs.size(); i++) {
//         cout << '[' << i + 1 << "]\n" << dogs[i].dog_to_string();
//     }
//     cout << "\nThat's all!\n";
// }
//
// void UI::user_menu() {
//     string format;
//     cout << "Choose adoption file format (csv/html): ";
//     cin >> format;
//
//     try {
//         UIValidator::validate_save_mode(format);
//     } catch (const UIException& e) {
//         cout << e.what() << " Defaulting to CSV.\n";
//         format = "csv";
//     }
//
//     if (format == "csv")
//         serv.setAdoptionList(new CSVOutput());
//     else
//         serv.setAdoptionList(new HTMLOutput());
//
//     while (true) {
//         string input;
//         cout << "\n[USER MENU]\n";
//         cout << "|1| SEE DOGS ONE BY ONE\n|2| FILTER DOGS\n|3| SEE ADOPTION LIST\n|4| OPEN FILE\n|5| LOG OUT\n";
//         cout << "Input: ";
//         cin >> input;
//
//         try {
//             UIValidator::validate_user_menu(input);
//         } catch (const UIException& e) {
//             cout << e.what() << endl;
//             continue;
//         }
//
//         int option = stoi(input);
//         switch (option) {
//             case 1: user_op1(); break;
//             case 2: user_op2(); break;
//             case 3: user_op3(); break;
//             case 4: user_op4(); break;
//             case 5: cout << "LOGGING OUT.\n"; return;
//         }
//     }
// }
//
// void UI::user_op1() {
//     vector<Dog>& dogs = serv.getServiceDogs();
//     int total = dogs.size();
//     if (total == 0) {
//         cout << "No dogs available!\n";
//         return;
//     }
//
//     int index = 0;
//     while (true) {
//         bool allAdopted = all_of(dogs.begin(), dogs.end(), [](const Dog& d) { return d.get_adopted(); });
//         if (allAdopted) {
//             cout << "All dogs have been adopted!\n";
//             break;
//         }
//
//         index %= total;
//         if (!dogs[index].get_adopted()) {
//             cout << "------------------------------------------\n";
//             cout << dogs[index].dog_to_string();
//             cout << "Adopt this dog? (y = yes, n = next, q = quit): ";
//             string input;
//             cin >> input;
//             if (input == "y") {
//                 bool adopted = serv.userAdoptService(dogs[index].get_photograph());
//                 cout << (adopted ? "Successfully adopted!\n" : "Failed to adopt.\n");
//             } else if (input == "q") {
//                 cout << "Exiting...\n";
//                 break;
//             }
//         }
//         index++;
//     }
// }
//
// void UI::user_op2() {
//     cout << "SEE DOGS BY BREED AND AGE\n";
//     string breed, age_str;
//     int age;
//
//     cin.ignore();
//     while (true) {
//         cout << "Input breed (leave empty for all): ";
//         getline(cin, breed);
//         try {
//             if (!breed.empty())
//                 UIValidator::validate_letters_only(breed);
//             break;
//         } catch (const UIException& e) {
//             cout << e.what() << endl;
//         }
//     }
//
//     while (true) {
//         cout << "Input max age: ";
//         cin >> age_str;
//         try {
//             UIValidator::validate_digits_only(age_str);
//             age = stoi(age_str);
//             UIValidator::validate_age(age);
//             break;
//         } catch (const UIException& e) {
//             cout << e.what() << endl;
//         }
//     }
//
//     vector<Dog> filtered = serv.getDogsByBreedAndAge(breed, age);
//     if (filtered.empty()) {
//         cout << "No dogs found.\n";
//     } else {
//         for (size_t i = 0; i < filtered.size(); ++i) {
//             cout << '[' << i + 1 << "]\n" << filtered[i].dog_to_string();
//         }
//     }
// }
//
// void UI::user_op3() {
//     vector<Dog>& adopted = serv.getUserAdoptionList();
//     if (adopted.empty()) {
//         cout << "No dogs adopted yet.\n";
//         return;
//     }
//     for (size_t i = 0; i < adopted.size(); ++i) {
//         cout << '[' << i + 1 << "]\n" << adopted[i].dog_to_string();
//     }
// }
//
// void UI::user_op4() {
//     serv.openAdoptionFile();
// }
