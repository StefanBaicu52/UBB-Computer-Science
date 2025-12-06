#pragma once

typedef int TKey;
typedef int TValue;
#include <utility>
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TPAIR std::pair<TKey, TValue>(-111111, -111111)

class SMIterator;
typedef bool(*Relation)(TKey, TKey);

class SortedMap {
	friend class SMIterator;

private:
	struct DLLNode {
		TElem info;
		DLLNode* prev;
		DLLNode* next;
		DLLNode(TElem elem, DLLNode* p = nullptr, DLLNode* n = nullptr)
			: info(elem), prev(p), next(n) {}
	};

	DLLNode* head;
	DLLNode* tail;
	int length;
	Relation rel;

public:
	// Constructor
	SortedMap(Relation r);

	// Add or update (key, value) pair
	TValue add(TKey c, TValue v);

	// Search for key
	TValue search(TKey c) const;

	// Remove by key
	TValue remove(TKey c);

	// Size of the map
	int size() const;

	// Check if empty
	bool isEmpty() const;

	// Return a modifiable iterator
	SMIterator iterator();

	// Destructor
	~SortedMap();
};
