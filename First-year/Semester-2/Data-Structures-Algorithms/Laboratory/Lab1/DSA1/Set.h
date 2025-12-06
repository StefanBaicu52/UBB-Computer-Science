#pragma once
// DO NOT INCLUDE SETITERATOR

// DO NOT CHANGE THIS PART
#define NULL_TELEM -111111
typedef int TElem;
class SetIterator;

class Set {
    // DO NOT CHANGE THIS PART
    friend class SetIterator;

private:
    //  Internal Representation
    bool* elements;  // dynamic array representing presence of elements
    int minElem;     // minimum element stored
    int maxElem;     // maximum element stored
    int capacity;    // size of the dynamic array
    int length;      // number of elements in the set

public:
    // implicit constructor
    Set();

    // adds an element to the set
    // returns true if the element was added, false otherwise
    bool add(TElem e);

    // removes an element from the set
    // returns true if e was removed, false otherwise
    bool remove(TElem e);

    // checks whether an element belongs to the set or not
    bool search(TElem elem) const;

    // returns the number of elements
    int size() const;

    // check whether the set is empty or not
    bool isEmpty() const;

    // return an iterator for the set
    SetIterator iterator() const;

    // destructor
    ~Set();
};
