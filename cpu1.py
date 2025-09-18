class CPU:
    def __init__(self):
        self.memory = [0] * 256
        self.accumulator = 0
    
    def load_to_memory(self, value, address):
        self.memory[address] = value
    
    def fetch(self, address):
        return self.memory[address]
    
    def load_to_accumulator(self, value):
        self.accumulator = value
    
    def execute(self, op, mem_address):
        memory_value = self.fetch(mem_address)
        if op == 'add':
            self.accumulator += memory_value
        elif op == 'sub':
            self.accumulator -= memory_value
        elif op == 'mul':
            self.accumulator *= memory_value
        elif op == 'div':
            if memory_value != 0:
                self.accumulator //= memory_value
            else:
                print("Erro: Divisão por zero")
        elif op == 'neg':
            self.accumulator = -self.accumulator
    
    def run(self):
        initial_value = int(input("Digite o valor inicial para o acumulador: "))
        self.load_to_accumulator(initial_value)
        mem_address = int(input("Digite o endereço de memória: "))
        op = input("Escolha a operação (add, sub, mul, div, neg): ")
        self.execute(op, mem_address)
        print(f'Resultado no acumulador = {self.accumulator}')

if __name__ == "__main__":
    cpu = CPU()
    cpu.run()
