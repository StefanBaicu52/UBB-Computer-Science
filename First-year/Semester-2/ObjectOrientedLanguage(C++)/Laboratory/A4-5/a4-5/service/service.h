#ifndef SERVICE_H
#define SERVICE_H
#pragma once


#include "../repository/AdminRepository.h"
#include "../repository/UserRepository.h"

class Service {
private:
	RepoAdmin repoAdmin;
	RepoUser repoUser;

public:
	Service() {}
	~Service() {}

	// Admin
	DynamicArray<class Dog>& getServiceDogs();
	bool photoIsUnique(const string& photo);
	bool adminAddService(const string& name, const string& breed, int age, const string& photograph);
	bool adminRemoveService(const string& photograph);
	bool adminUpdateService(const string& photograph, const string& name, const string& breed, int age);
	bool isAdopted(const string& photograph);

	// User
	bool userAdoptService(const string& photograph);
	DynamicArray<Dog>& getUserAdoptionList();
	DynamicArray<Dog> getDogsByBreedAndAge(const std::string& breed, int maxAge);
	void addDog(Dog& dog);

	void adoptDog(const Dog& d);


};
#endif