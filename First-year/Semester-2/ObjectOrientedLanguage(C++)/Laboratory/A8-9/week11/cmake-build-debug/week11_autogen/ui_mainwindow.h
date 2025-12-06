/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.9.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QVBoxLayout *verticalLayout;
    QStackedWidget *stackedWidget;
    QWidget *mainPage;
    QVBoxLayout *mainLayout;
    QPushButton *adminButton;
    QPushButton *userButton;
    QPushButton *exitButton;
    QWidget *adminPage;
    QVBoxLayout *adminLayout;
    QPushButton *addDogButton;
    QPushButton *deleteDogButton;
    QPushButton *updateDogButton;
    QPushButton *viewDogsButton;
    QPushButton *adminBackButton;
    QLineEdit *nameLineEdit;
    QLineEdit *breedLineEdit;
    QLineEdit *ageLineEdit;
    QLineEdit *photoLineEdit;
    QLineEdit *deletePhotoLineEdit;
    QLineEdit *updatePhotoLineEdit;
    QLineEdit *updateNameLineEdit;
    QLineEdit *updateBreedLineEdit;
    QLineEdit *updateAgeLineEdit;
    QTableWidget *dogTable;
    QWidget *userFormatPage;
    QVBoxLayout *formatLayout;
    QComboBox *formatComboBox;
    QPushButton *confirmFormatButton;
    QWidget *userPage;
    QVBoxLayout *userLayout;
    QPushButton *userViewOneByOneButton;
    QPushButton *filterDogsButton;
    QPushButton *viewAdoptionListButton;
    QPushButton *openAdoptionFileButton;
    QPushButton *userBackButton;
    QLineEdit *filterBreedLineEdit;
    QSpinBox *filterAgeSpinBox;

    void setupUi(QWidget *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 600);
        verticalLayout = new QVBoxLayout(MainWindow);
        verticalLayout->setObjectName("verticalLayout");
        stackedWidget = new QStackedWidget(MainWindow);
        stackedWidget->setObjectName("stackedWidget");
        mainPage = new QWidget();
        mainPage->setObjectName("mainPage");
        mainLayout = new QVBoxLayout(mainPage);
        mainLayout->setObjectName("mainLayout");
        adminButton = new QPushButton(mainPage);
        adminButton->setObjectName("adminButton");

        mainLayout->addWidget(adminButton);

        userButton = new QPushButton(mainPage);
        userButton->setObjectName("userButton");

        mainLayout->addWidget(userButton);

        exitButton = new QPushButton(mainPage);
        exitButton->setObjectName("exitButton");

        mainLayout->addWidget(exitButton);

        stackedWidget->addWidget(mainPage);
        adminPage = new QWidget();
        adminPage->setObjectName("adminPage");
        adminLayout = new QVBoxLayout(adminPage);
        adminLayout->setObjectName("adminLayout");
        addDogButton = new QPushButton(adminPage);
        addDogButton->setObjectName("addDogButton");

        adminLayout->addWidget(addDogButton);

        deleteDogButton = new QPushButton(adminPage);
        deleteDogButton->setObjectName("deleteDogButton");

        adminLayout->addWidget(deleteDogButton);

        updateDogButton = new QPushButton(adminPage);
        updateDogButton->setObjectName("updateDogButton");

        adminLayout->addWidget(updateDogButton);

        viewDogsButton = new QPushButton(adminPage);
        viewDogsButton->setObjectName("viewDogsButton");

        adminLayout->addWidget(viewDogsButton);

        adminBackButton = new QPushButton(adminPage);
        adminBackButton->setObjectName("adminBackButton");

        adminLayout->addWidget(adminBackButton);

        nameLineEdit = new QLineEdit(adminPage);
        nameLineEdit->setObjectName("nameLineEdit");

        adminLayout->addWidget(nameLineEdit);

        breedLineEdit = new QLineEdit(adminPage);
        breedLineEdit->setObjectName("breedLineEdit");

        adminLayout->addWidget(breedLineEdit);

        ageLineEdit = new QLineEdit(adminPage);
        ageLineEdit->setObjectName("ageLineEdit");

        adminLayout->addWidget(ageLineEdit);

        photoLineEdit = new QLineEdit(adminPage);
        photoLineEdit->setObjectName("photoLineEdit");

        adminLayout->addWidget(photoLineEdit);

        deletePhotoLineEdit = new QLineEdit(adminPage);
        deletePhotoLineEdit->setObjectName("deletePhotoLineEdit");

        adminLayout->addWidget(deletePhotoLineEdit);

        updatePhotoLineEdit = new QLineEdit(adminPage);
        updatePhotoLineEdit->setObjectName("updatePhotoLineEdit");

        adminLayout->addWidget(updatePhotoLineEdit);

        updateNameLineEdit = new QLineEdit(adminPage);
        updateNameLineEdit->setObjectName("updateNameLineEdit");

        adminLayout->addWidget(updateNameLineEdit);

        updateBreedLineEdit = new QLineEdit(adminPage);
        updateBreedLineEdit->setObjectName("updateBreedLineEdit");

        adminLayout->addWidget(updateBreedLineEdit);

        updateAgeLineEdit = new QLineEdit(adminPage);
        updateAgeLineEdit->setObjectName("updateAgeLineEdit");

        adminLayout->addWidget(updateAgeLineEdit);

        dogTable = new QTableWidget(adminPage);
        dogTable->setObjectName("dogTable");

        adminLayout->addWidget(dogTable);

        stackedWidget->addWidget(adminPage);
        userFormatPage = new QWidget();
        userFormatPage->setObjectName("userFormatPage");
        formatLayout = new QVBoxLayout(userFormatPage);
        formatLayout->setObjectName("formatLayout");
        formatComboBox = new QComboBox(userFormatPage);
        formatComboBox->addItem(QString());
        formatComboBox->addItem(QString());
        formatComboBox->setObjectName("formatComboBox");

        formatLayout->addWidget(formatComboBox);

        confirmFormatButton = new QPushButton(userFormatPage);
        confirmFormatButton->setObjectName("confirmFormatButton");

        formatLayout->addWidget(confirmFormatButton);

        stackedWidget->addWidget(userFormatPage);
        userPage = new QWidget();
        userPage->setObjectName("userPage");
        userLayout = new QVBoxLayout(userPage);
        userLayout->setObjectName("userLayout");
        userViewOneByOneButton = new QPushButton(userPage);
        userViewOneByOneButton->setObjectName("userViewOneByOneButton");

        userLayout->addWidget(userViewOneByOneButton);

        filterDogsButton = new QPushButton(userPage);
        filterDogsButton->setObjectName("filterDogsButton");

        userLayout->addWidget(filterDogsButton);

        viewAdoptionListButton = new QPushButton(userPage);
        viewAdoptionListButton->setObjectName("viewAdoptionListButton");

        userLayout->addWidget(viewAdoptionListButton);

        openAdoptionFileButton = new QPushButton(userPage);
        openAdoptionFileButton->setObjectName("openAdoptionFileButton");

        userLayout->addWidget(openAdoptionFileButton);

        userBackButton = new QPushButton(userPage);
        userBackButton->setObjectName("userBackButton");

        userLayout->addWidget(userBackButton);

        filterBreedLineEdit = new QLineEdit(userPage);
        filterBreedLineEdit->setObjectName("filterBreedLineEdit");

        userLayout->addWidget(filterBreedLineEdit);

        filterAgeSpinBox = new QSpinBox(userPage);
        filterAgeSpinBox->setObjectName("filterAgeSpinBox");

        userLayout->addWidget(filterAgeSpinBox);

        stackedWidget->addWidget(userPage);

        verticalLayout->addWidget(stackedWidget);


        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QWidget *MainWindow)
    {
        adminButton->setText(QCoreApplication::translate("MainWindow", "Admin", nullptr));
        userButton->setText(QCoreApplication::translate("MainWindow", "User", nullptr));
        exitButton->setText(QCoreApplication::translate("MainWindow", "Exit", nullptr));
        addDogButton->setText(QCoreApplication::translate("MainWindow", "Add Dog", nullptr));
        deleteDogButton->setText(QCoreApplication::translate("MainWindow", "Delete Dog", nullptr));
        updateDogButton->setText(QCoreApplication::translate("MainWindow", "Update Dog", nullptr));
        viewDogsButton->setText(QCoreApplication::translate("MainWindow", "View Dogs", nullptr));
        adminBackButton->setText(QCoreApplication::translate("MainWindow", "Back", nullptr));
        formatComboBox->setItemText(0, QCoreApplication::translate("MainWindow", "csv", nullptr));
        formatComboBox->setItemText(1, QCoreApplication::translate("MainWindow", "html", nullptr));

        confirmFormatButton->setText(QCoreApplication::translate("MainWindow", "Confirm", nullptr));
        userViewOneByOneButton->setText(QCoreApplication::translate("MainWindow", "See Dogs One by One", nullptr));
        filterDogsButton->setText(QCoreApplication::translate("MainWindow", "See by Breed and Age", nullptr));
        viewAdoptionListButton->setText(QCoreApplication::translate("MainWindow", "See Adoption List", nullptr));
        openAdoptionFileButton->setText(QCoreApplication::translate("MainWindow", "Open Adoption File", nullptr));
        userBackButton->setText(QCoreApplication::translate("MainWindow", "Back", nullptr));
        (void)MainWindow;
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
