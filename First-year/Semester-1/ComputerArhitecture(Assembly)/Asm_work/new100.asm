bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fscanf,printf,scanf,fopen                ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fscanf msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fisier db 'cuvinte.txt',0
    mod_acces db 'r',0
    descriptor dd -1
    format db'%d',0
    mesaj1 db'l=',0
    L resb 1
    nr db 0
    contor db 0
    text resd 100
    lg $(text-1)/4
    

; our code starts here
segment code use32 class=code
    start:
    
    
        push dword nume_fisier
        push dword mod_acces
        call [fopen]
        add esp,8
    
         push dword mesaj1    ;citire L
         call [printf]
         add esp,4
         push dword L
         push format 
         call [scanf]
         add esp,8
         
         push dword text
         push dword 1
         push dword len                 ; citire fisier
         push dword descriptor
         call [fscanf]
         add esp,4*4
         
         mov [descriptor],eax
         
         mov eax,0
         mov ebx,[L]
         mov esi,[text]
         
         repeta
            lodsb
            cmp al,0
            je final
            cmp al,' '
            je gata_cuv
            add nr,1
        gata_cuv
            cmp nr,bl
            jne urmator
            add contor,1
        urmator 
            mov nr,0
         loop repeta 
             
            
         
         
         
         
        
         
        
         final
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
