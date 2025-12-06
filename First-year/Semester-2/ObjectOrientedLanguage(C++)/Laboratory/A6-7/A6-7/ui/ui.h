#pragma once
#include <iostream>
#include "../validation/validation.h"
#include "../service/service.h"

using namespace std;

class UI
{
private:
    Service serv;
    UIValidator val;
    string save_mode;

public:
    UI(Service serv) : serv(serv), val(UIValidator()) {}

    int main_menu();

    void admin_menu();
    void adm_op1();
    void adm_op2();
    void adm_op3();
    void adm_op4();

    void user_menu();
    void user_op1();
    void user_op2();
    void user_op3();
    void user_op4();
};
