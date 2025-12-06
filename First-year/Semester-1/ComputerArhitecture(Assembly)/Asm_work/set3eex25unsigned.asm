bits 32               ; Assembling for the 32-bit architecture

global start          ; Entry point of the program
extern exit           ; External function declaration for exit
import exit msvcrt.dll; Importing exit from msvcrt.dll

segment data use32 class=data
;(a*a+b+x)/(b+b)+c*c
; a-word; b-byte; c-doubleword; x-qword

    a dw 100          
    b db 5     
    c dd 49                    
    x dq -27005     

    
segment code use32 class=code
start:
    mov eax,0
    mov ecx,0
    mov ebx,0
    mov ax,[a]
    imul ax 
    push dx
    push ax
    pop ebx;a*a
    
    mov eax,0
    mov al,0
    mov al,[b]
    cbw ;signed conversion from al to ax
    cwd
    cwde
    adc eax,ebx;;a*a+b= 
    cdq
    mov ebx,0
    mov ebx,[x]
    mov ecx,[x+4]; ECX:EBX =x
    add ebx,eax
    adc ecx,0 ;ECX:EBX= (a*a+b+x)
    
    mov eax,0
    mov al,0
    mov al,[b]
    cbw
    cwd
    cwde
    cdq
    add eax,eax
    push eax ;EAX: b+b 
    mov eax,0
    mov eax,ebx
    mov edx,ecx ;EDX:EAX //ECX
    pop ecx
    idiv ecx
    ;EAX: (a*a+b+x)/(b+b)
    
    mov ecx,eax ;(a*a+b+x)/(b+b)
    
    mov ebx , [c]
    
    imul ebx; EDX:EAX
    
    add eax,ecx
    adc edx,0
    
    
    
    ; Exit the program
    push dword 0      ; Push exit code 0
    call [exit]       ; Call exit to terminate the program
