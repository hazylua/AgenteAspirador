# Os estados possíveis de um agente podem ser mapeados por hashing.
Estados = {'0': {'a': '1', 'b': '0', 'c': '-1'},
           '1': {'a': '2', 'b': '0', 'c': '0'},
           '2': {'a': '0', 'b': '0', 'c': '1'}}
print(Estados)
Posicao = '0'
Cadeia = '0'
while len(Cadeia) != 0:
    Cadeia = input()
    for acao in Cadeia:
        Posicao = Estados[Posicao][acao]
        if(Posicao == '-1'):
            print("Impossível.")
            break
    print(Posicao)
    Posicao = '0'
