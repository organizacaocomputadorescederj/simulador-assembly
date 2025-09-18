
class CPU:
    def __init__(self, mem_size=256):
        self.memory = [0] * mem_size    # Memória linear
        self.acc = 0                    # Acumulador
        self.pc = 0                     # Contador de instruções (CI)
        # Flags: Zero (Z), Negativo (N)
        self.Z = 0
        self.N = 0
        self.running = True

    # ---------- Utilidades ----------
    def _set_flags_from_acc(self):
        """Atualiza Z e N a partir do ACC."""
        # TODO: Z deve ser 1 se ACC == 0, caso contrário 0
        #       N deve ser 1 se ACC < 0, caso contrário 0
        pass

    def _read_operand(self, token):
        """
        Retorna o valor do operando:
        - '#k'  => imediato k
        - 'addr' => direto, lê de memory[addr]
        """
        token = str(token).strip()
        if token.startswith('#'):
            # TODO: retornar o valor imediato (int(token[1:]))
            pass
        else:
            addr = int(token)
            # TODO: retornar o valor em memória no endereço addr
            pass

    def _write_memory(self, addr, value):
        # TODO: gravar value em self.memory[int(addr)]
        pass

    # ---------- ISA ----------
    def LDA(self, operand):
        # TODO: carregar operando em ACC e atualizar flags
        pass

    def STR(self, operand):
        # TODO: armazenar ACC no endereço indicado
        pass

    def ADD(self, operand):
        # TODO: somar operando ao ACC e atualizar flags
        pass

    def SUB(self, operand):
        # TODO: subtrair operando do ACC e atualizar flags
        pass

    def MUL(self, operand):
        # TODO: multiplicar ACC pelo operando e atualizar flags
        pass

    def DIV(self, operand):
        # TODO: divisão inteira do ACC pelo operando (tratar divisão por zero)
        pass

    def NEG(self, _unused):
        # TODO: inverter o sinal do ACC e atualizar flags
        pass

    def JZ(self, target):
        # TODO: se Z == 1, pc deve receber int(target)
        pass

    def JP(self, target):
        # TODO: se ACC > 0, pc deve receber int(target)
        pass

    def JN(self, target):
        # TODO: se N == 1, pc deve receber int(target)
        pass

    def JMP(self, target):
        # TODO: salto incondicional: pc recebe int(target)
        pass

    def HLT(self, _unused):
        self.running = False

    # ---------- Carregamento e Execução ----------
    def load_program(self, program, start=0):
        self.program = program[:]             # armazena programa
        self.pc = start
        self.running = True
        self.acc = 0
        self.Z = self.N = 0
        # não zere a memória aqui, ou senão regrave X, Y antes de rodar

    def step(self):
        if not self.running:
            return
        if self.pc < 0 or self.pc >= len(self.program):
            print("PC fora do programa, encerrando.")
            self.running = False
            return

        line = self.program[self.pc].strip()
        self.pc += 1  # PC avança por padrão

        if not line or line.startswith(';'):
            return

        parts = line.split()
        op = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else None

        if   op == 'LDA': self.LDA(operand)
        elif op == 'STR': self.STR(operand)
        elif op == 'ADD': self.ADD(operand)
        elif op == 'SUB': self.SUB(operand)
        elif op == 'MUL': self.MUL(operand)
        elif op == 'DIV': self.DIV(operand)
        elif op == 'NEG': self.NEG(operand)
        elif op == 'JZ':  self.JZ(operand)
        elif op == 'JP':  self.JP(operand)
        elif op == 'JN':  self.JN(operand)
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
    cpu = CPU()

    # --- Entradas ---
    X = int(input("Digite o valor de X: "))
    Y = int(input("Digite o valor de Y: "))

    cpu.memory[2] = X  # endereço 2 guarda X
    cpu.memory[3] = Y  # endereço 3 guarda Y

    # --- Programa: Z = (X - Y + 1) * (X + 3) ---
    program = [
        "LDA 2",    # ACC ← X
        "SUB 3",    # ACC ← X - Y
        "ADD #1",   # ACC ← X - Y + 1
        "STR 4",    # T1 ← ACC

        "LDA 2",    # ACC ← X
        "ADD #3",   # ACC ← X + 3
        "STR 5",    # T2 ← ACC

        "LDA 4",    # ACC ← T1
        "MUL 5",    # ACC ← T1 × T2
        "STR 1",    # Z ← ACC

        "HLT"
    ]

    cpu.load_program(program)
    cpu.run(trace=True)

    # --- Resultado ---
    Z = cpu.memory[1]
    print(f"\nResultado final: Z = {Z}")
    print(f"(Esperado: (X - Y + 1) * (X + 3) = {(X - Y + 1) * (X + 3)})")


if __name__ == "__main__":
    main()

