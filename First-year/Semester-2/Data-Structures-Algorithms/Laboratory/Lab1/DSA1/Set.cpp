#include "Set.h"
#include "SetIterator.h"
#include <iostream>
#include <exception>
using namespace std;

Set::Set() {
    this->elements = nullptr;
    this->minElem = 0;
    this->maxElem = -1;  // invalid range
    this->capacity = 0;
    this->length = 0;
}

// O(capacity) worst case, O(1) best case
bool Set::add(TElem elem) {
    if (capacity == 0) {
        // First element
        capacity = 1;
        elements = new bool[1];
        elements[0] = true;
        minElem = elem;
        maxElem = elem;
        length = 1;
        return true;
    }

    if (elem < minElem || elem > maxElem) {
        // Resize array to fit new range
        int newMin = std::min(minElem, elem);
        int newMax = std::max(maxElem, elem);
        int newCapacity = newMax - newMin + 1;
        bool* newElements = new bool[newCapacity]{false};

        for (int i = minElem; i <= maxElem; ++i) {
            newElements[i - newMin] = elements[i - minElem];
        }

        delete[] elements;
        elements = newElements;
        capacity = newCapacity;
        minElem = newMin;
        maxElem = newMax;
    }

    int index = elem - minElem;
    if (elements[index])
        return false; // already in set

    elements[index] = true;
    length++;
    return true;
}

// O(1)
bool Set::remove(TElem elem) {
    if (elem < minElem || elem > maxElem)
        return false;

    int index = elem - minElem;
    if (!elements[index])
        return false;

    elements[index] = false;
    length--;

    // NOTE: we do not shrink the array to avoid complexity
    return true;
}


// O(1)
bool Set::search(TElem elem) const {
    if (elem < minElem || elem > maxElem)
        return false;
    return elements[elem - minElem];
}


// O(1)
int Set::size() const {
    return length;
}

// O(1)
bool Set::isEmpty() const {
    return length == 0;
}

// O(1)
Set::~Set() {
    delete[] elements;

}

// O(1) best case; O(capacity) worst case
SetIterator Set::iterator() const {
    return SetIterator(*this);
}


