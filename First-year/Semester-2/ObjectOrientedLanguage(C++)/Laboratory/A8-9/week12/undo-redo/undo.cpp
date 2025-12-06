#include "undo.h"
#include "../service/service.h"

// === UndoAdd ===
void UndoAdd::doUndo() {
    service.removeDogNoUndo(addedDog.get_photograph());
}

void UndoAdd::doRedo() {
    service.addDogNoUndo(addedDog);
}

// === UndoRemove ===
void UndoRemove::doUndo() {
    service.addDogNoUndo(removedDog);
}

void UndoRemove::doRedo() {
    service.removeDogNoUndo(removedDog.get_photograph());
}

// === UndoUpdate ===
void UndoUpdate::doUndo() {
    service.updateDogNoUndo(oldDog);
}

void UndoUpdate::doRedo() {
    service.updateDogNoUndo(newDog);
}
