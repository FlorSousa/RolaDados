from tkinter import*
from ClasseBotaoDado import*
from ClasseVisor import*
from ClasseNumeroBotao import*
from Funcionalidades import*
root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
root.title("Rola Dados")

def InsereVisor(seletor):
    Visor.mudaVisor(seletor)
    
def Passa2Fucionalidades():
    Func = Funcionalidades(Visor.inseridos,Visor)
    Func.Encaminha()

def limpar():
    Visor.Limpar()
    
Visor = visor(root)
D20 = botaoDado(20,Button,root,90,200,Visor)
D12 = botaoDado(12,Button,root,150,200,Visor)
D10 = botaoDado(10,Button,root,210,200,Visor)
D8 = botaoDado(8,Button,root,270,200,Visor)
D6 = botaoDado(6,Button,root,150,260,Visor)
D4 = botaoDado(4,Button,root,210,260,Visor)
B0 = NumerBotao(0,Button,root,0,315,Visor)
B1 =  NumerBotao(1,Button,root,60,315,Visor)
B2 =  NumerBotao(2,Button,root,120,315,Visor)
B3 = NumerBotao(3,Button,root,180,315,Visor)
B4 = NumerBotao(4,Button,root,240,315,Visor)
B5 = NumerBotao(5,Button,root,0,375,Visor)
B6 = NumerBotao(6,Button,root,60,375,Visor)
B7 = NumerBotao(7,Button,root,120,375,Visor)
B8 = NumerBotao(8,Button,root,180,375,Visor)
B9 = NumerBotao(9,Button,root,240,375,Visor)
BtnSoma = Button(root,text= "+",font=("Arial",20),width=3,command = lambda:InsereVisor("+")).place(x=300,y=260)
BtnSoma = Button(root,text= "-",font=("Arial",20),width=3,command = lambda:InsereVisor("-")).place(x=120,y=260)
BtnResult = Button(root,text="ROLAR",font=("Arial",20),width=10, command = lambda:Passa2Fucionalidades()).place(x=160,y=130)
BtnLimpar = Button(root,text="Limpar", font=("Arial",12),command = lambda:limpar()).pack()
root.mainloop()