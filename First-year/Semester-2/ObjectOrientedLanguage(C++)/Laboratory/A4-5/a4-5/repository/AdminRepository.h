#pragma once
#include "../dynamic_vector/dynamic_vector.h"

class RepoAdmin {
private:
	DynamicArray<class Dog> dogs = DynamicArray<class Dog>();
	DynamicArray<class Dog> adoptedDogs = DynamicArray<class Dog>();

public:
	RepoAdmin();

	~RepoAdmin();

	DynamicArray<class Dog>& getRepoDogs();

	bool addRepoDog(class Dog& dog);

	bool removeRepoDog(const string& photograph);

	bool updateRepoDog(class Dog& dog, const string& name, const string& breed, int age);
};