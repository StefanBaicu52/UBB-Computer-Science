#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

using namespace std;

int main() {
    cout << "Running short tests..." << endl;
    testAll();
    cout << "Short tests passed!" << endl;

    cout << "Running extended tests..." << endl;
    testAllExtended();
    cout << "Extended tests passed!" << endl;

    cout << "All tests passed successfully!" << endl;

    void testIteratorRemove();

    return 0;
}
