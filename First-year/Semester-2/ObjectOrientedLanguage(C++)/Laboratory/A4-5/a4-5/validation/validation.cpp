#include "validation.h"
#include <cctype>  // for isalpha
#include <iostream>
#include <sstream>

using namespace std;

// Checks if a string contains only letters
bool is_only_letters(const std::string& str)
{
    for (char c : str)
    {
        if (!isalpha(c))  // Checks if the character is a letter
            return false;
    }
    return true;
}



// Checks if the age input is valid
bool is_valid_age_input(int age)
{
    // Checks if the age is between 0 and 100
    if (age < 0 || age > 100) {
        return false;  // The age is not valid
    }

    return true;  // The age is valid
}

// Checks if a string contains only digits
bool is_only_digits(const std::string& str)
{
    for (char c : str) {
        if (!isdigit(c)) {  // Checks if the character is not a digit
            return false;
        }
    }
    return true;  // If all characters are digits
}



// Checks if a string contains only digits
bool is_valid_number(const std::string& str)
{
    stringstream ss(str);
    int number;
    ss >> number;

    // Checks if the input can be converted to a number and if there are no remaining characters
    if (ss.eof() && !ss.fail()) {
        return true;  // It's a valid number
    } else {
        return false;  // It's not a valid number
    }
}