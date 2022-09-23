from Tabela import Tabela
from Linha import Linha

class TabelaBD(Tabela):
        
    def conta(self, valor):
        if valor in self.cabecalho:
            resultado = Tabela()
            resultado.add_cabecalho([valor,"numero"])
            dicionario = {}
            i = self.cabecalho.index(valor)
            for linha in self.dados:
                if linha[i] in dicionario:
                    dicionario[linha[i]]+=1
                else:
                    dicionario[str(linha[i])] = 1
            for linha in dicionario:
                arr = [linha, dicionario[linha]]
                linha_tabela = Linha()
                linha_tabela.append(arr)
                resultado.addLinha(linha_tabela)
            resultado.ordena_por("numero")
            return resultado
            
