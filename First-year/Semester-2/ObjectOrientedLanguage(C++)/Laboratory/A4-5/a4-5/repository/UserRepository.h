
// UserRepository.h
#pragma once
#include "../domain/dog.h"
#include "../dynamic_vector/dynamic_vector.h"

class RepoUser {
private:
    DynamicArray<Dog> adoptedDogs;
public:
    RepoUser();
    ~RepoUser();

    void addAdoptedDog(const Dog& dog);
    DynamicArray<Dog>& getAdoptedDogs();
};

