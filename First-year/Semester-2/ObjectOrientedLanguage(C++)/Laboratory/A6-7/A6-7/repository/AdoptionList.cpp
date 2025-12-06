#include "AdoptionList.h"
#include "../exceptions/exceptions.h"
#include <fstream>
#include <iostream>
#include <cstdlib>

#ifdef _WIN32
    #define OPEN_COMMAND "start "
#elif __APPLE__
    #define OPEN_COMMAND "open "
#elif __linux__
    #define OPEN_COMMAND "xdg-open "
#else
    #define OPEN_COMMAND ""
#endif

// ---------------------------- CSVOutput

void CSVOutput::addDog(const Dog& dog) {
    adopted.push_back(dog);
    saveToFile();
}

void CSVOutput::saveToFile() {
    std::ofstream file("adoptions.csv");
    if (!file.is_open()) {
        throw RepoException("CSV file could not be opened!");
    }

    file << "Name,Breed,Age,Photograph\n";
    for (const Dog& d : adopted) {
        if (d.get_adopted()) {
            file << d.get_name() << ","
                 << d.get_breed() << ","
                 << d.get_age() << ","
                 << d.get_photograph() << "\n";
        }
    }
    file.close();
}

void CSVOutput::openFile() {
    std::string command = std::string(OPEN_COMMAND) + "adoptions.csv";
    system(command.c_str());
}

std::vector<Dog>& CSVOutput::getDogs() {
    return adopted;
}

// ---------------------------- HTMLOutput

void HTMLOutput::addDog(const Dog& dog) {
    adopted.push_back(dog);
    saveToFile();
}

void HTMLOutput::saveToFile() {
    std::ofstream file("adoptions.html");
    if (!file.is_open()) {
        throw RepoException("HTML file could not be opened!");
    }

    file << "<!DOCTYPE html><html><head><title>Adoption List</title></head><body>";
    file << "<table border=\"1\"><tr><th>Name</th><th>Breed</th><th>Age</th><th>Photograph</th></tr>";

    for (const Dog& d : adopted) {
        file << "<tr><td>" << d.get_name() << "</td><td>" << d.get_breed() << "</td><td>" << d.get_age()
             << "</td><td><a href='https://kcaaap.com/dogs-photos/" << d.get_photograph() << "'>Link</a></td></tr>";
    }

    file << "</table></body></html>";
    file.close();
}

void HTMLOutput::openFile() {
    std::string command = std::string(OPEN_COMMAND) + "adoptions.html";
    system(command.c_str());
}

std::vector<Dog>& HTMLOutput::getDogs() {
    return adopted;
}
