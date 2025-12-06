#include "SetIterator.h"
#include "Set.h"
#include <exception>
#include <algorithm>

using namespace std;

SetIterator::SetIterator(const Set& m) : set(m) {
    first();
}
//complexity O(1) best; Θ(capacity) – if all elements are false (no elements in set) worst,total
void SetIterator::first() {
    current = 0;
    while (current < set.capacity && !set.elements[current]) {
        current++;
    }
}

//complexity O(1) best; Θ(capacity) – if all elements are false (no elements in set) worst,total
void SetIterator::next() {
    if (!valid())
        throw exception();

    current++;
    while (current < set.capacity && !set.elements[current]) {
        current++;
    }
}

//complexity O(1)
TElem SetIterator::getCurrent() {
    if (!valid())
        throw exception();
    return current + set.minElem;
}

//complexity O(1)
bool SetIterator::valid() const {
    return current < set.capacity;
}



