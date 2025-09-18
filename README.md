# ACC Assembly Simulator

Este repositório contém materiais para alunos praticarem **arquitetura de computadores** usando:
1. **Assembly hipotético de 1 operando (ACC)**
2. **Simulador em Python**

## Estrutura
- `*.asm` → Programas em assembly para máquina hipotética
- `*.py` → Simulador de CPU com acumulador
  - `cpu1.py` → versão básica  
  - `cpu2.py` → versão com flags e desvios (para preencher lacunas)

## Exercício
Implemente o programa que calcula:

Z←(X−Y+1)×(X+3)

E teste no simulador.

## Como rodar online
Você pode executar o simulador em qualquer ambiente Python.  
A forma mais simples é usar o compilador online do Programiz:

1. Acesse: [https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)
2. Copie e cole o conteúdo do arquivo `cpu2.py`.
3. Preencha as lacunas (marcadas como TODO no código).
4. Clique em **Run**.
5. Informe os valores de `X` e `Y` quando solicitado.
6. Observe o resultado do programa e o traço de execução.

> 💡 Dica: se o programa não mostrar nada, verifique se o arquivo contém no final:
> ```python
> if __name__ == "__main__":
>     main()
> ```

## Questões
- Complete as lacunas no simulador em Python.
- Discuta vantagens e desvantagens de uma arquitetura **de 1 operando (ACC) só com endereçamento direto** contra a arquitetura **de 1 operando (ACC) com endereçamento direto ou imediato.**
