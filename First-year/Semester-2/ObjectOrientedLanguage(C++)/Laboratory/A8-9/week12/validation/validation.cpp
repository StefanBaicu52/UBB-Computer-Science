#include "validation.h"

void UIValidator::validate_main_menu(int input) {
    if (input < 1 || input > 3)
        throw UIException("Main menu input must be between 1 and 3.");
}

void UIValidator::validate_digits_only(const std::string& str) {
    if (str.empty() || !all_of(str.begin(), str.end(), ::isdigit))
        throw UIException("Input must contain digits only!");
}

void UIValidator::validate_admin_menu(const std::string& input) {
    // Verificam daca input-ul este un numar valid
    if (input.empty() || !std::all_of(input.begin(), input.end(), ::isdigit)) {
        throw UIException("Invalid input! Must be a number.");
    }

    int option = std::stoi(input);  // Convertim string-ul intr-un numar

    // Verificam daca optiunea este in intervalul valid (1-5)
    if (option < 1 || option > 5) {
        throw UIException("Admin menu input must be between 1 and 5.");
    }
}

void UIValidator::validate_user_menu(const std::string& input) {
    // Verificam daca input-ul este un numar valid
    if (input.empty() || !std::all_of(input.begin(), input.end(), ::isdigit)) {
        throw UIException("Invalid input! Must be a number.");
    }

    int option = std::stoi(input);  // Convertim string-ul intr-un numar

    // Verificam daca optiunea este in intervalul valid (1-5)
    if (option < 1 || option > 5) {
        throw UIException("User menu input must be between 1 and 5.");
    }
}

void UIValidator::validate_save_mode(const std::string& save_mode) {
    if (save_mode != "csv" && save_mode != "html")
        throw UIException("Invalid save mode! Must be 'csv' or 'html'.");
}

void UIValidator::validate_letters_only(const std::string& str) {
    if (str.empty() || !std::all_of(str.begin(), str.end(), ::isalpha))
        throw UIException("Input must contain only letters!");
}

void UIValidator::validate_age(int age) {
    if (age < 0 || age > 100)
        throw UIException("Age must be between 0 and 100!");
}

void UIValidator::validate_empty(const std::string& str) {
    if (str.empty())
        throw UIException("Input cannot be empty!");
}


void DogValidator::validate(const Dog& dog) {
    const std::string& name = dog.get_name();
    const std::string& breed = dog.get_breed();
    int age = dog.get_age();
    const std::string& photo = dog.get_photograph();

    if (name.empty() || !std::all_of(name.begin(), name.end(), ::isalpha)) {
        throw UIException("Dog name must contain only letters!");
    }

    if (breed.empty() || !std::all_of(breed.begin(), breed.end(), ::isalpha)) {
        throw UIException("Dog breed must contain only letters!");
    }

    if (age < 0 || age > 100) {
        throw UIException("Dog age must be between 0 and 100!");
    }

    if (photo.empty()) {
        throw UIException("Photograph link cannot be empty!");
    }
}

