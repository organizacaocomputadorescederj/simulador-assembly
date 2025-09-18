; Calcula W = (P - Q + 2) * (P + 4)
; Dados:
;   P em 0x10
;   Q em 0x11
;   W em 0x12
;   Constantes: 2 em 0x15, 4 em 0x16
;   Temporários: 0x13, 0x14

    LDA 0x10     ; ACC <- P
    SUB 0x11     ; ACC <- P - Q
    ADD 0x15     ; ACC <- P - Q + 2
    STA 0x13     ; Temp1 <- ACC

    LDA 0x10     ; ACC <- P
    ADD 0x16     ; ACC <- P + 4
    STA 0x14     ; Temp2 <- ACC

    LDA 0x13     ; ACC <- Temp1
    MUL 0x14     ; ACC <- Temp1 * Temp2
    STA 0x12     ; W <- ACC

    HLT
