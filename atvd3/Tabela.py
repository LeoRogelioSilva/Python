#Davi Pereira Bergamin 169753
#Felipe Araujo Santos Pinto 169401
#Leonardo Rogelio da Silva 177346

from copy import copy, deepcopy
from Linha import Linha
import json

class Tabela:
  cabecalho = Linha()
  dados = []

  def __init__(self, arq=""):
    if arq != "":
        arq_open = open((arq), 'r+', encoding="utf8")
        self.cabecalho = Linha()
        self.cabecalho.append(json.loads(arq_open.readline().replace("\'","\"")))
        self.dados=[]
        todas_linhas = arq_open.readlines()
        for linha in todas_linhas:
            self.addLinha(json.loads(linha.replace("\'","\"")))            
    else: 
        self.cabecalho = Linha()
        self.dados=[]


  def add_cabecalho(self, cab):
    self.cabecalho.append(cab)

  def addLinha(self,novo):
    if len(novo) != len(self.cabecalho):
      print("tamanho da linha incompatível")
    else:
      self.dados.append(deepcopy(novo))

  def ordena_por(self, valor):
    if not valor in self.cabecalho:
      print("valor para ordenação inválido")
      return
    coluna = self.cabecalho.index(valor)
    self.dados.sort(key=lambda x: x.dados[coluna])

  def __len__(self):
      return len(self.dados)

  def writeFile(self, arq):
      file = open(arq, "w+", encoding="utf8")
      s = ""
      s+= str(self.cabecalho) +"\n"
      for dado in self.dados:
        s+=dado.__repr__()+"\n"
      
      file.write(s)
      

  def __str__(self):
    s = ""
    s+= str(self.cabecalho) +"\n"
    s+="------------------\n"
    for dado in self.dados:
      s+=str(dado)+"\n"
    
    return s