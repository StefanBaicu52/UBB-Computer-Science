#pragma once

#include <QMainWindow>
#include <QApplication>
#include <QKeyEvent>
#include <QShortcut>
#include "ui_mainwindow.h"
#include "../service/service.h"

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(Service& service, QWidget* parent = nullptr);
    ~MainWindow();

protected:
    void keyPressEvent(QKeyEvent* event) override;

private:
    Ui::MainWindow ui;
    Service& serv;

    QShortcut* undoShortcut;
    QShortcut* redoShortcut;

    // UI wiring
    void connectMainMenu();
    void connectAdminMenu();
    void connectUserMenu();
    void showAdminForm(int index);
    void setupShortcuts();  // Ctrl+Z / Ctrl+Y

    private slots:
        // Navigation
        void goToAdmin();
    void goToUser();
    void exitApp();

    // Admin view handlers
    void adminShowAddForm();
    void adminShowDeleteForm();
    void adminShowUpdateForm();
    void adminViewDogs();

    // Admin dog actions
    void handleAddDog();
    void handleDeleteDog();
    void handleUpdateDog();

    // User view handlers
    void confirmFormat();
    void showAdoptionTable();

    // Undo / Redo
    void handleUndo();
    void handleRedo();
};
