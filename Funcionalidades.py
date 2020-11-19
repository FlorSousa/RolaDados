import random
class Funcionalidades:
    def __init__(self,stringVisor,obj):
        self.stringVisor = stringVisor
        self.listaValores = []
        self.obj = obj
    def Encaminha(self):
        for k in self.stringVisor:
            if k[0] == "D":
                self.Sortea(k)
            elif k[0] == "+" or k[0] == "-":
                self.Opera(k)
            else:
                self.Opera(int(k))
    
    def Sortea(self,dado):
        if len(dado) == 2:
            sorteado = random.randint(0,int(dado[1]))
            self.Opera(sorteado)
        else:
            num = int(dado[1]+dado[2])
            sorteado = random.randint(0, num)
            self.Opera(sorteado)
        
    def Opera(self,elemento):
        if len(self.listaValores) < len(self.stringVisor)-1:
            self.listaValores.append(str(elemento))
        else:
            self.listaValores.append(str(elemento))
            saida = ""
            for k in range(len(self.listaValores)):
                saida += self.listaValores[k]
            STRFinal= str(eval(saida))
            self.obj.Finaliza(STRFinal)
            
    def Limpar(self):
        self.stringVisor = ""
        self.listaValores = []