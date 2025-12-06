#pragma once

#include <vector>

#include "../domain/dog.h"
#include <fstream>
#include <iostream>
using namespace std;

class RepoAdmin {
private:
	vector<Dog> dogs;
	string filename = "dogs.txt";  // text file with repository data

	void load_from_file();
	void save_to_file();

public:
	RepoAdmin();
	~RepoAdmin();

	vector<Dog>& getRepoDogs();
	bool addRepoDog(Dog& dog);
	bool removeRepoDog(const string& photograph);
	bool updateRepoDog(Dog& dog, const string& name, const string& breed, int age);
};
