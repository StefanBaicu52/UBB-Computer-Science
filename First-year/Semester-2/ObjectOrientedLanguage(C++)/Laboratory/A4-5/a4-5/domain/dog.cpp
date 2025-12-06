#include "dog.h"
Dog::Dog() {
    this->name = "";
    this->breed = "";
    this->age = 0;
    this->photograph = "";
    this->adopted = false;
}
Dog::Dog(const string& name, const string& breed, const int& age, const string& photograph) {
    this->name = name;
    this->breed = breed;
    this->age = age;
    this->photograph = photograph;
    this->adopted = false;
}

string Dog :: dog_to_string() {
    return "NAME: " + name + "\n"
           "BREED: " + breed +
           "\nAGE: " + to_string(age) +
           "\nPHOTOGRAPH LINK: https://kcaaap.com/dogs-photos/" + photograph + "\n\n";
}
