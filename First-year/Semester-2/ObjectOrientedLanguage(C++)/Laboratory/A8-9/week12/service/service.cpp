#include "service.h"
#include <algorithm>
#include <QDebug>
#include "../undo-redo/undo.h"

void Service::addDog(Dog& dog) {
    this->repoAdmin.addRepoDog(dog);
}

void Service::reloadFromFile() {
    repoAdmin.load_from_file();
}

void Service::adoptDog(const Dog& d) {
    this->adoptionlist->addDog(d);
}

std::vector<Dog>& Service::getServiceDogs() {
    return this->repoAdmin.getRepoDogs();
}

bool Service::photoIsUnique(const std::string& photo) {
    const auto& dogs = repoAdmin.getRepoDogs();
    return std::none_of(dogs.begin(), dogs.end(),
                        [&](const Dog& d) { return d.get_photograph() == photo; });
}

// Add Dog + UndoAdd
bool Service::adminAddService(const std::string& name, const std::string& breed, int age, const std::string& photograph) {
    Dog dog(name, breed, age, photograph);
    bool success = this->repoAdmin.addRepoDog(dog);
    if (success) {
        undoStack.push_back(std::make_unique<UndoAdd>(*this, dog));
        redoStack.clear();
        repoAdmin.save_to_file();
    }
    return success;
}

// Remove Dog + UndoRemove
bool Service::adminRemoveService(const std::string& photograph) {
    auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](const Dog& d) { return d.get_photograph() == photograph; });

    if (it != dogs.end()) {
        Dog removedDog = *it;
        bool success = repoAdmin.removeRepoDog(photograph);
        if (success) {
            undoStack.push_back(std::make_unique<UndoRemove>(*this, removedDog));
            redoStack.clear();
            repoAdmin.save_to_file();
        }
        return success;
    }
    return false;
}

// Update Dog + UndoUpdate
bool Service::adminUpdateService(const std::string& photograph, const std::string& name, const std::string& breed, int age) {
    auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](const Dog& d) { return d.get_photograph() == photograph; });

    if (it != dogs.end()) {
        Dog oldDog = *it;
        Dog newDog(name, breed, age, photograph);

        bool success = repoAdmin.updateRepoDog(*it, name, breed, age);
        if (success) {
            undoStack.push_back(std::make_unique<UndoUpdate>(*this, oldDog, newDog));
            redoStack.clear();
            repoAdmin.save_to_file();
        }
        return success;
    }
    return false;
}

bool Service::isAdopted(const std::string& photograph) {
    const auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](const Dog& d) { return d.get_photograph() == photograph; });
    return it != dogs.end() ? it->get_adopted() : false;
}

bool Service::userAdoptService(const std::string& photograph) {
    auto& dogs = repoAdmin.getRepoDogs();
    auto it = std::find_if(dogs.begin(), dogs.end(),
                           [&](Dog& d) {
                               return d.get_photograph() == photograph && !d.get_adopted();
                           });

    if (it != dogs.end()) {
        it->set_adopted(true);
        this->adoptionlist->addDog(*it);
        return true;
    }
    return false;
}

std::vector<Dog>& Service::getUserAdoptionList() {
    return this->adoptionlist->getDogs();
}

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

void Service::openAdoptionFile() {
    this->adoptionlist->openFile();
}

// UNDO
void Service::undo() {
    if (undoStack.empty())
        throw std::runtime_error("No more undos!");

    qDebug() << "[UNDO] Stack size before: " << undoStack.size();

    auto action = std::move(undoStack.back());
    undoStack.pop_back();
    action->doUndo();
    redoStack.push_back(std::move(action));

    qDebug() << "[UNDO] Stack size after: " << undoStack.size();
    repoAdmin.save_to_file();
}

// REDO
void Service::redo() {
    if (redoStack.empty())
        throw std::runtime_error("No more redos!");

    qDebug() << "[REDO] Stack size before: " << redoStack.size();

    auto action = std::move(redoStack.back());
    redoStack.pop_back();
    action->doRedo();
    undoStack.push_back(std::move(action));

    qDebug() << "[REDO] Stack size after: " << redoStack.size();
    repoAdmin.save_to_file();
}

void Service::addDogNoUndo(Dog d) {
    this->repoAdmin.addRepoDog(d);
}

void Service::removeDogNoUndo(std::string photo) {
    this->repoAdmin.removeRepoDog(photo);
}

void Service::updateDogNoUndo(Dog d) {
    this->repoAdmin.updateRepoDog(d, d.get_name(), d.get_breed(), d.get_age());
}
AdoptionList* Service::getRawAdoptionList() {
    return this->adoptionlist;
}
