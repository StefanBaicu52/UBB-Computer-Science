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
	struct Node {
		TElem elem;
		Node* next;
		Node(TElem e, Node* n = nullptr) : elem(e), next(n) {}
	};

	Node** table;
	int capacity;
	int length;
	Relation rel;
	float loadFactor;
	void resize();

	int hash(TKey key) const;
	typedef bool (*Condition)(TValue);


public:
	SortedMap(Relation r);
	TValue add(TKey c, TValue v);
	TValue search(TKey c) const;
	TValue remove(TKey c);
	int size() const;
	bool isEmpty() const;
	SMIterator iterator() const;
	~SortedMap();
	void filter(Condition cond);

};
