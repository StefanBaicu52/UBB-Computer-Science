#include "tests.h"

#include "../service/service.h"
#include "../domain/dog.h"
#include "../repository/AdminRepository.h"
#include "../repository/UserRepository.h"
#include "../dynamic_vector/dynamic_vector.h"
#include "../validation/validation.h"

#include <iostream>
#include <cassert>

Tests::Tests() {}

void Tests::test_service() {
    Service service;

    assert(service.getServiceDogs().getSize() == 10);
    assert(service.photoIsUnique("photo") == true);
    assert(service.adminAddService("name", "breed", 1, "photo") == true);
    assert(service.isAdopted("photo") == false);
    assert(service.userAdoptService("photo") == true);
    assert(service.adminUpdateService("photo", "newName", "newBreed", 2) == true);
    assert(service.isAdopted("photo") == true);
    assert(service.getServiceDogs().getSize() == 11);
    assert(service.photoIsUnique("photo") == false);
    assert(service.adminRemoveService("photo") == true);
    assert(service.getServiceDogs().getSize() == 10);
    assert(service.userAdoptService("photo") == false);
    assert(service.isAdopted("photo") == false);

    DynamicArray<Dog> filtered1 = service.getDogsByBreedAndAge("ValidBreed", 10);
    assert(filtered1.getSize() >= 0);

    DynamicArray<Dog> filtered2 = service.getDogsByBreedAndAge("Pug", 3);
    assert(filtered2.getSize() >= 0);


    assert(service.isAdopted("nope.jpg") == false);

    auto all = service.getDogsByBreedAndAge("", 100);
    assert(all.getSize() >= 1);

    auto none = service.getDogsByBreedAndAge("notfound", 100);
    assert(none.getSize() == 0);
}

void Tests::test_repo() {
    RepoAdmin repo;

    assert(repo.getRepoDogs().getSize() == 10);
    assert(repo.removeRepoDog("photo") == true);
    assert(repo.getRepoDogs().getSize() == 10);

    Dog dog("name", "breed", 1, "photo");
    assert(repo.updateRepoDog(dog, "newName", "newBreed", 2) == true);
}

void Tests::test_user_repo() {
    RepoUser repo;
    Dog d("Max", "Poodle", 5, "m.jpg");
    repo.addAdoptedDog(d);
    auto all = repo.getAdoptedDogs();
    assert(all.getSize() == 1);
    assert(all[0].get_name() == "Max");
}

void Tests::test_dog() {
    Dog dog("name", "breed", 1, "photo");

    assert(dog.get_name() == "name");
    assert(dog.get_breed() == "breed");
    assert(dog.get_age() == 1);
    assert(dog.get_photograph() == "photo");
    assert(dog.get_adopted() == false);

    dog.set_name("newName");
    dog.set_breed("newBreed");
    dog.set_age(2);
    dog.set_photograph("newPhoto");
    dog.set_adopted(true);

    assert(dog.get_name() == "newName");
    assert(dog.get_breed() == "newBreed");
    assert(dog.get_age() == 2);
    assert(dog.get_photograph() == "newPhoto");
    assert(dog.get_adopted() == true);

    std::string s = dog.dog_to_string();
    assert(s.find("NAME: newName") != std::string::npos);
}

void Tests::test_dynamicArray() {
    DynamicArray<int> array;

    assert(array.getSize() == 0);
    array.addElem(1);
    assert(array.getSize() == 1);
    assert(array[0] == 1);
    array.removeElem(0);
    assert(array.getSize() == 0);

    DynamicArray<int> copy = array;
    DynamicArray<int> assigned;
    assigned = copy;
    assert(assigned.getSize() == copy.getSize());
}

void Tests::test_validation() {
    assert(is_only_letters("ValidName") == true);
    assert(is_only_letters("Invalid Name") == false);
    assert(is_only_digits("1234") == true);
    assert(is_only_digits("12a4") == false);
    assert(is_valid_number("1234") == true);
    assert(is_valid_number("12.34") == false);
    assert(is_valid_age_input(25) == true);
    assert(is_valid_age_input(150) == false);
}

void Tests::test_add_remove_update() {
    Service service;

    assert(service.adminAddService("ValidBreed", "ValidName", 5, "photo1") == true);
    assert(service.adminRemoveService("photo1") == true);
}

void Tests::test_all() {
    test_service();
    test_repo();
    test_dog();
    test_dynamicArray();
    test_validation();
    test_add_remove_update();
    test_user_repo();
    std::cout << "All tests passed" << std::endl;
}
