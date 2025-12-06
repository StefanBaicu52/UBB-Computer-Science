bits 32               ; Assembling for the 32-bit architecture

global start          ; Entry point of the program
extern exit           ; External function declaration for exit
import exit msvcrt.dll; Importing exit from msvcrt.dll

segment data use32 class=data

a dw 01101101_11001100b
b dw 11100010_00011101b
c dd 0
    
segment code use32 class=code
start:

mov ebx,0 ;in registrul ebx vom calcula rezultatul

;bitii 0-2 ai lui C au valoarea 0
and ebx,11111111_11111111_11111111_11111000b ;fac bitii 0-2 din rezultat sa aiba valoarea 0

;bitii 3-5 ai lui C au valoarea 1
or ebx,00000000_00000000_00000000_00111000b ;fac bitii 3-5 din rezultat sa aiba valoarea 1

;bitii 6-9 ai lui C coincid cu bitii 11-14 ai lui A
mov ax,[a] ;ax=a
cwde ;eax=a
and eax,00000000_00000000_01111000_00000000b ;izolez bitii 11-14 a lui a
mov cl,5
ror eax,cl ;rotesc 5 pozitii spre dreapta
or ebx,eax ;pun bitii in rezultat

;bitii 10-15 ai lui C coincid cu bitii 1-6 ai lui B
mov ax,[b] ;ax=b
cwde ;eax=b
and eax,00000000_00000000_00000000_01111110b ;izolez bitii 1-6 a lui b
mov cl,9
rol eax,cl ;rotesc 9 pozitii spre stanga
or ebx,eax ;pun bitii in rezultat

;bitii 16-31 ai lui C au valoarea 1
or ebx,11111111_11111111_00000000_00000000b ;fac bitii 16-31 din rezultat sa aiba valoarea 1

mov [c],ebx ;pun valoarea din registru in variabila rezultat

  
    
    
    ; Exit the program
    push dword 0      ; Push exit code 0
    call [exit]       ; Call exit to terminate the program
