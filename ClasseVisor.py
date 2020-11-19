from tkinter import*
class visor:
    def __init__(self,root):
        self.valor = ""
        self.saida = StringVar()
        self.saida.set(self.valor)
        self.inseridos = []
        Label(root,textvariable = self.saida,font=("Arial",16)).place(x=90,y=60)
    def mudaVisor(self,novo):
        if len(self.inseridos) <=0:
            if novo != "+":
               if novo != "-":
                    self.valor += novo
                    self.saida.set(self.valor)
                    self.inseridos.append(novo)
        else:
            if self.inseridos[len(self.inseridos)-1] == "+" or self.inseridos[len(self.inseridos)-1] == "-":
                if novo != "+" or novo != "-":
                    self.valor += novo
                    self.saida.set(self.valor)
                    self.inseridos.append(novo)
                    
            else:
                if novo == "+" or novo == "-":
                    self.valor += novo
                    self.saida.set(self.valor)
                    self.inseridos.append(novo)
                elif novo[0] != "D" and self.inseridos[len(self.inseridos)-1][0]!="D" :
                    self.valor += novo
                    self.saida.set(self.valor)
                    self.inseridos[len(self.inseridos)-1] =   self.inseridos[len(self.inseridos)-1] + novo
                      
                    
    def Finaliza(self,STR):
        self.valor = STR
        self.saida.set(self.valor)
    def Limpar(self):
        self.valor = ""
        self.saida.set(self.valor)
        self.inseridos = []
        #Se for o primeiro n aceita + ou -
        # Se o anterior for + ou - só aceita valores numericos 
        # Se o anterior for numerico so aceita + ou - ou numericos sem ser Dado