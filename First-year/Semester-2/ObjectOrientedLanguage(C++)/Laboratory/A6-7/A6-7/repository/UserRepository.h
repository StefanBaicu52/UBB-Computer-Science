#pragma once
#include <vector>
#include <fstream>
#include "../domain/dog.h"

class RepoUser {
private:
    std::vector<Dog> adoptedDogs;
    std::string filename = "adoptions.txt";

    void load_from_file();
    void save_to_file();

public:
    RepoUser();
    ~RepoUser();

    void addAdoptedDog(const Dog& dog);
    std::vector<Dog>& getAdoptedDogs();
};
