package model.state;



public interface ISymbolTable<K, V> {
    boolean isDefined(K key);     // verifică dacă cheia există
    void put(K key, V value);     // adaugă o pereche nouă (ca la declarare)
    void update(K key, V value);  // actualizează valoarea existentă
    V getValue(K key);              // preia valoarea (nume conform PDF)

}
