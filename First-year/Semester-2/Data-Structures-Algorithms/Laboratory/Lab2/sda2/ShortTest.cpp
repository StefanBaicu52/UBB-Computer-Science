#include <assert.h>

#include "SortedMap.h"
#include "SMIterator.h"
#include "ShortTest.h"
#include <exception>
using namespace std;

bool relatie1(TKey cheie1, TKey cheie2) {
	if (cheie1 <= cheie2) {
		return true;
	}
	else {
		return false;
	}
}

void testAll(){
	SortedMap sm(relatie1);
	assert(sm.size() == 0);
	assert(sm.isEmpty());
    sm.add(1,2);
    assert(sm.size() == 1);
    assert(!sm.isEmpty());
    assert(sm.search(1)!=NULL_TVALUE);
    TValue v =sm.add(1,3);
    assert(v == 2);
    assert(sm.search(1) == 3);
    SMIterator it = sm.iterator();
    it.first();
    while (it.valid()){
    	TElem e = it.getCurrent();
    	assert(e.second != NULL_TVALUE);
    	it.next();
    }
    assert(sm.remove(1) == 3);
    assert(sm.isEmpty());
}

void testIteratorRemove() {
	SortedMap map([](TKey a, TKey b) { return a <= b; });
	map.add(10, 100);
	map.add(20, 200);

	SMIterator it = map.iterator();
	it.first(); // at 10

	TElem removed = it.remove(); // remove 10
	assert(removed.first == 10);
	assert(map.search(10) == NULL_TVALUE);

	assert(it.valid()); // should now point to 20
	assert(it.getCurrent().first == 20);

	removed = it.remove(); // remove 20
	assert(removed.first == 20);
	assert(map.isEmpty());
	assert(!it.valid()); // iterator now invalid
}

