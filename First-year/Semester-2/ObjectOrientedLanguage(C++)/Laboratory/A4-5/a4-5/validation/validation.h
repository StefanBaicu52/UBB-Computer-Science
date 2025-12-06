#ifndef VALIDATION_H
#define VALIDATION_H

#include <string>

bool is_only_letters(const std::string& str);
bool is_only_digits(const std::string& str);
bool is_valid_number(const std::string& str);
bool is_valid_age_input(int age);

#endif // VALIDATION_H
