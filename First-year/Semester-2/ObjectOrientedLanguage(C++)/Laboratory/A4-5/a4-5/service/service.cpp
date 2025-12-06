#include "service.h"

void Service::addDog(Dog& dog) {
    this->repoAdmin.addRepoDog(dog);
}


void Service::adoptDog(const Dog& d) {
    this->repoUser.addAdoptedDog(d);
}


// ADMIN: returneaza cainii din shelter
DynamicArray<class Dog>& Service::getServiceDogs() {
    return this->repoAdmin.getRepoDogs();
}

// ADMIN: verifica daca un linke unic
bool Service::photoIsUnique(const string& photo) {
    DynamicArray<class Dog>& dogs = repoAdmin.getRepoDogs();
    for (int i = 0; i < dogs.getSize(); i++)
        if (dogs[i].get_photograph() == photo)
            return false;
    return true;
}

// ADMIN:add un câine nou
bool Service::adminAddService(const string& name, const string& breed, int age, const string& photograph) {
    Dog dog(name, breed, age, photograph);
    return this->repoAdmin.addRepoDog(dog);
}

// ADMIN:sterge un caine dupa link fotografie
bool Service::adminRemoveService(const string& photograph) {
    return this->repoAdmin.removeRepoDog(photograph);
}

// ADMIN: Verifica daca un caine e adoptat
bool Service::isAdopted(const string& photograph) {
    DynamicArray<class Dog>& dogs = repoAdmin.getRepoDogs();
    for (int i = 0; i < dogs.getSize(); i++)
        if (dogs[i].get_photograph() == photograph)
            return dogs[i].get_adopted();
    return false;
}

// ADMIN: Actualizeaza datele unui caine
bool Service::adminUpdateService(const string& photograph, const string& name, const string& breed, int age) {
    DynamicArray<class Dog>& dogs = repoAdmin.getRepoDogs();
    for (int i = 0; i < dogs.getSize(); i++)
        if (dogs[i].get_photograph() == photograph) {
            return this->repoAdmin.updateRepoDog(dogs[i], name, breed, age);
        }
    return false;
}

// USER: marcheaza ca adoptat și adauga in lista userului
bool Service::userAdoptService(const string& photograph) {
    DynamicArray<class Dog>& dogs = repoAdmin.getRepoDogs();
    for (int i = 0; i < dogs.getSize(); i++) {
        if (dogs[i].get_photograph() == photograph && !dogs[i].get_adopted()) {
            dogs[i].set_adopted(true);
            this->repoUser.addAdoptedDog(dogs[i]);
            return true;
        }
    }
    return false;
}

// USER:return lista de caini adoptati
DynamicArray<Dog>& Service::getUserAdoptionList() {
    return this->repoUser.getAdoptedDogs();
}


DynamicArray<Dog> Service::getDogsByBreedAndAge(const std::string& breed, int maxAge) {
    DynamicArray<Dog> allDogs = repoAdmin.getRepoDogs();
    DynamicArray<Dog> result;

    for (int i = 0; i < allDogs.getSize(); i++) {
        bool match_breed = (breed.empty() || allDogs[i].get_breed() == breed);
        bool match_age = (allDogs[i].get_age() < maxAge);

        if (match_breed && match_age) {
            result.addElem(allDogs[i]);
        }
    }

    return result;
}
