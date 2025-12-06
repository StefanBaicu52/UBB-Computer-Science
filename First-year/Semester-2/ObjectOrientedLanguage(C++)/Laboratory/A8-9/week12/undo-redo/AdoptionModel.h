#pragma once
#include <QAbstractTableModel>
#include "../repository/AdoptionList.h"

class AdoptionModel : public QAbstractTableModel {
    Q_OBJECT
private:
    AdoptionList& list;

public:
    explicit AdoptionModel(AdoptionList& list, QObject* parent = nullptr);

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;
    int columnCount(const QModelIndex& parent = QModelIndex()) const override;
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role) const override;
};
