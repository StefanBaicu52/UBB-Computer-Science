#pragma once
#include <string>
#include <iostream>
using namespace std;
class Dog {
private:
    string name;
    string breed;
    int age;
    string photograph;
    bool adopted;

public:
    //constructors
    Dog();
    Dog(const string& name, const string& breed, const int& age, const string& photograph);

    //getters
    string get_name() const { return name; }
    string get_breed() const { return breed; }
    int get_age() const { return age; }
    string get_photograph() const { return photograph; }
    bool get_adopted() const { return adopted; }

    //setters
    void set_name(const string& new_name) { name = new_name; }
    void set_breed(const string& new_breed) { breed = new_breed; }
    void set_age(int new_age) { age = new_age; }
    void set_photograph(const string& new_photo) { photograph = new_photo; }
    void set_adopted(bool value) { adopted = value; }

    //UI output format
    string dog_to_string();

    //stream operators
    friend ostream& operator<<(ostream& os, const Dog& dog);
    friend istream& operator>>(istream& is, Dog& dog);
};
