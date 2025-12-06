#pragma once
#include "SortedMap.h"

class SMIterator {
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);

	// Stack for in-order traversal
	int stack[1000];  // Adjust size as needed
	int stackTop;

	// Helper to push left subtree
	void pushLeft(int nodeIndex);

public:
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;
};

