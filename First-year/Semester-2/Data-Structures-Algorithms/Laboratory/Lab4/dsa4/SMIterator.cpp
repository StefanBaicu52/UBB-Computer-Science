#include "SMIterator.h"
#include <algorithm>
#include <exception>
using namespace std;
//best worst total nlogn
SMIterator::SMIterator(const SortedMap& m) : map(m) {
	currentIndex = 0;

	for (int i = 0; i < map.capacity; i++) {
		SortedMap::Node* node = map.table[i];
		while (node != nullptr) {
			elements.push_back(node->elem);
			node = node->next;
		}
	}


	sortElements();
}

//best worst total nlogn
void SMIterator::sortElements() {
	std::sort(elements.begin(), elements.end(),
		[this](const TElem& a, const TElem& b) {
			return map.rel(a.first, b.first);
		});
}

//teta 1
void SMIterator::first() {
	currentIndex = 0;
}

// teta 1
void SMIterator::next() {
	if (!valid())
		throw exception();
	currentIndex++;
}


// teta 1
bool SMIterator::valid() const {
	return currentIndex < (int)elements.size();
}

// teta 1
TElem SMIterator::getCurrent() const {
	if (!valid())
		throw exception();
	return elements[currentIndex];
}


