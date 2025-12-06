#include "service.h"
#include <algorithm> // for std::find_if, std::copy_if

void Service::addDog(Dog& dog) {
    this->repoAdmin.addRepoDog(dog);
}

void Service::adoptDog(const Dog& d) {
    this->adoptionlist->addDog(d);//modificarea
}

//ADMIN: returns all dogs in the shelter
std::vector<Dog>& Service::getServiceDogs() {
    return this->repoAdmin.getRepoDogs();
}

//ADMIN: checks if a photograph link is unique
bool Service::photoIsUnique(const std::string& photo) {
    const auto& dogs = repoAdmin.getRepoDogs();
    return std::none_of(dogs.begin(), dogs.end(),
                        [&](const Dog& d) { return d.get_photograph() == photo; });
}

//ADMIN: adds a new dog
bool Service::adminAddService(const std::string& name, const std::string& breed, int age, const std::string& photograph) {
    Dog dog(name, breed, age, photograph);
    return this->repoAdmin.addRepoDog(dog);
}

//ADMIN: removes a dog by photograph link
bool Service::adminRemoveService(const std::string& photograph) {
    return this->repoAdmin.removeRepoDog(photograph);
}

// ADMIN: checks if a dog is adopted
bool Service::isAdopted(const std::string& photograph) {
    const auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](const Dog& d) { return d.get_photograph() == photograph; });
    return it != dogs.end() ? it->get_adopted() : false;
}

// ADMIN: updates a dog's information
bool Service::adminUpdateService(const std::string& photograph, const std::string& name, const std::string& breed, int age) {
    auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](Dog& d) { return d.get_photograph() == photograph; });
    if (it != dogs.end()) {
        return this->repoAdmin.updateRepoDog(*it, name, breed, age);
    }
    return false;
}

// USER: marks a dog as adopted and adds it to the user's list
bool Service::userAdoptService(const std::string& photograph) {
    auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](Dog& d) {
                               return d.get_photograph() == photograph && !d.get_adopted();
                           });

    if (it != dogs.end()) {
        it->set_adopted(true);
        this->adoptionlist->addDog(*it); //modificarea!!!
        return true;
    }
    return false;
}

//USER: returns the list of adopted dogs
std::vector<Dog>& Service::getUserAdoptionList() {
    return this->adoptionlist->getDogs();  // modificat
}

// USER: filters dogs by breed and maximum age
std::vector<Dog> Service::getDogsByBreedAndAge(const std::string& breed, int maxAge) {
    const auto& allDogs = repoAdmin.getRepoDogs();
    std::vector<Dog> result;

    std::copy_if(allDogs.begin(), allDogs.end(), std::back_inserter(result),
                 [&](const Dog& d) {
                     bool match_breed = breed.empty() || d.get_breed() == breed;
                     bool match_age = d.get_age() < maxAge;
                     return match_breed && match_age;
                 });

    return result;
}

//deschide lista adopțiilor(pt cerinta 5)
void Service::openAdoptionFile() {
    this->adoptionlist->openFile();
}



