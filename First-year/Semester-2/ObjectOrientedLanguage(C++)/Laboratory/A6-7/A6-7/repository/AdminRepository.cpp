#include "AdminRepository.h"
#include "../domain/dog.h"
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

RepoAdmin::RepoAdmin() {
    load_from_file();  //load dogs from file at start
}

RepoAdmin::~RepoAdmin() {
    save_to_file();  //save all doogs to file at end
}

void RepoAdmin::load_from_file() {
    ifstream in(filename);
    if (!in.is_open())  //verfiic daca fisierul se deschide corect
        return;

    Dog dog;
    while (in >> dog) {//citesc cate un caine pe rand din fisier
        dogs.push_back(dog);//adaug cainele in lista
    }

    in.close();
}

void RepoAdmin::save_to_file() {
    ofstream out(filename);
    if (!out.is_open())
        return;

    for (const Dog& dog : dogs)
        out << dog;

    out.close();
}

vector<Dog>& RepoAdmin::getRepoDogs() {
    return this->dogs;
}

bool RepoAdmin::addRepoDog(Dog& dog) {
    this->dogs.push_back(dog);
    save_to_file();
    return true;
}

bool RepoAdmin::removeRepoDog(const string& photograph) {
    auto it = find_if(dogs.begin(), dogs.end(),
                           [&](const Dog& d) { return d.get_photograph() == photograph; });

    if (it != dogs.end()) {//daca s a gasit cainele
        dogs.erase(it);//il sterg din lista
        save_to_file();//salvez lista actualizata
        return true;
    }

    return false;
}

bool RepoAdmin::updateRepoDog(Dog& dog, const string& name, const string& breed, int age) {
    dog.set_name(name);//actualiazari
    dog.set_breed(breed);
    dog.set_age(age);
    save_to_file();
    return true;
}
