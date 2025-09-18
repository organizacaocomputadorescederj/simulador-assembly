class CPU:
    def __init__(self, mem_size=256):
        self.memory = [0] * mem_size    # Memória linear
        self.acc = 0                    # Acumulador
        self.pc = 0                     # Program Counter
        # Flags: Zero (Z), Negativo (N) 
        self.Z = 0
        self.N = 0
        self.running = True

    # ---------- Utilidades ----------
    def _set_flags_from_acc(self):
        """Atualiza Z e N a partir do ACC."""
        # TODO: Z=1 se acc == 0; N=1 se acc < 0
        # self.Z = ...
        # self.N = ...
        pass

    def _read_operand(self, token):
        """
        Retorna o valor de operando segundo o modo de endereçamento:
        - '#k'  => imediato k
        - 'addr' (ex.: '42') => modo direto, lê de memory[addr]
        """
        token = str(token).strip()
        if token.startswith('#'):
            # TODO: imediato
            # return int(token[1:])
            pass
        else:
            addr = int(token)
            # TODO: direto (valor = memory[addr])
            # return self.memory[addr]
            pass

    def _write_memory(self, addr, value):
        # TODO: armazenar valor em memória (endereçamento direto)
        pass

    # ---------- ISA de 1 operando ----------
    def LDA(self, operand):
        # ACC <- M[addr] ou ACC <- #imm
        val = self._read_operand(operand)
        # TODO: carregar no ACC e atualizar flags
        pass

    def STA(self, operand):
        # M[addr] <- ACC (somente modo direto faz sentido para STA)
        addr = int(operand)
        # TODO: gravar ACC na memória
        pass

    def ADD(self, operand):
        val = self._read_operand(operand)
        # TODO: acc = acc + val; 
        pass

    def SUB(self, operand):
        val = self._read_operand(operand)
        pass

    def MUL(self, operand):
        val = self._read_operand(operand)
        # TODO: multiplicação; atualizar flags Z,N;  
        pass

    def DIV(self, operand):
        val = self._read_operand(operand)
        if val == 0:
            print("Erro: divisão por zero")
            self.running = False
            return
        # TODO: divisão inteira; atualizar flags; 
        pass

    def NEG(self, _unused):
        # TODO: acc = -acc; atualizar flags; 
        pass

    def BZ(self, target):
        # Branch if Zero
        # TODO: se Z==1 então pc = int(target) (salto absoluto simples)
        pass

    def BN(self, target):
        # Branch if Negative
        # TODO: se N==1 então pc = int(target)
        pass

    def JMP(self, target):
        # Salto incondicional
        # TODO: pc = int(target)
        pass

    def HLT(self, _unused):
        self.running = False

    # ---------- Carregamento e Execução ----------
    def load_program(self, program, start=0):
        """
        program: lista de strings, cada string é "OP opnd" ou "OP"
        Exemplos:
          "LDA 10"        ; ACC <- M[10]
          "ADD #3"        ; ACC <- ACC + 3
          "STA 12"        ; M[12] <- ACC
          "BZ  15"        ; se Z=1, PC <- 15
          "HLT"
        """
        self.memory = [0] * len(self.memory)  # limpa memória de dados
        self.program = program[:]              # armazena programa separadamente
        self.pc = start
        self.running = True
        self.acc = 0
        self.Z = self.N = self.C = 0

    def step(self):
        if not self.running:
            return
        if self.pc < 0 or self.pc >= len(self.program):
            print("PC fora do programa, encerrando.")
            self.running = False
            return

        line = self.program[self.pc].strip()
        self.pc += 1  # PC avança por padrão; saltos irão sobrescrever

        if not line or line.startswith(';'):
            return

        parts = line.split()
        op = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else None

        # Despacho de instrução
        if   op == 'LDA': self.LDA(operand)
        elif op == 'STA': self.STA(operand)
        elif op == 'ADD': self.ADD(operand)
        elif op == 'SUB': self.SUB(operand)
        elif op == 'MUL': self.MUL(operand)
        elif op == 'DIV': self.DIV(operand)
        elif op == 'NEG': self.NEG(operand)
        elif op == 'BZ':  self.BZ(operand)
        elif op == 'BN':  self.BN(operand)
        elif op == 'JMP': self.JMP(operand)
        elif op == 'HLT': self.HLT(operand)
        else:
            print(f"Instrução desconhecida: {op}")
            self.running = False

    def run(self, max_steps=1000, trace=False):
        steps = 0
        while self.running and steps < max_steps:
            if trace:
                print(f"PC={self.pc:03d} ACC={self.acc}")
            self.step()
            steps += 1
        if steps >= max_steps:
            print("Execução interrompida por limite de passos.")

def main():
    # Instancia a CPU
    cpu = CPU()

    # --- Entradas do problema ---
    X = int(input("Digite o valor de X: "))
    Y = int(input("Digite o valor de Y: "))

    # Grava os valores de entrada na memória
    cpu.memory[2] = X  # endereço 0x02 guarda X
    cpu.memory[3] = Y  # endereço 0x03 guarda Y

    # --- Programa: Z = (X - Y + 1) * (X + 3) ---
    program = [
        "LDA 2",    # ACC <- X
        "SUB 3",    # ACC <- X - Y
        "ADD #1",   # ACC <- X - Y + 1
        "STA 4",    # T1 <- ACC (M[4])

        "LDA 2",    # ACC <- X
        "ADD #3",   # ACC <- X + 3
        "STA 5",    # T2 <- ACC (M[5])

        "LDA 4",    # ACC <- T1
        "MUL 5",    # ACC <- T1 * T2
        "STA 1",    # Z <- ACC (M[1])

        "HLT"       # fim
    ]

    # Carrega o programa e executa com traço
    cpu.load_program(program)
    cpu.run(trace=True)

    # --- Resultado ---
    Z = cpu.memory[1]
    print(f"\nResultado final: Z = {Z}")
    print(f"(Valor esperado: (X - Y + 1) * (X + 3) = {(X - Y + 1) * (X + 3)})")

if __name__ == "__main__":
    main()

