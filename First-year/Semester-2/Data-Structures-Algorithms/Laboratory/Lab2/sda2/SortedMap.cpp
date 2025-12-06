#include "SortedMap.h"
#include "SMIterator.h"
#include <exception>
using namespace std;
//teta 1
SortedMap::SortedMap(Relation r) {
    this->rel = r;
    this->head = nullptr;
    this->tail = nullptr;
    this->length = 0;
}

//best case teta(1) worst teta n and total o(n)
TValue SortedMap::add(TKey k, TValue v) {
    DLLNode* current = head;
    DLLNode* prev = nullptr;

    while (current != nullptr && rel(current->info.first, k)) {
        if (current->info.first == k) {
            TValue oldVal = current->info.second;
            current->info.second = v;
            return oldVal;
        }
        prev = current;
        current = current->next;
    }

    if (current != nullptr && current->info.first == k) {
        TValue oldVal = current->info.second;
        current->info.second = v;
        return oldVal;
    }

    DLLNode* newNode = new DLLNode({k, v});
    if (prev == nullptr) {
        // Insert at beginning
        newNode->next = head;
        if (head != nullptr)
            head->prev = newNode;
        head = newNode;
        if (tail == nullptr)
            tail = newNode;
    } else {
        newNode->next = prev->next;
        newNode->prev = prev;
        prev->next = newNode;
        if (newNode->next != nullptr)
            newNode->next->prev = newNode;
        else
            tail = newNode;
    }

    length++;
    return NULL_TVALUE;
}
// best teta(1) worst teta n and total o(n)
TValue SortedMap::search(TKey k) const {
    DLLNode* current = head;
    while (current != nullptr) {
        if (current->info.first == k)
            return current->info.second;
        current = current->next;
    }
    return NULL_TVALUE;
}
// best teta(1) worst and total o(n)
TValue SortedMap::remove(TKey k) {
    DLLNode* current = head;

    while (current != nullptr) {
        if (current->info.first == k) {
            TValue val = current->info.second;

            if (current->prev != nullptr)
                current->prev->next = current->next;
            else
                head = current->next;

            if (current->next != nullptr)
                current->next->prev = current->prev;
            else
                tail = current->prev;

            delete current;
            length--;
            return val;
        }
        current = current->next;
    }

    return NULL_TVALUE;
}
// o(1)
int SortedMap::size() const {
    return length;
}
// o(1)
bool SortedMap::isEmpty() const {
    return length == 0;
}
// o(1)
SMIterator SortedMap::iterator() {
    return SMIterator(*this);
}
// o(lenght)
SortedMap::~SortedMap() {
    DLLNode* current = head;
    while (current != nullptr) {
        DLLNode* next = current->next;
        delete current;
        current = next;
    }
}
