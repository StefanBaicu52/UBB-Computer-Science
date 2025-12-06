#include <QApplication>
#include "GUI/mainwindow.h"
#include "repository/AdoptionList.h"
#include "repository/AdoptionList.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // poți schimba CSVOutput cu HTMLOutput dacă preferi HTML
    auto* adoptionList = new CSVOutput();
    Service service(adoptionList);

    MainWindow window(service);
    window.show();

    return app.exec();
}
