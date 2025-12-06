bits 32
global start

extern exit, printf, scanf, fopen, fprintf, fclose
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    file_name db "out.txt", 0
    mode db "w", 0
    fd dd 0
    fmt_n db "%d", 0
    fmt_s db "%s", 0
    msg_n db "n = ", 0
    msg_s db "word = ", 0
    n dd 0
    wordd times 255 db 0

segment code use32 class=code
start:
    push dword mode
    push dword file_name
    call [fopen]
    add esp, 8
    mov [fd], eax

read_loop:
    push dword msg_n
    call [printf]
    add esp, 4

    push dword n
    push dword fmt_n
    call [scanf]
    add esp, 8

    mov eax, [n]
    cmp eax, 0
    je end_prog

    push dword msg_s
    call [printf]
    add esp, 4

    push dword wordd
    push dword fmt_s
    call [scanf]
    add esp, 8

    push dword wordd
    push dword fmt_s
    push dword [fd]
    call [fprintf]
    add esp, 12

    jmp read_loop

end_prog:
    push dword [fd]
    call [fclose]
    add esp, 4

    push dword 0
    call [exit]
