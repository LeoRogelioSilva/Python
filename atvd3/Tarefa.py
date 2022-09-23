from Tabela import Tabela
from TabelaBD import TabelaBD
from Linha import Linha


teste = Tabela()
# deve ser criada uma tabela vazia.
# por outro lado, se for passado no construtor o nome de um arquivo,
# a tabela deve ser carregada deste arquivo.
# Veja o exemplo:
teste = Tabela("carros.txt")
print(teste)


teste.writeFile("saida.txt")

teste = Tabela("saida.txt")
print(teste)

candidatos = TabelaBD("candidados_dep_fed.txt")

result = candidatos.conta("Partido")
print(result)