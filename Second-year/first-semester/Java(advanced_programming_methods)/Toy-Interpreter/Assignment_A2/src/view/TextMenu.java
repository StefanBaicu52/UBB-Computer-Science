package view;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TextMenu {

    // Mapa care va ține comenzi cu cheia și descrierea lor
    private final Map<String, Command> commands;

    // Constructorul clasei, initializează mapa de comenzi
    public TextMenu() {
        commands = new HashMap<>();
    }

    // Adăugăm o comandă în mapă
    public void addCommand(Command c) {
        commands.put(c.getKey(), c);
    }

    // Afișăm meniul în formatul dorit
    private void printMenu() {
        System.out.println("\n=== MENIU PRINCIPAL ===");
        // Afișăm opțiunile în funcție de comenzile disponibile
        for (Command com : commands.values()) {
            String line = String.format("%4s : %s", com.getKey(), com.getDescription());
            System.out.println(line);
        }
        System.out.println();  // Adăugăm un spațiu la sfârșit
    }

    // Metoda principală care afișează meniul și gestionează selecția utilizatorului
    public void show() {
        Scanner scanner = new Scanner(System.in);
        boolean finished = false;

        while (!finished) {
            printMenu();  // Afișăm meniul
            System.out.print("Alege programul: ");  // Mesajul pentru utilizator

            // Citim inputul utilizatorului și eliminăm eventualele spații suplimentare
            String key = scanner.nextLine().trim();

            // Căutăm comanda în mapă
            Command com = commands.get(key);

            // Dacă opțiunea nu există în mapă, afișăm un mesaj de eroare
            if (com == null) {
                System.out.println("Optiune invalida! Incearca din nou.");
            } else {
                // Dacă utilizatorul a ales opțiunea de ieșire (0), încheiem bucla
                if (key.equals("0")) {
                    finished = true;
                    System.out.println("Iesire... Programul s-a încheiat.");
                } else {
                    // Executăm comanda selectată
                    com.execute();
                }
            }
        }
        scanner.close();  // Închidem scanner-ul pentru a evita eventuale memory leak-uri
    }
}