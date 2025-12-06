#include "UserRepository.h"
#include <fstream>
#include <sstream>

RepoUser::RepoUser() {
    load_from_file();
}

RepoUser::~RepoUser() {
    save_to_file();
}

void RepoUser::load_from_file() {
    std::ifstream in(filename);
    if (!in.is_open()) return;

    Dog dog;
    while (in >> dog) {
        adoptedDogs.push_back(dog);
    }

    in.close();
}

void RepoUser::save_to_file() {
    std::ofstream out(filename);
    if (!out.is_open()) return;

    for (const Dog& dog : adoptedDogs)
        out << dog;

    out.close();
}

void RepoUser::addAdoptedDog(const Dog& dog) {
    adoptedDogs.push_back(dog);
    save_to_file();
}

std::vector<Dog>& RepoUser::getAdoptedDogs() {
    return adoptedDogs;
}
