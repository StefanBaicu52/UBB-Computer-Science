// #include "ui/ui.h"
// #include "repository/AdoptionList.h"
//
// int main() {
//     AdoptionList* adoptionList = new CSVOutput();
//     Service service(adoptionList);
//     UI ui(service);
//     ui.main_menu();
//     return 0;
// }


#include <QApplication>
#include "GUI/GUI.h"
#include "repository/AdoptionList.h"
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    Service service(new CSVOutput());  // Default, poate fi schimbat de UI
    GUI gui(service);
    gui.show();

    return app.exec();
}
