; Agora as constantes não estão na memória
; Usamos imediato para 2 e 4

    LDA 0x10     ; ACC <- P
    SUB 0x11     ; ACC <- P - Q
    ADD #2       ; ACC <- P - Q + 2
    STA 0x13     ; Temp1 <- ACC

    LDA 0x10     ; ACC <- P
    ADD #4       ; ACC <- P + 4
    STA 0x14     ; Temp2 <- ACC

    LDA 0x13     ; ACC <- Temp1
    MUL 0x14     ; ACC <- Temp1 * Temp2
    STA 0x12     ; W <- ACC

    HLT
