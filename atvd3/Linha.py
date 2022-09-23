#Davi Pereira Bergamin 169753
#Felipe Araujo Santos Pinto 169401
#Leonardo Rogelio da Silva 177346

class Linha:
  def __init__(self):
    self.dados = []

  def append(self,novo):
    if type(novo) is list:
      self.dados+=novo
    else:
      self.dados += [novo]

  def __len__(self):
    return len(self.dados)

  def index(self,val):
    return self.dados.index(val)

  def __str__(self):
    return str(self.dados)
    
  def __repr__(self):
    return str(self.dados)

  def __contains__(self, v):
    return v in self.dados


      