#include "mainwindow.h"
#include <QMessageBox>
#include <QInputDialog>
#include <QKeyEvent>
#include <QPushButton>
#include <QTableWidget>
#include <QVBoxLayout>
#include <QTableView>
#include "../validation/validation.h"
#include "../undo-redo/AdoptionModel.h"

MainWindow::MainWindow(Service& service, QWidget* parent)
    : QMainWindow(parent), serv(service) {
    ui.setupUi(this);

    ui.stackedWidget->setCurrentWidget(ui.pageMainMenu);
    ui.adminForms->hide();

    connectMainMenu();
    connectAdminMenu();
    connectUserMenu();
}

MainWindow::~MainWindow() = default;

void MainWindow::connectMainMenu() {
    connect(ui.adminButton, &QPushButton::clicked, this, &MainWindow::goToAdmin);
    connect(ui.userButton, &QPushButton::clicked, this, &MainWindow::goToUser);
    connect(ui.exitButton, &QPushButton::clicked, this, &MainWindow::exitApp);
}

void MainWindow::goToAdmin() {
    ui.stackedWidget->setCurrentWidget(ui.pageAdmin);
    ui.adminForms->hide();
}

void MainWindow::goToUser() {
    ui.stackedWidget->setCurrentWidget(ui.pageUser);
}

void MainWindow::exitApp() {
    QApplication::quit();
}

void MainWindow::connectAdminMenu() {
    connect(ui.addButton, &QPushButton::clicked, this, &MainWindow::adminShowAddForm);
    connect(ui.deleteButton, &QPushButton::clicked, this, &MainWindow::adminShowDeleteForm);
    connect(ui.updateButton, &QPushButton::clicked, this, &MainWindow::adminShowUpdateForm);
    connect(ui.viewButton, &QPushButton::clicked, this, &MainWindow::adminViewDogs);
    connect(ui.logoutAdminButton, &QPushButton::clicked, this, [this]() {
        ui.stackedWidget->setCurrentWidget(ui.pageMainMenu);
    });
    connect(ui.undoButton, &QPushButton::clicked, this, &MainWindow::handleUndo);
    connect(ui.redoButton, &QPushButton::clicked, this, &MainWindow::handleRedo);

    // corect după obiectele din designer
    connect(ui.submitAddButton, &QPushButton::clicked, this, &MainWindow::handleAddDog);
    connect(ui.submitDeleteButton, &QPushButton::clicked, this, &MainWindow::handleDeleteDog);
    connect(ui.submitUpdateButton, &QPushButton::clicked, this, &MainWindow::handleUpdateDog);
}


void MainWindow::adminShowAddForm() { showAdminForm(0); }
void MainWindow::adminShowDeleteForm() { showAdminForm(1); }
void MainWindow::adminShowUpdateForm() { showAdminForm(2); }

void MainWindow::showAdminForm(int index) {
    ui.adminForms->setCurrentIndex(index);
    ui.adminForms->show();
}

void MainWindow::adminViewDogs() {
    serv.reloadFromFile();
    const auto& dogs = serv.getServiceDogs();
    QTableWidget* table = new QTableWidget(this);
    table->setColumnCount(4);
    table->setHorizontalHeaderLabels({ "Name", "Breed", "Age", "Photo" });
    table->setRowCount(static_cast<int>(dogs.size()));

    for (int row = 0; row < dogs.size(); ++row) {
        const Dog& d = dogs[row];
        table->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(d.get_name())));
        table->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(d.get_breed())));
        table->setItem(row, 2, new QTableWidgetItem(QString::number(d.get_age())));
        table->setItem(row, 3, new QTableWidgetItem(QString::fromStdString(d.get_photograph())));
    }

    table->resizeColumnsToContents();
    table->resize(600, 400);

    QWidget* popup = new QWidget;
    QVBoxLayout* layout = new QVBoxLayout(popup);
    layout->addWidget(table);
    popup->setLayout(layout);
    popup->setWindowTitle("All Dogs");
    popup->setAttribute(Qt::WA_DeleteOnClose);
    popup->resize(620, 420);
    popup->show();
}

void MainWindow::connectUserMenu() {
    connect(ui.confirmFormatButton, &QPushButton::clicked, this, &MainWindow::confirmFormat);
    connect(ui.logoutUserButton, &QPushButton::clicked, this, [this]() {
        ui.stackedWidget->setCurrentWidget(ui.pageMainMenu);
    });

    connect(ui.seeOneByOneButton, &QPushButton::clicked, this, [this]() {
        auto& dogs = serv.getServiceDogs();
        int index = 0;
        while (index < dogs.size()) {
            Dog d = dogs[index];
            if (!d.get_adopted()) {
                QString msg = QString::fromStdString(d.dog_to_string()) + "\nAdopt?";
                auto reply = QMessageBox::question(this, "Adopt", msg, QMessageBox::Yes | QMessageBox::No | QMessageBox::Cancel);
                if (reply == QMessageBox::Yes) {
                    serv.userAdoptService(d.get_photograph());
                    QMessageBox::information(this, "Success", "Dog adopted!");
                } else if (reply == QMessageBox::Cancel) {
                    break;
                }
            }
            ++index;
        }
    });

    connect(ui.filterButton, &QPushButton::clicked, this, [this]() {
        QString breed = QInputDialog::getText(this, "Breed", "Enter breed (optional):");
        bool ok;
        int age = QInputDialog::getInt(this, "Age", "Enter max age:", 0, 0, 100, 1, &ok);
        if (!ok) return;

        auto filtered = serv.getDogsByBreedAndAge(breed.toStdString(), age);
        QString result;
        for (const auto& d : filtered)
            result += QString::fromStdString(d.dog_to_string()) + "\n";
        QMessageBox::information(this, "Filtered", result.isEmpty() ? "None found." : result);
    });

    connect(ui.viewListButton, &QPushButton::clicked, this, &MainWindow::showAdoptionTable);
    connect(ui.openFileButton, &QPushButton::clicked, this, [this]() {
        serv.openAdoptionFile();
    });
}

void MainWindow::showAdoptionTable() {
    AdoptionList* list = serv.getRawAdoptionList();
    auto* model = new AdoptionModel(*list);
    auto* table = new QTableView();
    table->setModel(model);
    table->resizeColumnsToContents();
    table->setWindowTitle("Adopted Dogs");
    table->setAttribute(Qt::WA_DeleteOnClose);
    table->resize(600, 400);
    table->show();
}

void MainWindow::confirmFormat() {
    QString format = ui.formatEdit->text().toLower();
    try {
        UIValidator::validate_save_mode(format.toStdString());
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Invalid", e.what());
        format = "csv";
    }

    if (format == "csv")
        serv.setAdoptionList(new CSVOutput());
    else if (format == "html")
        serv.setAdoptionList(new HTMLOutput());
}

void MainWindow::handleUndo() {
    try {
        serv.undo();
        QMessageBox::information(this, "Undo", "Undo successful.");
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Undo", e.what());
    }
}

void MainWindow::handleRedo() {
    try {
        serv.redo();
        QMessageBox::information(this, "Redo", "Redo successful.");
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Redo", e.what());
    }
}

void MainWindow::keyPressEvent(QKeyEvent* event) {
    if (event->modifiers() == Qt::ControlModifier && event->key() == Qt::Key_Z) {
        handleUndo();
    } else if (event->modifiers() == Qt::ControlModifier && event->key() == Qt::Key_Y) {
        handleRedo();
    } else {
        QMainWindow::keyPressEvent(event);
    }
}

void MainWindow::handleAddDog() {
    QString name = ui.nameEdit->text();
    QString breed = ui.breedEdit->text();
    QString ageStr = ui.ageEdit->text();
    QString photo = ui.photoEdit->text();

    try {
        UIValidator::validate_letters_only(name.toStdString());
        UIValidator::validate_letters_only(breed.toStdString());
        UIValidator::validate_digits_only(ageStr.toStdString());
        UIValidator::validate_empty(photo.toStdString());

        int age = ageStr.toInt();
        UIValidator::validate_age(age);

        bool ok = serv.adminAddService(name.toStdString(), breed.toStdString(), age, photo.toStdString());
        if (ok)
            QMessageBox::information(this, "Success", "Dog added.");
        else
            QMessageBox::warning(this, "Failed", "Dog already exists.");
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Error", e.what());
    }
}
void MainWindow::handleDeleteDog() {
    QString photo = ui.photoDeleteEdit->text();

    try {
        UIValidator::validate_empty(photo.toStdString());

        bool ok = serv.adminRemoveService(photo.toStdString());
        if (ok)
            QMessageBox::information(this, "Success", "Dog deleted.");
        else
            QMessageBox::warning(this, "Failed", "Dog not found.");
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Error", e.what());
    }
}

void MainWindow::handleUpdateDog() {
    QString name = ui.nameUpdateEdit->text();
    QString breed = ui.breedUpdateEdit->text();
    QString ageStr = ui.ageUpdateEdit->text();
    QString photo = ui.photoUpdateEdit->text();

    try {
        UIValidator::validate_letters_only(name.toStdString());
        UIValidator::validate_letters_only(breed.toStdString());
        UIValidator::validate_digits_only(ageStr.toStdString());
        UIValidator::validate_empty(photo.toStdString());

        int age = ageStr.toInt();
        UIValidator::validate_age(age);

        bool ok = serv.adminUpdateService(photo.toStdString(), name.toStdString(), breed.toStdString(), age);
        if (ok)
            QMessageBox::information(this, "Success", "Dog updated.");
        else
            QMessageBox::warning(this, "Failed", "Dog not found.");
    } catch (const std::exception& e) {
        QMessageBox::warning(this, "Error", e.what());
    }
}
