#pragma once
//DO NOT INCLUDE BAGITERATOR

//DO NOT CHANGE THIS PART
#define NULL_TELEM -111111
typedef int TElem;
class BagIterator;

class Bag {

private:
	// Representation
	struct Node {
		TElem element;
		int frequency;
		int next;
		int prev;
	};

	Node* nodes;       // array of nodes
	int head;          // index of first node
	int tail;          // index of last node
	int firstEmpty;    // index of first free position
	int capacity;      // capacity of array
	int sizeOfBag;     // total number of elements (counting duplicates)

	void resize();         // doubles array size
	int allocate();        // allocates a free position
	void deallocate(int i); // deallocates a position

	//DO NOT CHANGE THIS PART
	friend class BagIterator;

public:
	// constructor
	Bag();

	// adds an element to the bag
	void add(TElem e);

	// removes one occurrence of an element from the bag
	// returns true if an element was removed, false otherwise (if e was not part of the bag)
	bool remove(TElem e);

	// checks if an element appears in the bag
	bool search(TElem e) const;

	// returns the number of occurrences for an element in the bag
	int nrOccurrences(TElem e) const;

	// returns the number of elements from the bag
	int size() const;

	// returns an iterator for this bag
	BagIterator iterator() const;

	// checks if the bag is empty
	bool isEmpty() const;

	// most frequent element
	TElem mostFrequent() const;

	// destructor
	~Bag();
};
