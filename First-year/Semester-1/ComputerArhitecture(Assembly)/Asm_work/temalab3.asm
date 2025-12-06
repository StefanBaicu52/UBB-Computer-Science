bits 32 

global start        

extern exit, printf, scanf            
import exit msvcrt.dll    
import printf msvcrt.dll    
import scanf msvcrt.dll    
    
segment data use32 class=data
    a dd 0
    b dd 0
    mesaj db "Rezultatul este", 0
    mesaja db "a = ", 0
    mesajb db "b = ", 0
    format db "%d", 0    ;numar intreg
    formath db "%x", 0   ;hexadecimal
    
segment code use32 class=code
    start:
        push dword mesaja
        call [printf]    ;afiseaza a=
        add esp, 4*1     
        
        push dword a        ;pune adresa a pe stiva
        push dword format   ;pune %d pt citire nr intreg 
        call [scanf]        ;citeste 
        add esp, 4*2
        
        push dword mesajb
        call [printf]      
        add esp, 4*1
        
        push dword b
        push dword format  
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        add eax, [b]
        push dword mesaj  ;pune pe stivă adresa mesajului rezultatul este
        push dword eax     ;pune pe stiva rezultatul
        push dword formath  ;pune formatul %x pt hexadecimal 
        call [printf]
        add esp, 4*3
        
        
        push    dword 0      
        call    [exit]     
