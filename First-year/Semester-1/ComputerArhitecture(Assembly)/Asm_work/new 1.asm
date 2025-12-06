section .data
    ; The initial data (bytes) to be sorted
    d db 56h, 3Ch, 34h, 2Bh, 1Ah, 15h, 12h, 07h  ; Example bytes

section .text
    global _start
_start:
    ; Step 1: Sorting the bytes using bubble sort

    mov ecx, 7          ; Outer loop counter: 7 iterations (one less than the number of bytes)
bubble_sort_outer:
    xor ebx, ebx        ; Inner loop counter (starting at 0)
    mov edx, ecx        ; Set the inner loop limit to the outer loop counter

bubble_sort_inner:
    ; Compare d[ebx] and d[ebx + 1]
    mov al, [d + ebx]
    mov ah, [d + ebx + 1]
    cmp al, ah          ; Compare d[ebx] and d[ebx + 1]
    jge no_swap         ; If d[ebx] >= d[ebx + 1], no swap needed

    ; Swap the bytes if needed
    xchg al, ah
    mov [d + ebx], al
    mov [d + ebx + 1], ah

no_swap:
    inc ebx             ; Move to the next byte
    dec edx             ; Decrement the inner loop counter
    jnz bubble_sort_inner

    dec ecx             ; Decrement outer loop counter
    jnz bubble_sort_outer

    ; Step 2: Finish the program (exit)
    mov eax, 1          ; Exit syscall number
    xor ebx, ebx        ; Status 0
    int 0x80            ; Make syscall
