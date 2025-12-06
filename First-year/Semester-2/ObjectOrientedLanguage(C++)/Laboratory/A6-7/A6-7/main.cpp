#include "ui/ui.h"
#include "repository/AdoptionList.h"

int main() {
    AdoptionList* adoptionList = new CSVOutput();
    Service service(adoptionList);
    UI ui(service);
    ui.main_menu();
    return 0;
}
