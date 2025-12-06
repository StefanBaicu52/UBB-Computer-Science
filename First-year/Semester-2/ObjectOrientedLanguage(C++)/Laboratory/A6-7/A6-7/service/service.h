#ifndef SERVICE_H
#define SERVICE_H
#pragma once

#include <vector>
#include "../repository/AdminRepository.h"
#include "../repository/AdoptionList.h"

class Service {
private:
	RepoAdmin repoAdmin;
	AdoptionList* adoptionlist; //inlocuim RepoUser cu AdoptionList

public:
    Service(AdoptionList* list) : adoptionlist(list) {}
	~Service() {}

	// Admin
	std::vector<Dog>& getServiceDogs();
	bool photoIsUnique(const std::string& photo);
	bool adminAddService(const std::string& name, const std::string& breed, int age, const std::string& photograph);
	bool adminRemoveService(const std::string& photograph);
	bool adminUpdateService(const std::string& photograph, const std::string& name, const std::string& breed, int age);
	bool isAdopted(const std::string& photograph);



	// User
	bool userAdoptService(const std::string& photograph);
	std::vector<Dog>& getUserAdoptionList(); // nou
	std::vector<Dog> getDogsByBreedAndAge(const std::string& breed, int maxAge);
	void addDog(Dog& dog);
	void adoptDog(const Dog& d);

	void openAdoptionFile(); //  deschidem fisierul CSV/HTML  	//pt cerinta 5

	void setAdoptionList(AdoptionList* list) { this->adoptionlist = list; }




};

#endif
