from tema6functii import *

while True:
    n = input("Choose a command group (a/b/c/d/e) or 'f' to exit: ").strip().lower()
    if n == "f":
        print("Exiting program.")
        break
    elif n in ["a", "b", "c", "d", "e"]:
        if n!="e":
            command = input("Enter your command: ").strip()
        if n == "a":
            a(command)
        elif n == "b":
            b(command)
        elif n == "c":
            c(command)
        elif n == "d":
            d(command)
        elif n == "e":
            undo_last_action()
    else:
        print("Invalid choice. Please choose a, b, c, d, f, or e.")
