bits 32               ; Assembling for the 32-bit architecture

global start          ; Entry point of the program
extern exit           ; External function declaration for exit
import exit msvcrt.dll; Importing exit from msvcrt.dll

segment data use32 class=data
;(a*a+b+x)/(b+b)+c*c
; a-word; b-byte; c-doubleword; x-qword

     a db 2,1,3,3,4,2,6       ; Array `a`
    lga equ $-a              ; Length of `a`
    b db 4,5,7,6,2,1         ; Array `b`
    lgb equ $-b              ; Length of `b`
    lg equ $-a               ; General length for `r`
    r times lg db 0          ; Result array `r`, initialized with zeros   

    
segment code use32 class=code
start:
   
        mov ecx, lgb             ; Încarcă lungimea vectorului `b` în registrul ECX (contor pentru buclă).
        jecxz parcurgerea        ; Dacă ECX (lungimea lui `b`) este zero, sare la eticheta `parcurgerea`.
        mov esi, lgb             ; Încarcă lungimea vectorului `b` în registrul ESI (index pentru `b`).
        sub esi, 1               ; Ajustează ESI pentru a indica ultimul element al lui `b` (indexare de la zero).
        mov edi, 0               ; Inițializează EDI cu 0, indexul pentru vectorul `r`.

        repeta1:
        mov al, [b+esi]          ; Încarcă elementul curent al lui `b` în registrul AL.
        mov [r+edi], al          ; Stochează valoarea din AL în poziția curentă din `r`.
        dec esi                  ; Decrementează ESI pentru a trece la elementul precedent din `b`.
        inc edi                  ; Incrementează EDI pentru a trece la următoarea poziție din `r`.
        loop repeta1             ; Repetă bucla până când ECX devine zero.

        parcurgerea:
        mov ecx, lga             ; Încarcă lungimea vectorului `a` în registrul ECX (contor pentru buclă).
        jecxz final              ; Dacă ECX (lungimea lui `a`) este zero, sare la eticheta `final`.
        mov esi, 0               ; Inițializează ESI cu 0, pentru a începe de la primul element din `a`.

        repeta2:
        mov al, [a+esi]          ; Încarcă elementul curent al lui `a` în registrul AL.
        test al, 000000001b      ; Testează dacă bitul cel mai puțin semnificativ (LSB) este 1 (verificare pentru număr impar).
        jnz cazimpar               ; Dacă LSB este 1 (numărul este impar), sare la eticheta `cazpar`.
        jmp finalrepeta2         ; Dacă numărul este par, sare la `finalrepeta2`.

        cazimpar:
        mov al, [a+esi]          ; Încarcă din nou elementul impar din `a` în registrul AL.
        mov [r+edi], al          ; Stochează valoarea din AL în poziția curentă din `r`.
        inc edi                  ; Incrementează EDI pentru a trece la următoarea poziție din `r`.

        finalrepeta2:
        inc esi                  ; Incrementează ESI pentru a trece la următorul element din `a`.
        loop repeta2             ; Repetă bucla până când ECX devine zero.

        final:
        push    dword 0         
        call    [exit]           
