bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s times 100 db 0
    read_format db "%s", 0
    print_format db"afisare %s", 0

; our code starts here
segment code use32 class=code
    start:
        ; read word
        push dword s
        push dword read_format
        call[scanf]
        add esp, 2*4
        
        ;printf
        push dword s
        push dword print_format
        call [printf]
        add esp, 2*4
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
