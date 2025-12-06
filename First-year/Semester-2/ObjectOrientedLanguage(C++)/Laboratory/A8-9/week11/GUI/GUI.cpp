#include "GUI.h"

GUI::GUI(Service& serviceRef, QWidget* parent): QWidget(parent), serv(serviceRef) // initializez referinta la service si parintele
{
    this->setMinimumSize(600, 400); //pentru a stabili dimeniusnea ferestrei
    mainLayout = new QVBoxLayout();// creez layout-ul principal vertical
    this->setLayout(mainLayout);//asociaza layout-ul cu fereastra(GUI)l
    mainMenu();//AFISEZ MENIUL PRINCIPAL
}


void GUI::clearLayout(QLayout* layout) {
    if (!layout) return;

    while (layout->count() > 0) {
        QLayoutItem* item = layout->takeAt(0);
        if (!item) continue;

        if (QWidget* widget = item->widget()) {
            widget->hide();
            widget->setParent(nullptr);
            delete widget;
        }
        if (QLayout* childLayout = item->layout()) {
            clearLayout(childLayout);
        }
        delete item;
    }
}

void GUI::clearLayout() {
    clearLayout(mainLayout);
}

void GUI::mainMenu() {
    clearLayout(); //curat layout-ul de orice widget existent

    QLabel* label = new QLabel("CHOOSE USER OR SHUT DOWN SESSION:");
    label->setAlignment(Qt::AlignCenter);

    QPushButton* adminButton = new QPushButton(" Admin");
    QPushButton* userButton = new QPushButton(" User");
    QPushButton* exitButton = new QPushButton("SHUT DOWN");

    //adaug butoanele in layout ul principal
    mainLayout->addWidget(label);
    mainLayout->addWidget(adminButton);
    mainLayout->addWidget(userButton);
    mainLayout->addWidget(exitButton);

    connect(adminButton, &QPushButton::clicked, this, &GUI::admin_menu);
    connect(userButton, &QPushButton::clicked, this, &GUI::user_menu);
    connect(exitButton, &QPushButton::clicked, this, &GUI::close);
}

void GUI::user_menu() {
    clearLayout();

    QLabel* label = new QLabel("Choose adoption file format (csv/html): ");
    label->setAlignment(Qt::AlignCenter);

    QPushButton* button1 = new QPushButton("See dogs one by one");
    QPushButton* button2 = new QPushButton("See dogs by breed and age");
    QPushButton* button3 = new QPushButton("See adoption list");
    QPushButton* button4 = new QPushButton("Open adoption file");
    QPushButton* button5 = new QPushButton("Log out");
    QPushButton* button6 = new QPushButton("Back to main menu");


    mainLayout->addWidget(label);
    mainLayout->addWidget(button1);
    mainLayout->addWidget(button2);
    mainLayout->addWidget(button3);
    mainLayout->addWidget(button4);
    mainLayout->addWidget(button5);
    mainLayout->addWidget(button6);


    connect(button5, &QPushButton::clicked, this, &GUI::close);
    connect(button6, &QPushButton::clicked, this, &GUI::mainMenu);

}



void GUI::admin_menu() {
    clearLayout();

    QLabel* label = new QLabel("Choose an option");
    label->setAlignment(Qt::AlignCenter);
    QPushButton* button1 = new QPushButton("Add dog");
    QPushButton* button2 = new QPushButton("Remove dog");
    QPushButton* button3 = new QPushButton("Update dog");
    QPushButton* button4 = new QPushButton("View dogs");
    QPushButton* button5 = new QPushButton("Log out");
    QPushButton* button6 = new QPushButton("Back to main menu");

    mainLayout->addWidget(label);
    mainLayout->addWidget(button1);
    mainLayout->addWidget(button2);
    mainLayout->addWidget(button3);
    mainLayout->addWidget(button4);
    mainLayout->addWidget(button5);
    mainLayout->addWidget(button6);

    //butoane functionale
    connect(button4, &QPushButton::clicked, this, &GUI::adm_op4);
    connect(button5, &QPushButton::clicked, this, &GUI::close);
    connect(button6, &QPushButton::clicked, this, &GUI::mainMenu);

}

void GUI::adm_op4() {
    clearLayout();

    serv.reloadFromFile();//reincarc datele din fisier(cainii disponibili)

    QLabel* title = new QLabel("All Dogs in the Shelter");
    title->setAlignment(Qt::AlignCenter);
    mainLayout->addWidget(title);

    QTableWidget* table = new QTableWidget();// asa creez un tabel
    const auto& dogs = serv.getServiceDogs();// obtin lista de caini din service

    table->setRowCount(static_cast<int>(dogs.size()));
    table->setColumnCount(5);

    QStringList headers = {"Name", "Breed", "Age", "Photograph", "Adopted"};
    table->setHorizontalHeaderLabels(headers);
    table->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);

    int row = 0;
    for (const auto& dog : dogs) {
        table->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(dog.get_name())));
        table->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(dog.get_breed())));
        table->setItem(row, 2, new QTableWidgetItem(QString::number(dog.get_age())));
        table->setItem(row, 3, new QTableWidgetItem(QString::fromStdString(dog.get_photograph())));
        table->setItem(row, 4, new QTableWidgetItem(dog.get_adopted() ? "Yes" : "No"));
        ++row;
    }

    mainLayout->addWidget(table);

    QPushButton* backButton = new QPushButton("Back");
    connect(backButton, &QPushButton::clicked, this, &GUI::admin_menu);
    mainLayout->addWidget(backButton);
}