package view;

import controller.Controller;
import exceptions.InterpreterException;
import exceptions.MyException;
import exceptions.TypeMismatchException;
import repository.IRepository;
import repository.Repository;
import model.state.ProgramState;

import java.io.IOException;

public class RunExample extends Command {
    private final Controller ctrl;
    private boolean alreadyRun;

    public RunExample(String key, String desc, Controller ctrl) {
        super(key, desc);
        this.ctrl = ctrl;
        this.alreadyRun = false;
    }

    @Override
    public void execute() {
        if (alreadyRun) {
            throw new TypeMismatchException("Programul a fost deja rulat și nu poate fi rulat din nou.");
        }

        try {
            System.out.println("\n=== EXECUȚIA PROGRAMULUI ===");

            // Facem deep copy al programului
            ProgramState copiedState = ctrl.copyProgramState(ctrl.getRepository().getCurrentProgram());
            IRepository tempRepo = new Repository(copiedState, ctrl.getRepository().getLogFilePath());
            Controller tempCtrl = new Controller(tempRepo);

            // Rulăm programul pe copia deep
            tempCtrl.allStep();

            // Afișăm rezultatul
            System.out.println("Rezultatul final al programului: " + copiedState.getOutput());

            alreadyRun = true;
        } catch (MyException | InterpreterException | IOException e) {
            System.out.println("Eroare: " + e.getMessage());
        }
    }
}
