#include "SMIterator.h"
#include <exception>

using namespace std;
// teta 1
SMIterator::SMIterator(SortedMap& m) : map(m) {
    current = map.head;
}
// teta 1
void SMIterator::first() {
    current = map.head;
}
// teta 1
void SMIterator::next() {
    if (!valid())
        throw exception();
    current = current->next;
}
// teta 1
bool SMIterator::valid() const {
    return current != nullptr;
}
// teta 1
TElem SMIterator::getCurrent() const {
    if (!valid())
        throw exception();
    return current->info;
}
// teta 1
TElem SMIterator::remove() {
    if (!valid())
        throw exception();

    SortedMap::DLLNode* nodeToRemove = current;
    TElem removedElem = nodeToRemove->info;

    current = current->next;

    if (nodeToRemove->prev != nullptr)
        nodeToRemove->prev->next = nodeToRemove->next;
    else
        map.head = nodeToRemove->next;

    if (nodeToRemove->next != nullptr)
        nodeToRemove->next->prev = nodeToRemove->prev;
    else
        map.tail = nodeToRemove->prev;

    delete nodeToRemove;
    map.length--;

    return removedElem;
}
