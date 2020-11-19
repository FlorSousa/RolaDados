class botaoDado:
    def __init__(self,NumeroLados,Button,root,x,y,Visor):
        self.x = x
        self.y = y
        self.text = "D"+str(NumeroLados)
        self.visor = Visor
        Button(root,text= self.text,font=("Arial",20),width=3,command=lambda : self.InsereNoVisor()).place(x=self.x+30,y=self.y)
    
    def InsereNoVisor(self):
        self.visor.mudaVisor(self.text)