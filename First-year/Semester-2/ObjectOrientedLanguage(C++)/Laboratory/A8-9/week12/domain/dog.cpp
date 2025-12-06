#include "dog.h"
#include <sstream>
#include <iostream>

#include "../validation/validation.h"
using namespace std;
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

string Dog::dog_to_string() const{
    return "NAME: " + name + "\n" +
           "BREED: " + breed + "\n" +
           "AGE: " + to_string(age) + "\n" +
           "PHOTOGRAPH LINK: https://kcaaap.com/dogs-photos/" + photograph + "\n";
}

ostream& operator<<(ostream& os, const Dog& dog) {
    os << dog.get_name() << ","
       << dog.get_breed() << ","
       << dog.get_age() << ","
       << dog.get_photograph() << ","
       << dog.get_adopted() << "\n";
    return os;
}

istream& operator>>(istream& is, Dog& dog) {
    string line;
    if (!getline(is, line))
        return is;

    stringstream ss(line);
    string name, breed, age_str, photo, adopted_str;

    //citirea campurilor
    getline(ss, name, ',');
    getline(ss, breed, ',');
    getline(ss, age_str, ',');
    getline(ss, photo, ',');
    getline(ss, adopted_str, ',');

    dog.set_name(name);
    dog.set_breed(breed);
    dog.set_age(stoi(age_str));
    dog.set_photograph(photo);
    dog.set_adopted(stoi(adopted_str));

    return is;
}

