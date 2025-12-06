#include "ui/ui.h"
#include "tests/tests.h"
#include <iostream>

int main()
{
    std::cout << "\nRunning tests...\n";
    Tests tests;
    tests.test_all();

    std::cout << "\n>>Starting application...\n";

    UI ui;
    int result = ui.main_menu();

    if (result == 0) {
        std::cout << "Session ended successfully.\n";
    } else {
        std::cout << "An error occurred during the session.\n";
    }

    return 0;
}
