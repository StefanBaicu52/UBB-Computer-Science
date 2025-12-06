#include "ShortTest.h"
#include <assert.h>
#include "Bag.h"
#include "BagIterator.h"


void testAll() { 
	Bag b;
	assert(b.isEmpty() == true);
	assert(b.size() == 0); 
	b.add(5);
	b.add(1);
	b.add(10);
	b.add(7);
	b.add(1);
	b.add(11);
	b.add(-3);
	assert(b.size() == 7);
	assert(b.search(10) == true);
	assert(b.search(16) == false);
	assert(b.nrOccurrences(1) == 2);
	assert(b.nrOccurrences(7) == 1);
	assert(b.remove(1) == true);
	assert(b.remove(6) == false);
	assert(b.size() == 6);
	assert(b.nrOccurrences(1) == 1);
	BagIterator it = b.iterator();
	it.first();
	while (it.valid()) {
		TElem e = it.getCurrent();
		it.next();
	}
}

void testMostFrequentFunction() {
	Bag b;
	assert(b.mostFrequent() == NULL_TELEM);
	b.add(2);
	b.add(3);
	b.add(3);
	b.add(4);
	b.add(4);
	b.add(4);
	b.add(5);
	b.add(5);
	b.add(5);
	b.add(5);  // 5 appears 4 times

	TElem mf = b.mostFrequent();
	assert(mf == 5);  // 5 should be most frequent

	b.add(3);
	b.add(3);
	b.add(3);

	mf = b.mostFrequent();
	assert(mf == 3);  // both valid

}

