// UserRepository.cpp
#include "UserRepository.h"

RepoUser::RepoUser() {}

RepoUser::~RepoUser() {}

void RepoUser::addAdoptedDog(const Dog& dog) {
    this->adoptedDogs.addElem(dog);
}

DynamicArray<Dog>& RepoUser::getAdoptedDogs() {
    return this->adoptedDogs;
}
