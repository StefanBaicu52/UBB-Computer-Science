#include "AdoptionModel.h"

AdoptionModel::AdoptionModel(AdoptionList& list, QObject* parent)
    : QAbstractTableModel(parent), list(list) {}

int AdoptionModel::rowCount(const QModelIndex& parent) const {
    Q_UNUSED(parent);
    return static_cast<int>(list.getDogs().size());
}

int AdoptionModel::columnCount(const QModelIndex& parent) const {
    Q_UNUSED(parent);
    return 4; // name, breed, age, photo
}

QVariant AdoptionModel::data(const QModelIndex& index, int role) const {
    if (!index.isValid() || role != Qt::DisplayRole)
        return {};

    const Dog& dog = list.getDogs()[index.row()];
    switch (index.column()) {
        case 0: return QString::fromStdString(dog.get_name());
        case 1: return QString::fromStdString(dog.get_breed());
        case 2: return dog.get_age();
        case 3: return QString::fromStdString(dog.get_photograph());
        default: return {};
    }
}

QVariant AdoptionModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role != Qt::DisplayRole || orientation != Qt::Horizontal)
        return {};

    switch (section) {
        case 0: return "Name";
        case 1: return "Breed";
        case 2: return "Age";
        case 3: return "Photograph";
        default: return {};
    }
}
