#pragma once
#include "SortedMap.h"
#include <utility>
#include <exception>

class SMIterator {
    friend class SortedMap;

private:
    SortedMap& map;
    SortedMap::DLLNode* current;

    SMIterator(SortedMap& mapionar);

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;

    TElem remove();
};
