#pragma once
#include "Bag.h"

class BagIterator
{
    // DO NOT CHANGE THIS PART
    friend class Bag;

private:
    const Bag& bag;
    int currentNode; // index in the array (points to the node we are at)
    int currentFreq; // frequency position inside the node

    // Private constructor
    BagIterator(const Bag& c);

public:
    // Sets the iterator to the first element
    void first();

    // Moves the iterator to the next element
    void next();

    // Returns the current element
    TElem getCurrent() const;

    // Checks if the iterator is valid
    bool valid() const;
};
