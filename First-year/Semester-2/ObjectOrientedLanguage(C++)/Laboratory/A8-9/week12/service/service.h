#ifndef SERVICE_H
#define SERVICE_H
#pragma once
#include <stack>
#include "../undo-redo/undo.h"
#include <vector>
#include "../repository/AdminRepository.h"
#include "../repository/AdoptionList.h"
#include <memory>


class Service {
private:
	RepoAdmin repoAdmin;
	AdoptionList* adoptionlist;
	std::vector<std::unique_ptr<UndoAction>> undoStack;
	std::vector<std::unique_ptr<UndoAction>> redoStack;

public:
	AdoptionList* getRawAdoptionList();


	Service(AdoptionList* list) : adoptionlist(list) {}
	void addDogNoUndo(Dog d);
	void removeDogNoUndo(std::string photo);
	void updateDogNoUndo(Dog d);


	~Service() {
		delete adoptionlist;
	}

	// Admin
	std::vector<Dog>& getServiceDogs();
	bool photoIsUnique(const std::string& photo);
	bool adminAddService(const std::string& name, const std::string& breed, int age, const std::string& photograph);
	bool adminRemoveService(const std::string& photograph);
	bool adminUpdateService(const std::string& photograph, const std::string& name, const std::string& breed, int age);
	bool isAdopted(const std::string& photograph);
	void reloadFromFile();

	// User
	bool userAdoptService(const std::string& photograph);
	std::vector<Dog>& getUserAdoptionList();
	std::vector<Dog> getDogsByBreedAndAge(const std::string& breed, int maxAge);
	void addDog(Dog& dog);
	void adoptDog(const Dog& d);
	void openAdoptionFile();

	//Setter care elibereaza memoria veche
	void setAdoptionList(AdoptionList* list) {
		if (adoptionlist)
			delete adoptionlist;
		adoptionlist = list;
	}


	void undo();
	void redo();



};




#endif
