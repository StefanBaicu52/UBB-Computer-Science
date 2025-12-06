#pragma once
#include "SortedMap.h"
#include <vector>

class SMIterator {
	friend class SortedMap;

private:
	const SortedMap& map;
	std::vector<TElem> elements;
	int currentIndex;

	SMIterator(const SortedMap& mapionar);

	void sortElements();

public:
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;
};
