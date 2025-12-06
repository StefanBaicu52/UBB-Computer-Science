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
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QVBoxLayout *verticalLayout;
    QStackedWidget *stackedWidget;
    QWidget *mainPage;
    QVBoxLayout *mainPageLayout;
    QPushButton *adminButton;
    QPushButton *userButton;
    QPushButton *exitButton;
    QWidget *userFormatPage;
    QVBoxLayout *userFormatLayout;
    QLabel *formatLabel;
    QHBoxLayout *hboxLayout;
    QPushButton *csvButton;
    QPushButton *htmlButton;
    QWidget *adminPage;
    QVBoxLayout *adminLayout;
    QPushButton *addDogButton;
    QPushButton *deleteDogButton;
    QPushButton *updateDogButton;
    QPushButton *viewDogsButton;
    QPushButton *adminBackButton;
    QWidget *page;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QPushButton *userViewOneByOneButton;
    QPushButton *filterDogsButton;
    QPushButton *viewAdoptionListButton;
    QPushButton *openAdoptionFileButton;
    QPushButton *userBackButton;

    void setupUi(QWidget *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(222, 206);
        verticalLayout = new QVBoxLayout(MainWindow);
        verticalLayout->setObjectName("verticalLayout");
        stackedWidget = new QStackedWidget(MainWindow);
        stackedWidget->setObjectName("stackedWidget");
        mainPage = new QWidget();
        mainPage->setObjectName("mainPage");
        mainPageLayout = new QVBoxLayout(mainPage);
        mainPageLayout->setObjectName("mainPageLayout");
        adminButton = new QPushButton(mainPage);
        adminButton->setObjectName("adminButton");

        mainPageLayout->addWidget(adminButton);

        userButton = new QPushButton(mainPage);
        userButton->setObjectName("userButton");

        mainPageLayout->addWidget(userButton);

        exitButton = new QPushButton(mainPage);
        exitButton->setObjectName("exitButton");

        mainPageLayout->addWidget(exitButton);

        stackedWidget->addWidget(mainPage);
        userFormatPage = new QWidget();
        userFormatPage->setObjectName("userFormatPage");
        userFormatLayout = new QVBoxLayout(userFormatPage);
        userFormatLayout->setObjectName("userFormatLayout");
        formatLabel = new QLabel(userFormatPage);
        formatLabel->setObjectName("formatLabel");

        userFormatLayout->addWidget(formatLabel);

        hboxLayout = new QHBoxLayout();
        hboxLayout->setObjectName("hboxLayout");
        csvButton = new QPushButton(userFormatPage);
        csvButton->setObjectName("csvButton");

        hboxLayout->addWidget(csvButton);

        htmlButton = new QPushButton(userFormatPage);
        htmlButton->setObjectName("htmlButton");

        hboxLayout->addWidget(htmlButton);


        userFormatLayout->addLayout(hboxLayout);

        stackedWidget->addWidget(userFormatPage);
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

        stackedWidget->addWidget(adminPage);
        page = new QWidget();
        page->setObjectName("page");
        verticalLayoutWidget = new QWidget(page);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(-1, 9, 199, 171));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        userViewOneByOneButton = new QPushButton(verticalLayoutWidget);
        userViewOneByOneButton->setObjectName("userViewOneByOneButton");

        verticalLayout_2->addWidget(userViewOneByOneButton);

        filterDogsButton = new QPushButton(verticalLayoutWidget);
        filterDogsButton->setObjectName("filterDogsButton");

        verticalLayout_2->addWidget(filterDogsButton);

        viewAdoptionListButton = new QPushButton(verticalLayoutWidget);
        viewAdoptionListButton->setObjectName("viewAdoptionListButton");

        verticalLayout_2->addWidget(viewAdoptionListButton);

        openAdoptionFileButton = new QPushButton(verticalLayoutWidget);
        openAdoptionFileButton->setObjectName("openAdoptionFileButton");

        verticalLayout_2->addWidget(openAdoptionFileButton);

        userBackButton = new QPushButton(verticalLayoutWidget);
        userBackButton->setObjectName("userBackButton");

        verticalLayout_2->addWidget(userBackButton);

        stackedWidget->addWidget(page);

        verticalLayout->addWidget(stackedWidget);


        retranslateUi(MainWindow);

        stackedWidget->setCurrentIndex(3);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QWidget *MainWindow)
    {
        adminButton->setText(QCoreApplication::translate("MainWindow", "Admin", nullptr));
        userButton->setText(QCoreApplication::translate("MainWindow", "User", nullptr));
        exitButton->setText(QCoreApplication::translate("MainWindow", "Exit", nullptr));
        formatLabel->setText(QCoreApplication::translate("MainWindow", "Choose format:", nullptr));
        csvButton->setText(QCoreApplication::translate("MainWindow", "CSV", nullptr));
        htmlButton->setText(QCoreApplication::translate("MainWindow", "HTML", nullptr));
        addDogButton->setText(QCoreApplication::translate("MainWindow", "Add Dog", nullptr));
        deleteDogButton->setText(QCoreApplication::translate("MainWindow", "Delete Dog", nullptr));
        updateDogButton->setText(QCoreApplication::translate("MainWindow", "Update Dog", nullptr));
        viewDogsButton->setText(QCoreApplication::translate("MainWindow", "View Dogs", nullptr));
        adminBackButton->setText(QCoreApplication::translate("MainWindow", "Back", nullptr));
        userViewOneByOneButton->setText(QCoreApplication::translate("MainWindow", "See dogs one by one", nullptr));
        filterDogsButton->setText(QCoreApplication::translate("MainWindow", "See dogs by breed  and age", nullptr));
        viewAdoptionListButton->setText(QCoreApplication::translate("MainWindow", "See adoption list", nullptr));
        openAdoptionFileButton->setText(QCoreApplication::translate("MainWindow", "Open adoption file", nullptr));
        userBackButton->setText(QCoreApplication::translate("MainWindow", "Back", nullptr));
        (void)MainWindow;
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
