import readline

class Jodador:
    ja_fez_sua_jogada: bool = False

    def FazASuaJogada(self):
        self.ja_fez_sua_jogada = True
        return 'O'

    def VerificarJaFezJogada(self):
        if(self.ja_fez_sua_jogada == True):
            return True
        else:
            self.ja_fez_sua_jogada = False
            return False