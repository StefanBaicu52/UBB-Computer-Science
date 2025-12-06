#include "SortedMap.h"
#include "SMIterator.h"
#include <exception>
#include <iostream>
using namespace std;

//teta 1
SortedMap::SortedMap(Relation r) {
    this->capacity = 13;
    this->table = new Node * [capacity]();
    this->length = 0;
    this->rel = r;
    this->loadFactor = 0.7f; //resize when more than 70 of the buckets are filled
}

//teta 1
int SortedMap::hash(TKey key) const {
    return abs(key) % capacity;
}


//teta n
void SortedMap::resize() {
    int oldCapacity = capacity;
    capacity *= 2;
    Node** oldTable = table;
    table = new Node * [capacity]();
    length = 0;

    for (int i = 0; i < oldCapacity; i++) {
        Node* current = oldTable[i];
        while (current != nullptr) {
            add(current->elem.first, current->elem.second);
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
    delete[] oldTable;
}


//best teta 1 worst teta n total teta n
TValue SortedMap::add(TKey k, TValue v) {
    if ((float)length / capacity > loadFactor)
        resize();

    int index = hash(k);
    Node* current = table[index];

    while (current != nullptr) {
        if (current->elem.first == k) {
            TValue oldValue = current->elem.second;
            current->elem.second = v;
            return oldValue;
        }
        current = current->next;
    }

    table[index] = new Node({ k, v }, table[index]);
    length++;
    return NULL_TVALUE;
}

//best teta 1 worst teta n total teta n
TValue SortedMap::search(TKey k) const {
    int index = hash(k);
    Node* current = table[index];
    while (current != nullptr) {
        if (current->elem.first == k)
            return current->elem.second;
        current = current->next;
    }
    return NULL_TVALUE;
}

//best teta 1 worst teta n total teta n
TValue SortedMap::remove(TKey k) {
    int index = hash(k);
    Node* current = table[index];
    Node* prev = nullptr;

    while (current != nullptr) {
        if (current->elem.first == k) {
            TValue val = current->elem.second;
            if (prev == nullptr)
                table[index] = current->next;
            else
                prev->next = current->next;

            delete current;
            length--;
            return val;
        }
        prev = current;
        current = current->next;
    }
    return NULL_TVALUE;
}

// teta 1
int SortedMap::size() const {
    return length;
}

// teta 1
bool SortedMap::isEmpty() const {
    return length == 0;
}

SMIterator SortedMap::iterator() const {
    return SMIterator(*this);
}

// best teta m worst teta n total teta n
SortedMap::~SortedMap() {
    for (int i = 0; i < capacity; i++) {
        Node* current = table[i];
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
    delete[] table;
}

//best teta1 worst teta n total teta n
void SortedMap::filter(Condition cond) {
    for (int i = 0; i < capacity; i++) {
        Node* current = table[i];
        Node* prev = nullptr;

        while (current != nullptr) {
            if (!cond(current->elem.second)) {
                // Remove current node
                if (prev == nullptr) {
                    table[i] = current->next;
                    delete current;
                    current = table[i]; // move to new head
                } else {
                    prev->next = current->next;
                    delete current;
                    current = prev->next; // move forward
                }
                length--;
            } else {
                prev = current;
                current = current->next;
            }
        }
    }
}

