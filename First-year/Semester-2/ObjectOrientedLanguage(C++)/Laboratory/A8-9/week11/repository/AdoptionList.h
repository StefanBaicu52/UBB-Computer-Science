#pragma once
#include <vector>
#include <string>
#include "../domain/dog.h"

//interfata de baza
class AdoptionList {
public:
    virtual void addDog(const Dog& dog) = 0;
    virtual void saveToFile() = 0;
    virtual void openFile() = 0;
    virtual std::vector<Dog>& getDogs() = 0;
    virtual ~AdoptionList() = default;
};

//declar CSVOutput
class CSVOutput : public AdoptionList {
private:
    std::vector<Dog> adopted;
public:
    void addDog(const Dog& dog) override;
    void saveToFile() override;
    void openFile() override;
    std::vector<Dog>& getDogs() override;
};

//declar HTMLOutput
class HTMLOutput : public AdoptionList {
private:
    std::vector<Dog> adopted;
public:
    void addDog(const Dog& dog) override;
    void saveToFile() override;
    void openFile() override;
    std::vector<Dog>& getDogs() override;
};
