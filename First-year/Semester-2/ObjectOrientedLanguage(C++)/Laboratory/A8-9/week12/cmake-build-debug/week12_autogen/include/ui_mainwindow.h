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
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *mainLayout;
    QStackedWidget *stackedWidget;
    QWidget *pageMainMenu;
    QVBoxLayout *mainMenuLayout;
    QLabel *mainLabel;
    QPushButton *adminButton;
    QPushButton *userButton;
    QPushButton *exitButton;
    QWidget *pageAdmin;
    QVBoxLayout *vboxLayout;
    QHBoxLayout *hboxLayout;
    QPushButton *addButton;
    QPushButton *deleteButton;
    QPushButton *updateButton;
    QPushButton *viewButton;
    QPushButton *undoButton;
    QPushButton *redoButton;
    QPushButton *logoutAdminButton;
    QStackedWidget *adminForms;
    QWidget *formAdd;
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *nameEdit;
    QLabel *label1;
    QLineEdit *breedEdit;
    QLabel *label2;
    QLineEdit *ageEdit;
    QLabel *label3;
    QLineEdit *photoEdit;
    QPushButton *submitAddButton;
    QWidget *formDelete;
    QFormLayout *formLayout1;
    QLabel *label4;
    QLineEdit *photoDeleteEdit;
    QPushButton *submitDeleteButton;
    QWidget *formUpdate;
    QFormLayout *formLayout2;
    QLabel *label5;
    QLineEdit *photoUpdateEdit;
    QLabel *label6;
    QLineEdit *nameUpdateEdit;
    QLabel *label7;
    QLineEdit *breedUpdateEdit;
    QLabel *label8;
    QLineEdit *ageUpdateEdit;
    QPushButton *submitUpdateButton;
    QWidget *pageUser;
    QVBoxLayout *vboxLayout1;
    QLabel *label9;
    QLineEdit *formatEdit;
    QPushButton *confirmFormatButton;
    QPushButton *seeOneByOneButton;
    QPushButton *filterButton;
    QPushButton *viewListButton;
    QPushButton *openFileButton;
    QPushButton *logoutUserButton;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 600);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        mainLayout = new QVBoxLayout(centralwidget);
        mainLayout->setObjectName("mainLayout");
        stackedWidget = new QStackedWidget(centralwidget);
        stackedWidget->setObjectName("stackedWidget");
        pageMainMenu = new QWidget();
        pageMainMenu->setObjectName("pageMainMenu");
        mainMenuLayout = new QVBoxLayout(pageMainMenu);
        mainMenuLayout->setObjectName("mainMenuLayout");
        mainLabel = new QLabel(pageMainMenu);
        mainLabel->setObjectName("mainLabel");
        mainLabel->setAlignment(Qt::AlignCenter);

        mainMenuLayout->addWidget(mainLabel);

        adminButton = new QPushButton(pageMainMenu);
        adminButton->setObjectName("adminButton");

        mainMenuLayout->addWidget(adminButton);

        userButton = new QPushButton(pageMainMenu);
        userButton->setObjectName("userButton");

        mainMenuLayout->addWidget(userButton);

        exitButton = new QPushButton(pageMainMenu);
        exitButton->setObjectName("exitButton");

        mainMenuLayout->addWidget(exitButton);

        stackedWidget->addWidget(pageMainMenu);
        pageAdmin = new QWidget();
        pageAdmin->setObjectName("pageAdmin");
        vboxLayout = new QVBoxLayout(pageAdmin);
        vboxLayout->setObjectName("vboxLayout");
        hboxLayout = new QHBoxLayout();
        hboxLayout->setObjectName("hboxLayout");
        addButton = new QPushButton(pageAdmin);
        addButton->setObjectName("addButton");

        hboxLayout->addWidget(addButton);

        deleteButton = new QPushButton(pageAdmin);
        deleteButton->setObjectName("deleteButton");

        hboxLayout->addWidget(deleteButton);

        updateButton = new QPushButton(pageAdmin);
        updateButton->setObjectName("updateButton");

        hboxLayout->addWidget(updateButton);

        viewButton = new QPushButton(pageAdmin);
        viewButton->setObjectName("viewButton");

        hboxLayout->addWidget(viewButton);

        undoButton = new QPushButton(pageAdmin);
        undoButton->setObjectName("undoButton");

        hboxLayout->addWidget(undoButton);

        redoButton = new QPushButton(pageAdmin);
        redoButton->setObjectName("redoButton");

        hboxLayout->addWidget(redoButton);

        logoutAdminButton = new QPushButton(pageAdmin);
        logoutAdminButton->setObjectName("logoutAdminButton");

        hboxLayout->addWidget(logoutAdminButton);


        vboxLayout->addLayout(hboxLayout);

        adminForms = new QStackedWidget(pageAdmin);
        adminForms->setObjectName("adminForms");
        formAdd = new QWidget();
        formAdd->setObjectName("formAdd");
        formLayout = new QFormLayout(formAdd);
        formLayout->setObjectName("formLayout");
        label = new QLabel(formAdd);
        label->setObjectName("label");

        formLayout->setWidget(0, QFormLayout::ItemRole::LabelRole, label);

        nameEdit = new QLineEdit(formAdd);
        nameEdit->setObjectName("nameEdit");

        formLayout->setWidget(0, QFormLayout::ItemRole::FieldRole, nameEdit);

        label1 = new QLabel(formAdd);
        label1->setObjectName("label1");

        formLayout->setWidget(1, QFormLayout::ItemRole::LabelRole, label1);

        breedEdit = new QLineEdit(formAdd);
        breedEdit->setObjectName("breedEdit");

        formLayout->setWidget(1, QFormLayout::ItemRole::FieldRole, breedEdit);

        label2 = new QLabel(formAdd);
        label2->setObjectName("label2");

        formLayout->setWidget(2, QFormLayout::ItemRole::LabelRole, label2);

        ageEdit = new QLineEdit(formAdd);
        ageEdit->setObjectName("ageEdit");

        formLayout->setWidget(2, QFormLayout::ItemRole::FieldRole, ageEdit);

        label3 = new QLabel(formAdd);
        label3->setObjectName("label3");

        formLayout->setWidget(3, QFormLayout::ItemRole::LabelRole, label3);

        photoEdit = new QLineEdit(formAdd);
        photoEdit->setObjectName("photoEdit");

        formLayout->setWidget(3, QFormLayout::ItemRole::FieldRole, photoEdit);

        submitAddButton = new QPushButton(formAdd);
        submitAddButton->setObjectName("submitAddButton");

        formLayout->setWidget(4, QFormLayout::ItemRole::FieldRole, submitAddButton);

        adminForms->addWidget(formAdd);
        formDelete = new QWidget();
        formDelete->setObjectName("formDelete");
        formLayout1 = new QFormLayout(formDelete);
        formLayout1->setObjectName("formLayout1");
        label4 = new QLabel(formDelete);
        label4->setObjectName("label4");

        formLayout1->setWidget(0, QFormLayout::ItemRole::LabelRole, label4);

        photoDeleteEdit = new QLineEdit(formDelete);
        photoDeleteEdit->setObjectName("photoDeleteEdit");

        formLayout1->setWidget(0, QFormLayout::ItemRole::FieldRole, photoDeleteEdit);

        submitDeleteButton = new QPushButton(formDelete);
        submitDeleteButton->setObjectName("submitDeleteButton");

        formLayout1->setWidget(1, QFormLayout::ItemRole::FieldRole, submitDeleteButton);

        adminForms->addWidget(formDelete);
        formUpdate = new QWidget();
        formUpdate->setObjectName("formUpdate");
        formLayout2 = new QFormLayout(formUpdate);
        formLayout2->setObjectName("formLayout2");
        label5 = new QLabel(formUpdate);
        label5->setObjectName("label5");

        formLayout2->setWidget(0, QFormLayout::ItemRole::LabelRole, label5);

        photoUpdateEdit = new QLineEdit(formUpdate);
        photoUpdateEdit->setObjectName("photoUpdateEdit");

        formLayout2->setWidget(0, QFormLayout::ItemRole::FieldRole, photoUpdateEdit);

        label6 = new QLabel(formUpdate);
        label6->setObjectName("label6");

        formLayout2->setWidget(1, QFormLayout::ItemRole::LabelRole, label6);

        nameUpdateEdit = new QLineEdit(formUpdate);
        nameUpdateEdit->setObjectName("nameUpdateEdit");

        formLayout2->setWidget(1, QFormLayout::ItemRole::FieldRole, nameUpdateEdit);

        label7 = new QLabel(formUpdate);
        label7->setObjectName("label7");

        formLayout2->setWidget(2, QFormLayout::ItemRole::LabelRole, label7);

        breedUpdateEdit = new QLineEdit(formUpdate);
        breedUpdateEdit->setObjectName("breedUpdateEdit");

        formLayout2->setWidget(2, QFormLayout::ItemRole::FieldRole, breedUpdateEdit);

        label8 = new QLabel(formUpdate);
        label8->setObjectName("label8");

        formLayout2->setWidget(3, QFormLayout::ItemRole::LabelRole, label8);

        ageUpdateEdit = new QLineEdit(formUpdate);
        ageUpdateEdit->setObjectName("ageUpdateEdit");

        formLayout2->setWidget(3, QFormLayout::ItemRole::FieldRole, ageUpdateEdit);

        submitUpdateButton = new QPushButton(formUpdate);
        submitUpdateButton->setObjectName("submitUpdateButton");

        formLayout2->setWidget(4, QFormLayout::ItemRole::FieldRole, submitUpdateButton);

        adminForms->addWidget(formUpdate);

        vboxLayout->addWidget(adminForms);

        stackedWidget->addWidget(pageAdmin);
        pageUser = new QWidget();
        pageUser->setObjectName("pageUser");
        vboxLayout1 = new QVBoxLayout(pageUser);
        vboxLayout1->setObjectName("vboxLayout1");
        label9 = new QLabel(pageUser);
        label9->setObjectName("label9");

        vboxLayout1->addWidget(label9);

        formatEdit = new QLineEdit(pageUser);
        formatEdit->setObjectName("formatEdit");

        vboxLayout1->addWidget(formatEdit);

        confirmFormatButton = new QPushButton(pageUser);
        confirmFormatButton->setObjectName("confirmFormatButton");

        vboxLayout1->addWidget(confirmFormatButton);

        seeOneByOneButton = new QPushButton(pageUser);
        seeOneByOneButton->setObjectName("seeOneByOneButton");

        vboxLayout1->addWidget(seeOneByOneButton);

        filterButton = new QPushButton(pageUser);
        filterButton->setObjectName("filterButton");

        vboxLayout1->addWidget(filterButton);

        viewListButton = new QPushButton(pageUser);
        viewListButton->setObjectName("viewListButton");

        vboxLayout1->addWidget(viewListButton);

        openFileButton = new QPushButton(pageUser);
        openFileButton->setObjectName("openFileButton");

        vboxLayout1->addWidget(openFileButton);

        logoutUserButton = new QPushButton(pageUser);
        logoutUserButton->setObjectName("logoutUserButton");

        vboxLayout1->addWidget(logoutUserButton);

        stackedWidget->addWidget(pageUser);

        mainLayout->addWidget(stackedWidget);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        mainLabel->setText(QCoreApplication::translate("MainWindow", "CHOOSE USER OR SHUT DOWN SESSION:", nullptr));
        adminButton->setText(QCoreApplication::translate("MainWindow", "Admin", nullptr));
        userButton->setText(QCoreApplication::translate("MainWindow", "User", nullptr));
        exitButton->setText(QCoreApplication::translate("MainWindow", "Exit App", nullptr));
        addButton->setText(QCoreApplication::translate("MainWindow", "Add Dog", nullptr));
        deleteButton->setText(QCoreApplication::translate("MainWindow", "Remove Dog", nullptr));
        updateButton->setText(QCoreApplication::translate("MainWindow", "Update Dog", nullptr));
        viewButton->setText(QCoreApplication::translate("MainWindow", "View Dogs", nullptr));
        undoButton->setText(QCoreApplication::translate("MainWindow", "Undo", nullptr));
        redoButton->setText(QCoreApplication::translate("MainWindow", "Redo", nullptr));
        logoutAdminButton->setText(QCoreApplication::translate("MainWindow", "Back", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Name:", nullptr));
        label1->setText(QCoreApplication::translate("MainWindow", "Breed:", nullptr));
        label2->setText(QCoreApplication::translate("MainWindow", "Age:", nullptr));
        label3->setText(QCoreApplication::translate("MainWindow", "Photo:", nullptr));
        submitAddButton->setText(QCoreApplication::translate("MainWindow", "Submit Add", nullptr));
        label4->setText(QCoreApplication::translate("MainWindow", "Photograph:", nullptr));
        submitDeleteButton->setText(QCoreApplication::translate("MainWindow", "Submit Delete", nullptr));
        label5->setText(QCoreApplication::translate("MainWindow", "Photograph:", nullptr));
        label6->setText(QCoreApplication::translate("MainWindow", "Name:", nullptr));
        label7->setText(QCoreApplication::translate("MainWindow", "Breed:", nullptr));
        label8->setText(QCoreApplication::translate("MainWindow", "Age:", nullptr));
        submitUpdateButton->setText(QCoreApplication::translate("MainWindow", "Submit Update", nullptr));
        label9->setText(QCoreApplication::translate("MainWindow", "Choose adoption file format (csv/html):", nullptr));
        confirmFormatButton->setText(QCoreApplication::translate("MainWindow", "Confirm Format", nullptr));
        seeOneByOneButton->setText(QCoreApplication::translate("MainWindow", "See dogs one by one", nullptr));
        filterButton->setText(QCoreApplication::translate("MainWindow", "See dogs by breed and age", nullptr));
        viewListButton->setText(QCoreApplication::translate("MainWindow", "See adoption list", nullptr));
        openFileButton->setText(QCoreApplication::translate("MainWindow", "Open adoption file", nullptr));
        logoutUserButton->setText(QCoreApplication::translate("MainWindow", "Log out", nullptr));
        (void)MainWindow;
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
