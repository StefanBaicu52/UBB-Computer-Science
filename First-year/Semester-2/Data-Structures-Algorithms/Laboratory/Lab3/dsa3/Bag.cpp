#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;
Bag::Bag() {
    capacity = 10;
    nodes = new Node[capacity];
    for (int i = 0; i < capacity - 1; i++) {
        nodes[i].next = i + 1;
    }
    nodes[capacity - 1].next = -1; // end of free list
    head = -1;
    tail = -1;
    firstEmpty = 0;
    sizeOfBag = 0;
}

//teta n toate
void Bag::resize() {
    int newCapacity = capacity * 2;
    Node* newNodes = new Node[newCapacity];

    for (int i = 0; i < capacity; i++) {
        newNodes[i] = nodes[i];
    }
    for (int i = capacity; i < newCapacity - 1; i++) {
        newNodes[i].next = i + 1;
    }
    newNodes[newCapacity - 1].next = -1;

    delete[] nodes;
    nodes = newNodes;
    firstEmpty = capacity;
    capacity = newCapacity;
}

// best teta 1 worst teta n se face resize total 0(n)
int Bag::allocate() {
    if (firstEmpty == -1)
        resize();
    int newPos = firstEmpty;
    firstEmpty = nodes[firstEmpty].next;
    return newPos;
}

//teta 1 toate
void Bag::deallocate(int index) {
    nodes[index].next = firstEmpty;
    firstEmpty = index;
}

// teta 1 best worst teta n total o(n)
void Bag::add(TElem elem) {
    int current = head;
    while (current != -1) {
        if (nodes[current].element == elem) {
            nodes[current].frequency++;
            sizeOfBag++;
            return;
        }
        current = nodes[current].next;
    }

    int newNode = allocate();
    nodes[newNode].element = elem;
    nodes[newNode].frequency = 1;
    nodes[newNode].prev = tail;
    nodes[newNode].next = -1;

    if (tail != -1) {
        nodes[tail].next = newNode;
    } else {
        head = newNode;
    }
    tail = newNode;
    sizeOfBag++;
}

// teta 1 best worst teta n total o(n)
bool Bag::remove(TElem elem) {
    int current = head;
    while (current != -1) {
        if (nodes[current].element == elem) {
            nodes[current].frequency--;
            sizeOfBag--;

            if (nodes[current].frequency == 0) {
                if (nodes[current].prev != -1)
                    nodes[nodes[current].prev].next = nodes[current].next;
                else
                    head = nodes[current].next;

                if (nodes[current].next != -1)
                    nodes[nodes[current].next].prev = nodes[current].prev;
                else
                    tail = nodes[current].prev;

                deallocate(current);
            }
            return true;
        }
        current = nodes[current].next;
    }
    return false;
}

// teta 1 best worst teta n total o(n)
bool Bag::search(TElem elem) const {
    int current = head;
    while (current != -1) {
        if (nodes[current].element == elem) {
            return true;
        }
        current = nodes[current].next;
    }
    return false;
}

// teta 1 best worst teta n total o(n)
int Bag::nrOccurrences(TElem elem) const {
    int current = head;
    while (current != -1) {
        if (nodes[current].element == elem) {
            return nodes[current].frequency;
        }
        current = nodes[current].next;
    }
    return 0;
}

//teta 1
int Bag::size() const {
    return sizeOfBag;
}

//teta 1
bool Bag::isEmpty() const {
    return sizeOfBag == 0;
}

//teta 1
BagIterator Bag::iterator() const {
    return BagIterator(*this);
}

//best case teta 1 worst teta n total o(n)
TElem Bag::mostFrequent() const {
    if (isEmpty())
        return NULL_TELEM;

    int current = head;
    int maxFreq = -1;
    TElem mostFreqElem = NULL_TELEM;

    while (current != -1) {
        if (nodes[current].frequency > maxFreq) {
            maxFreq = nodes[current].frequency;
            mostFreqElem = nodes[current].element;
        }
        current = nodes[current].next;
    }

    return mostFreqElem;
}


// teta 1
Bag::~Bag() {
    delete[] nodes;
}

