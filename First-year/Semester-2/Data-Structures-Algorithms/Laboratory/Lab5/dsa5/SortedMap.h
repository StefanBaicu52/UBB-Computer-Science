#pragma once
typedef int TKey;
typedef int TValue;
#include <utility>
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TPAIR std::pair<TKey, TValue>(-111111, -111111)

typedef bool(*Relation)(TKey, TKey);

class SMIterator;

class SortedMap {
	friend class SMIterator;

private:
	struct Node {
		TKey key;
		TValue value;
		int left, right, parent;
	};

	Node* nodes;
	int root;
	int capacity;
	int firstEmpty;
	int sizeMap;
	Relation rel;

	int allocateNode();
	void freeNode(int index);
	void resize();

public:
	SortedMap(Relation r);
	TValue add(TKey c, TValue v);
	TValue search(TKey c) const;
	TValue remove(TKey c);
	int size() const;
	bool isEmpty() const;
	SMIterator iterator() const;
	~SortedMap();
	int getValueRange() const;
};
