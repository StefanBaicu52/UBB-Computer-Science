#include "Bag.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>

using namespace std;

int main() {

	testAll();
	cout << "Short tests over" << endl;
	testMostFrequentFunction();
	cout<<"Frequent tests over" << endl;
	testAllExtended();


	cout << "All test over" << endl;
}