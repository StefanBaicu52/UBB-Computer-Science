#include "AdoptionList.h"
#include "../exceptions/exceptions.h"
#include <fstream>
#include <iostream>
// ----------------------------             CSV
void CSVOutput::addDog(const Dog& dog) {
    adopted.push_back(dog);
    saveToFile();
}

void CSVOutput::saveToFile() {
    std::ofstream file("adoptions.csv");
    if (!file.is_open()) {
        throw RepoException("CSV file could not be opened!");
    }

    //Scriu capul tabelului
    file << "Name,Breed,Age,Photograph\n";

    // Salvam doar cainii adoptati
    for (const Dog& d : adopted) {
        // Verifica dacă cainele nu este deja adoptat
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
    system("open adoptions.csv");
}

std::vector<Dog>& CSVOutput::getDogs() {
    return adopted;
}


// ----------------------------             HTML

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
    system("open adoptions.html");
}

std::vector<Dog>& HTMLOutput::getDogs() {
    return adopted;
}

