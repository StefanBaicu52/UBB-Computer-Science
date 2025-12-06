bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;a - byte, b - word, c - double word, d - qword - Unsigned representation
    ;(a + b + c) - (d + d) + (b + c)
    a db 5
    b dw 10
    c dd 20
    d dq 3

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al,[a]
        mov ah,0
        mov dx,0
        mov edx,0
        
        mov eax,0
        mov ebx,eax
        mov ax,[b]
        mov dx,0
        mov edx,0
        add ebx,eax
        add ebx,eax
        
        mov eax,0
        mov eax,[c]
        add ebx,eax
        add ebx,eax
        
        MOV ECX,[d]
        MOV EBX,[d+4]
        ADD ECX,ECX
        ADD EBX,EBX
         
        sub ebx,ecx
        
       
        
       
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
