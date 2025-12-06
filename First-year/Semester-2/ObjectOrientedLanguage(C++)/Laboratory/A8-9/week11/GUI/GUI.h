#pragma once

#include "../service/service.h"
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QMessageBox>
#include <QScrollArea>
#include <QTableWidget>
#include <QHeaderView>

class GUI : public QWidget {
    Q_OBJECT

private:
    Service& serv;
    QVBoxLayout* mainLayout;

public:
    explicit GUI(Service& serviceRef, QWidget* parent = nullptr);

    void clearLayout(QLayout* layout);
    void clearLayout();

    public slots:
        void mainMenu();
    void admin_menu();
    void user_menu();
    void adm_op4();
};