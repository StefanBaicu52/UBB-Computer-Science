bits 32 

global start        

extern exit              
import exit msvcrt.dll    

segment data use32 class=data
    a db -2,1,3,-3        ; Șirul A
    lga equ $-a            ; Lungimea șirului A
    b db 4,5,-6,7          ; Șirul B
    lgb equ $-b            ; Lungimea șirului B
    lgr equ $-a            ; Lungimea maximă pentru R (în funcție de A)
    r times lgr db 0       ; Rezervăm un șir pentru R
segment code use32 class=code
    start:
        ; Parcurgem șirul A
        mov ecx, lga        ; Punem lungimea șirului A în ecx
        jecxz parcurgereb   ; Dacă șirul A este gol, trecem la șirul B
        mov esi, 0          ; Indice pentru șirul A
        mov edi, 0          ; Indice pentru șirul R
    repeta1:
        mov al, [a + esi]   ; Încărcăm un element din A
        cmp al, 0           ; Comparam cu 0
        jle finalepeta1      ; Dacă elementul este <= 0 (negativ sau zero), sărim peste el
        test al, 1           ; Verificăm dacă elementul este impar (ultimul bit)
        jz finalepeta1       ; Dacă nu este impar, sărim peste el
        mov [r + edi], al    ; Dacă este impar și pozitiv, îl adăugăm în R
        inc edi              ; Incrementăm indicele pentru R
    finalepeta1:
        inc esi              ; Trecem la următorul element din A
        loop repeta1         ; Repetăm pentru toate elementele din A

    parcurgereb:
        ; Parcurgem șirul B
        mov ecx, lgb        ; Punem lungimea șirului B în ecx
        jecxz final          ; Dacă șirul B este gol, trecem la final
        mov esi, 0          ; Indice pentru șirul B
    repeta2:
        mov al, [b + esi]   ; Încărcăm un element din B
        cmp al, 0           ; Comparam cu 0
        jle finalepeta2      ; Dacă elementul este <= 0 (negativ sau zero), sărim peste el
        test al, 1           ; Verificăm dacă elementul este impar (ultimul bit)
        jz finalepeta2       ; Dacă nu este impar, sărim peste el
        mov [r + edi], al    ; Dacă este impar și pozitiv, îl adăugăm în R
        inc edi              ; Incrementăm indicele pentru R
    finalepeta2:
        inc esi              ; Trecem la următorul element din B
        loop repeta2         ; Repetăm pentru toate elementele din B

    final:
        ; Terminăm programul
        push dword 0
        call [exit]         ; Ieșim din program
nu