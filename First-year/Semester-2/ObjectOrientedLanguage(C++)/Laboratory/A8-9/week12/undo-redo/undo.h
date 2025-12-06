#pragma once
#include "../domain/dog.h"

class Service;

class UndoAction {
public:
    virtual void doUndo() = 0;
    virtual void doRedo() = 0;
    virtual ~UndoAction() = default;
};

class UndoAdd : public UndoAction {
private:
    Dog addedDog;
    Service& service;

public:
    UndoAdd(Service& serv, const Dog& d) : service(serv), addedDog(d) {}

    void doUndo() override;  // implemented in undo.cpp
    void doRedo() override;
};

class UndoRemove : public UndoAction {
private:
    Dog removedDog;
    Service& service;

public:
    UndoRemove(Service& serv, const Dog& d) : service(serv), removedDog(d) {}

    void doUndo() override;
    void doRedo() override;
};

class UndoUpdate : public UndoAction {
private:
    Dog oldDog, newDog;
    Service& service;

public:
    UndoUpdate(Service& serv, const Dog& oldD, const Dog& newD)
        : service(serv), oldDog(oldD), newDog(newD) {}

    void doUndo() override;
    void doRedo() override;
};
