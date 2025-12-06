#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m) {
	stackTop = -1;
	first();
}

void SMIterator::first() {
	stackTop = -1;
	pushLeft(map.root);  // Push the left-most path from root
}

void SMIterator::next() {
	if (!valid())
		throw exception();

	int node = stack[stackTop--];  // Pop current node from stack
	pushLeft(map.nodes[node].right);  // Push left path from right child
}

bool SMIterator::valid() const {
	return stackTop >= 0;
}

TElem SMIterator::getCurrent() const {
	if (!valid())
		throw exception();
	int node = stack[stackTop];
	return { map.nodes[node].key, map.nodes[node].value };
}

// Helper to push left path of a subtree
void SMIterator::pushLeft(int nodeIndex) {
	while (nodeIndex != -1) {
		stack[++stackTop] = nodeIndex;
		nodeIndex = map.nodes[nodeIndex].left;
	}
}
