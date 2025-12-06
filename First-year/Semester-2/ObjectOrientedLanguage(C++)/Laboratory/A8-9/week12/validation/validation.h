#pragma once
#include "../exceptions/exceptions.h"
#include <string>
#include "../domain/dog.h"
#include <algorithm>
class UIValidator {
public:
    static void validate_main_menu(int input);
    static void validate_admin_menu(const std::string& input);
    static void validate_user_menu(const std::string& input);


    static void validate_save_mode(const std::string& mode);


    static void validate_letters_only(const std::string& str);
    static void validate_digits_only(const std::string& str);
    static void validate_age(int age);
    static void validate_empty(const std::string& str);

};


class DogValidator {
public:
    static void validate(const Dog& dog);
};