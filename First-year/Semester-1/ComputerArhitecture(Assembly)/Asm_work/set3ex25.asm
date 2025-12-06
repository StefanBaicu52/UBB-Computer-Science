bits 32               ; Assembling for the 32-bit architecture

global start          ; Entry point of the program
extern exit           ; External function declaration for exit
import exit msvcrt.dll; Importing exit from msvcrt.dll

segment data use32 class=data
;(a*a+b+x)/(b+b)+c*c
; a-word; b-byte; c-doubleword; x-qword

    a dw 1            
    b db 5      
    c dd 2                    
    x dq 14      

    
segment code use32 class=code
start:
    mov eax,0
    mov ecx,0
    mov ebx,0
    mov bx,[a]
    mov ax,[a]
    mul bx
    mov bx,ax
    
    mov al,0
    mov al,[b]
    mov ah,0
    add ax,bx
    mov dx,0
    mov edx,0
    mov ebx,0
    mov ebx,[x]
    mov ecx,[x+4]
    add ebx,eax
    
    mov al,0
    mov al,[b]
    mov ah,0
    mov dx,0
    mov edx,0
    add eax,eax
    mov ecx,0
    mov ecx,eax
    mov eax,0
    mov eax,ebx
    div ecx
    
    mov ebx,0
    mov ecx,0
    mov ebx , [c]
    mov ecx , [c]
    mul ebx
    
    add eax,ecx
    
    
    
    ; Exit the program
    push dword 0      ; Push exit code 0
    call [exit]       ; Call exit to terminate the program
