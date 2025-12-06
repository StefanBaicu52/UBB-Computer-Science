bits 32           

global start

extern exit, fopen, fprintf, fclose, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    nume_fisier db "put.txt", 0    ; numele fisierului care va fi creat
    mod_acces db "w", 0      ; modul de deschidere a fisierului - w pentru scriere
    descriptor_fisier dd -1      ; variabila pentru descriptorul fisierului

    text db "aA@#G,", 0   ; textul ce l modific
    len_text equ $-text-1       ; lungimea

    contor_message db "Textul rezultat: %s", 0 ; mesaj pt a afisa textul modificat

segment code use32 class=code
    start:


        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0

        ; apelez functia fopen pentru a crea fisierul
        push dword mod_acces     
        push dword nume_fisier
        call [fopen]
        add esp, 4*2         ; eliberez parametrii de pe stiva

        mov [descriptor_fisier], eax ; salvam valoarea returnata de fopen in variabila descriptor_fisier

        ;verificam daca functia fopen a creat fisierul (daca EAX != 0)
        cmp eax, 0
        je final

        ;incepem inlocuirea caracterelor speciale cu 'X'
        ;parcurgem textul si inlocuim 
        lea esi, [text]               ; in ESI punem adresa textului
        mov ecx, len_text            ; Lungimea textului
        cld                          ; Clear DF (directia de parcurere(stanga->dreapta)

    inlocuire:
        lodsb                         ; in AL se pune caracterul din text

        ;vrificam daca caracterul este o litera mica 
        cmp al, 'a'                   ; Comparam cu 'a'
        jl  verificare_mare           ; Daca AL < 'a', jump  la verificare mare
        cmp al, 'z'                   ; Comparam cu 'z'
        jg  verificare_mare           ; Daca AL > 'z', jump la verificare mare
        ;ddaca e caracter intre 'a' si 'z', continuam fara schimbare
        jmp continui

    verificare_mare:
        ; Verificam daca caracterul este o litera mare ('A' - 'Z')
        cmp al, 'A'                   ; Comparam cu 'A'
        jl  verificare_cifre          ; Daca AL < 'A', jump la verificare cifre
        cmp al, 'Z'                   ; Comparam cu 'Z'
        jg  verificare_cifre          ; Daca AL > 'Z', jump la verificare cifre
        ;ddaca e caracter intre 'A' si 'Z', continuam fara schimbare
        jmp continui

    verificare_cifre:
        ;verificam daca caracterul este o cifra ('0' - '9')
        cmp al, '0'                   ; Comparam cu '0'
        jl  verificare_spatiu         ; Daca AL < '0', jump la verificare spatiu
        cmp al, '9'                   ; Comparam cu '9'
        jg  verificare_spatiu         ; Daca AL > '9', jumpla verificare spatiu
        ; Daca e caracter intre '0' si '9', continuam fara schimbare
        jmp continui

    verificare_spatiu:
        cmp al, ' '                   
        je  continui                  ; Daca e spaitiu, trecem la urmatorul caracter

    inlocuire_speciala:
        ; Daca caracterul este special , il inlocuim cu 'X'
        mov al, 'X'

    continui:
        mov [esi - 1], al             ; Punem caracterul procesat inapoi in text
        dec ecx                       ;scadem lungimea textului
        cmp ecx, 0                    ;verificam daca am parcurs tot textul
        jg inlocuire          ;daca mai avem caractere, continuam

        ; Scriem textul modificat in fisier folosind fprintf
        push dword text                ; Adresa textului modificat
        push dword [descriptor_fisier] ; Descriptorul fisierului
        call [fprintf]
        add esp, 4*2           ;Eliberam parametrii de pe stiva

        ; Afisam textul rezultat
        push dword text          ; Adresa textului modificat
        push dword contor_message      ; Mesajul pentru printf
        call [printf]         ; Apelam printf
        add esp, 4*2                   ; Eliberam parametrii de pe stiva

        ;inchidem fisierul
        push dword [descriptor_fisier]
        call [fclose]
        add esp, 4                     

    final:
         push    dword 0      
        call    [exit]  
