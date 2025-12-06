bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 0702090Ah, 0B0C0304h, 05060108h  ; initial array of doublewords
    lga equ ($-a)/3        ; number of elements (3 doublewords)
    r times 6 db 0         ; array to store 6 sorted bytes
; our code starts here
segment code use32 class=code
    
        ;An array of doublewords, where each doubleword contains 2 values on a word (unpacked, so each nibble is preceded by a 0) is given. 
        ;Write an asm program to create a new array of bytes which contain those values (packed on a single byte), 
        ;arranged in an ascending manner in memory, these being considered signed numbers.
            ;Example:
            ;for the initial array:
            ;0702090Ah, 0B0C0304h, 05060108h  
            ;the following should be obtained:
            ;72h, 9Ah, 0BCh, 34h, 56h, 18h 
            ;which arranged in an ascending manner will give:
            ;9Ah, 0BCh, 18h, 34h, 56h, 72h
    

    start:
        ; Load the address of array 'a' into ESI
        mov esi, a
        ; Load the number of doublewords (3) into ECX
        mov ecx, lga
        ; Clear the direction flag
        cld

        ; Step 1: Extract nibbles (4 bits) and store as bytes
        mov edi, r         ; Load the address of the 'r' array into EDI
        xor edx, edx       ; Clear EDX (used as a temporary register)

        extract_nibbles:
            ; Load a doubleword from array 'a' into EAX
            mov eax, [esi]
            
            ; Extract the upper nibble of the first word and store it in the byte array
            mov dl, al        ; Move the lower byte of EAX into DL
            and dl, 0F0h      ; Mask the upper nibble (keeping the upper nibble)
            shr dl, 4         ; Shift it to the lower nibble
            mov [edi], dl     ; Store it in the result array
            inc edi           ; Move to the next byte in the result array

            ; Extract the lower nibble of the first word and store it in the byte array
            mov dl, al        ; Move the lower byte of EAX into DL again
            and dl, 0Fh       ; Mask the lower nibble (keeping only the lower nibble)
            mov [edi], dl     ; Store it in the result array
            inc edi           ; Move to the next byte in the result array

            ; Repeat for the second byte of the doubleword (AH and AL)
            mov dl, ah
            and dl, 0F0h
            shr dl, 4
            mov [edi], dl
            inc edi

            mov dl, ah
            and dl, 0Fh
            mov [edi], dl
            inc edi

            ; Repeat for the third byte of the doubleword (DH and DL)
            mov dl, bh
            and dl, 0F0h
            shr dl, 4
            mov [edi], dl
            inc edi

            mov dl, bh
            and dl, 0Fh
            mov [edi], dl
            inc edi

            ; Repeat for the next element in the array
            add esi, 4        ; Move to the next doubleword
            loop extract_nibbles

        ; Step 2: Sort the byte array in ascending order
        ; Bubble Sort Algorithm (simple for demonstration purposes)
        mov ecx, 6             ; Number of elements in array 'r'
        dec ecx                ; ECX = 5 (index of the last element)

        sort_loop:
            xor edx, edx       ; Clear EDX (used for comparison)
            mov esi, r         ; Load the address of the byte array into ESI
            mov ebx, ecx       ; Set EBX = ECX (outer loop counter)

            inner_sort_loop:
                mov al, [esi]  ; Load current byte
                mov dl, [esi+1] ; Load next byte
                cmp al, dl      ; Compare the two bytes
                jbe no_swap     ; If AL <= DL, no swap needed

                ; Swap the bytes
                xchg al, dl
                mov [esi], al   ; Store the swapped byte
                mov [esi+1], dl  ; Store the swapped byte
            no_swap:
                inc esi         ; Move to the next byte
                dec ebx
                jnz inner_sort_loop ; Repeat for the next pair of bytes

            dec ecx               ; Decrease outer loop counter
            jnz sort_loop         ; Repeat the outer loop



            ; exit(0)
            push    dword 0      ; push the parameter for exit onto the stack
            call    [exit]       ; call exit to terminate the program
