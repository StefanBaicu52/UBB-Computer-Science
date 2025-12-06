bits 32

global start        

extern exit, fopen, read, write, close, printf  
import exit msvcrt.dll
import fopen msvcrt.dll
import read msvcrt.dll
import write msvcrt.dll
import close msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    nume_fisier_in db "put.txt", 0  ; numele fisierului de intrare
    nume_fisier_out db "out.txt", 0 ; numele fisierului de iesire
    mod_acces db "r", 0                     ; modul de deschidere a fisierului pentru citire
    mod_acces_out db "w", 0                 ; modul de deschidere a fisierului pentru scriere
    descriptor_fisier_in dd -1              ; descriptor pentru fisierul de intrare
    descriptor_fisier_out dd -1             ; descriptor pentru fisierul de iesire
    caracter_X db 'X', 0                    ; caracterul cu care inlocuim caracterele speciale

segment code use32 class=code
start:
    ; Se pune 0 in fiecare registru
    mov eax, 0
    mov ebx, 0 ; contor pentru caracterele citite

    ; Deschidem fisierul de intrare
    push dword 0    ; descriptorul fisierului de intrare
    push dword mod_acces
    push dword nume_fisier_in
    call [fopen]
    add esp, 4*3 ; eliberam parametrii de pe stiva
    
    mov [descriptor_fisier_in], eax ; salvam descriptorul fisierului de intrare
    
    ; Verificam daca fisierul de intrare a fost deschis cu succes
    cmp eax, 0
    je final ; daca fisierul nu a fost deschis, iesim

    ; Deschidem fisierul de iesire
    push dword 0    ; descriptorul fisierului de iesire
    push dword mod_acces_out
    push dword nume_fisier_out
    call [fopen]
    add esp, 4*3 ; eliberam parametrii de pe stiva

    mov [descriptor_fisier_out], eax ; salvam descriptorul fisierului de iesire
    
    ; Verificam daca fisierul de iesire a fost deschis cu succes
    cmp eax, 0
    je final ; daca fisierul nu a fost deschis, iesim

    ; Citim caractere din fisierul de intrare
    ; Folosim read pentru a citi un byte de fiecare data
citire_fisier:
    push dword 1    ; numarul de octeti de citit
    push dword [descriptor_fisier_in] ; descriptorul fisierului de intrare
    lea eax, [esp+4] ; buffer pentru citirea unui caracter
    call [read] ; citim un caracter in buffer
    add esp, 4*3 ; eliberam parametrii de pe stiva

    ; Daca am ajuns la sfarsitul fisierului, iesim
    cmp eax, 0
    je final

    ; Verificam daca caracterul este o litera (A-Z sau a-z) sau spatiu
    mov al, [esp+4] ; luam caracterul citit
    cmp al, 'a'  ; daca e mai mic decat 'a'
    jl inlocuire_caracter
    cmp al, 'z'  ; daca e mai mare decat 'z'
    jg inlocuire_caracter
    cmp al, 'A'  ; daca e mai mic decat 'A'
    jl inlocuire_caracter
    cmp al, 'Z'  ; daca e mai mare decat 'Z'
    jg inlocuire_caracter
    cmp al, ' '  ; daca este spatiu
    je inlocuire_caracter
    ; Daca este litera sau spatiu, scriem caracterul in fisier
    push dword 1     ; numarul de octeti de scris
    push dword [descriptor_fisier_out] ; descriptorul fisierului de iesire
    lea eax, [esp+4] ; buffer cu caracterul citit
    call [write] ; scriem caracterul in fisier
    add esp, 4*3 ; eliberam parametrii de pe stiva

    ; Continuam sa citim caracterul urmator
    jmp citire_fisier

inlocuire_caracter:
    ; Inlocuim caracterul cu 'X'
    mov al, [caracter_X] ; inlocuim cu 'X'
    push dword 1     ; numarul de octeti de scris
    push dword [descriptor_fisier_out] ; descriptorul fisierului de iesire
    lea eax, [esp+4] ; buffer cu caracterul 'X'
    call [write] ; scriem 'X' in fisierul de iesire
    add esp, 4*3 ; eliberam parametrii de pe stiva

    ; Continuam sa citim caracterul urmator
    jmp citire_fisier

final:
    ; Inchidem fișierele
    push dword [descriptor_fisier_in]
    call [close]
    add esp, 4

    push dword [descriptor_fisier_out]
    call [close]
    add esp, 4

    ; Terminam programul
    push dword 0
    call [exit]
