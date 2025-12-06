#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;

//teta 1
BagIterator::BagIterator(const Bag& c) : bag(c) {
	first();
}

//teta 1
void BagIterator::first() {
	currentNode = bag.head;
	currentFreq = 1;
}

// teta 1 best worst teta n daca sare peste multe noduri eliminate sau frecvente scazute total teta 1
void BagIterator::next() {
	if (!valid())
		throw exception();

	if (currentFreq < bag.nodes[currentNode].frequency) {
		currentFreq++;
	} else {
		currentNode = bag.nodes[currentNode].next;
		currentFreq = 1;
	}
}

//teta 1
bool BagIterator::valid() const {
	return currentNode != -1;
}

//teta 1
TElem BagIterator::getCurrent() const {
	if (!valid())
		throw exception();
	return bag.nodes[currentNode].element;
}
