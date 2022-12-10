"""

"""

class Tabela:
    linhaPosicao = [['1','2','3'],['4','5','6'],['7','8','9']]


    def imprimirTabela(self):
        """
        imprimirTabela cria a tabela na qual ira ser jogado o jogo da velha
        """
        for linha in range(0, 3):
            for coluna in range(0, 3):
                print(f'[{self.linhaPosicao[linha][coluna]:3^}]', end=' ')
            print()



#        0123456789012  0
        ##############  1
        # 1 | 2 | 3  #  2
        #---|---|--- #  3
        # 4 | 5 | 6  #  4
        #---|---|--- #  5
        # 7 | 8 | 9  #  6
        ##############  7


