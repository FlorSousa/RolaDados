class NumerBotao:
    def __init__(self,Numero,Button,root,x,y,visor):
        self.x = x
        self.y = y
        self.text = str(Numero)
        self.visor = visor
        Button(root,text= self.text,font=("Arial",20),width=3,command = lambda: self.InsereNoVisor()).place(x=self.x+85,y=self.y+30)
    def InsereNoVisor(self):
        self.visor.mudaVisor(self.text)