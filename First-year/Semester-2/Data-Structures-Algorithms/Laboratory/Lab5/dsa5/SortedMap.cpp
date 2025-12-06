#include "SortedMap.h"
#include "SMIterator.h"
#include <exception>
using namespace std;

//teta 1
SortedMap::SortedMap(Relation r) : rel(r) {
    capacity = 100;
    nodes = new Node[capacity];
    root = -1;
    firstEmpty = 0;
    sizeMap = 0;

    for (int i = 0; i < capacity - 1; i++) {
        nodes[i].left = i + 1;
    }
    nodes[capacity - 1].left = -1;
}

//teta 1/ teta n o n
int SortedMap::allocateNode() {
    if (firstEmpty == -1) {
        resize();
    }
    int newNode = firstEmpty;
    firstEmpty = nodes[firstEmpty].left;
    return newNode;
}

void SortedMap::freeNode(int index) {
    nodes[index].left = firstEmpty;
    firstEmpty = index;
}

// teta n
void SortedMap::resize() {
    int newCapacity = capacity * 2;
    Node* newNodes = new Node[newCapacity];

    for (int i = 0; i < capacity; i++) {
        newNodes[i] = nodes[i];
    }
    for (int i = capacity; i < newCapacity - 1; i++) {
        newNodes[i].left = i + 1;
    }
    newNodes[newCapacity - 1].left = -1;
    firstEmpty = capacity;

    delete[] nodes;
    nodes = newNodes;
    capacity = newCapacity;
}
//o 1/ teta n/ teta n
TValue SortedMap::add(TKey k, TValue v) {
    if (root == -1) {
        int newNode = allocateNode();
        nodes[newNode] = {k, v, -1, -1, -1};
        root = newNode;
        sizeMap++;
        return NULL_TVALUE;
    }

    int current = root;
    int parent = -1;

    while (current != -1) {
        if (nodes[current].key == k) {
            TValue old = nodes[current].value;
            nodes[current].value = v;
            return old;
        }
        parent = current;
        if (rel(k, nodes[current].key)) {
            current = nodes[current].left;
        } else {
            current = nodes[current].right;
        }
    }

    int newNode = allocateNode();
    nodes[newNode] = {k, v, -1, -1, parent};
    if (rel(k, nodes[parent].key)) {
        nodes[parent].left = newNode;
    } else {
        nodes[parent].right = newNode;
    }

    sizeMap++;
    return NULL_TVALUE;
}
//o(1)/teta n
TValue SortedMap::search(TKey k) const {
    int current = root;
    while (current != -1) {
        if (nodes[current].key == k) return nodes[current].value;
        if (rel(k, nodes[current].key)) {
            current = nodes[current].left;
        } else {
            current = nodes[current].right;
        }
    }
    return NULL_TVALUE;
}

//o(1)/teta n
TValue SortedMap::remove(TKey k) {
    int current = root;
    int parent = -1;
    while (current != -1 && nodes[current].key != k) {
        parent = current;
        if (rel(k, nodes[current].key)) {
            current = nodes[current].left;
        } else {
            current = nodes[current].right;
        }
    }
    if (current == -1) return NULL_TVALUE;

    TValue removedValue = nodes[current].value;

    // Node with 2 children
    if (nodes[current].left != -1 && nodes[current].right != -1) {
        int successor = nodes[current].right;
        while (nodes[successor].left != -1) {
            successor = nodes[successor].left;
        }
        nodes[current].key = nodes[successor].key;
        nodes[current].value = nodes[successor].value;
        k = nodes[successor].key;
        parent = current;
        current = successor;
    }

    // Node with 0 or 1 child
    int child = (nodes[current].left != -1) ? nodes[current].left : nodes[current].right;

    if (parent == -1) {
        root = child;
        if (child != -1) nodes[child].parent = -1;
    } else if (nodes[parent].left == current) {
        nodes[parent].left = child;
    } else {
        nodes[parent].right = child;
    }

    if (child != -1) nodes[child].parent = parent;

    freeNode(current);
    sizeMap--;

    return removedValue;
}

// teta 1
int SortedMap::size() const {
    return sizeMap;
}


// teta 1
bool SortedMap::isEmpty() const {
    return sizeMap == 0;
}

SMIterator SortedMap::iterator() const {
    return SMIterator(*this);
}

SortedMap::~SortedMap() {
    delete[] nodes;
}


//teta(1)/teta n
int SortedMap::getValueRange() const {
    if (this->isEmpty()) {
        return -1;
    }

    SMIterator it = this->iterator();
    it.first();

    int minVal = it.getCurrent().second;
    int maxVal = it.getCurrent().second;

    while (it.valid()) {
        int val = it.getCurrent().second;
        if (val < minVal) minVal = val;
        if (val > maxVal) maxVal = val;
        it.next();
    }

    return maxVal - minVal;
}


