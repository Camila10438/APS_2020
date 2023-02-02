from tkinter import *
from tkinter import ttk
import coordenadas as cd
import webbrowser
import math
import os

def printlin(txt):
    print('\n' * os.get_terminal_size().lines)
    print(txt)

janela = Tk()
janela.title('APS')
janela.geometry("1000x650")

janela.resizable(width=False, height=False)
nb = ttk.Notebook(janela)
nb.place(x = 0, y = 0, width = 1000, height = 650)

tb0 = Frame(nb)
tb1 = Frame(nb)
tb2 = Frame(nb)
tb3 = Frame(nb)
tb4 = Frame(nb)
tb5 = Frame(nb)
tb6 = Frame(nb)
tb7 = Frame(nb)
tb8 = Frame(nb)

nb.add(tb0, text = "Home")
nb.add(tb1, text = "Plástico")
nb.add(tb2, text = "Papel")
nb.add(tb3, text = "Vidro")
nb.add(tb4, text = "Metal")
nb.add(tb5, text = "Orgânico")
nb.add(tb6, text = "Eletrônico")
nb.add(tb7, text = "MAPS")
nb.add(tb8, text = "NEWS")

Opt = StringVar(tb7)
NameVar = StringVar(tb7)
EndVar = StringVar(tb7)
Material = StringVar(tb7)

Opt.set('1')
NameVar.set('...')
EndVar.set('...')
Material.set('Qualquer')


#Página Plástico
ColMiddle = Frame(tb1, width=500)
Row1e = Frame(tb1, highlightbackground = "black", highlightthickness = 2)
Row2e = Frame(tb1, highlightbackground = "black", highlightthickness = 2)
Row1d = Frame(tb1, highlightbackground = "black", highlightthickness = 2)
Row2d = Frame(tb1, highlightbackground = "black", highlightthickness = 2)

ColMiddle.grid(row = 0, column = 1, rowspan = 2)
Row1e.grid(row = 0, column = 0, padx = 30, pady= 50, sticky = 'NW')
Row2e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row1d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row2d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb1.grid_rowconfigure(ColMiddle, weight = 1)
tb1.grid_rowconfigure(Row1e, weight = 1)
tb1.grid_rowconfigure(Row1d, weight = 1)
tb1.grid_rowconfigure(Row2e, weight = 1)
tb1.grid_rowconfigure(Row2d, weight = 1)
tb1.grid_columnconfigure(ColMiddle, weight = 1)
tb1.grid_columnconfigure(Row1e, weight = 1)
tb1.grid_columnconfigure(Row1d, weight = 1)
tb1.grid_columnconfigure(Row2e, weight = 1)
tb1.grid_columnconfigure(Row2d, weight = 1)

#programa principal do plástico
etq1 = Label(ColMiddle, text = "MEIO")
etq2 = Label(Row1e, font = "-weight bold -size 10",  text = "História")
etq3 = Label(Row1d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row2e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row2d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)


#Página Papel
ColMiddle2 = Frame(tb2, width = 500)
Row3e = Frame(tb2, highlightbackground = "black", highlightthickness=2)
Row4e = Frame(tb2, highlightbackground = "black", highlightthickness=2)
Row3d = Frame(tb2, highlightbackground = "black", highlightthickness=2)
Row4d = Frame(tb2, highlightbackground = "black", highlightthickness=2)

ColMiddle2.grid(row = 0, column = 1, rowspan= 2)
Row3e.grid(row = 0, column = 0, padx = 30, pady = 50, sticky = 'NW')
Row4e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row3d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row4d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb2.grid_rowconfigure(ColMiddle2, weight = 1)
tb2.grid_rowconfigure(Row3e, weight = 1)
tb2.grid_rowconfigure(Row3d, weight = 1)
tb2.grid_rowconfigure(Row4e, weight = 1)
tb2.grid_rowconfigure(Row4d, weight = 1)
tb2.grid_columnconfigure(ColMiddle2, weight = 1)
tb2.grid_columnconfigure(Row3e, weight = 1)
tb2.grid_columnconfigure(Row3d, weight = 1)
tb2.grid_columnconfigure(Row4e, weight = 1)
tb2.grid_columnconfigure(Row4d, weight = 1)

#programa principal do papel
etq1 = Label(ColMiddle2, font = "-weight bold -size 10", text = "MEIO")
etq2 = Label(Row3e, font = "-weight bold -size 10", text = "História")
etq3 = Label(Row3d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row4e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row4d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)

#Página Vidro
ColMiddle3 = Frame(tb3, width = 500)
Row5e = Frame(tb3, highlightbackground = "black", highlightthickness = 2)
Row6e = Frame(tb3, highlightbackground = "black", highlightthickness = 2)
Row5d = Frame(tb3, highlightbackground = "black", highlightthickness = 2)
Row6d = Frame(tb3, highlightbackground = "black", highlightthickness = 2)

ColMiddle3.grid(row = 0, column = 1, rowspan = 2)
Row5e.grid(row = 0, column = 0, padx = 30, pady = 50, sticky = 'NW')
Row6e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row5d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row6d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb3.grid_rowconfigure(ColMiddle3, weight = 1)
tb3.grid_rowconfigure(Row5e, weight = 1)
tb3.grid_rowconfigure(Row5d, weight = 1)
tb3.grid_rowconfigure(Row6e, weight = 1)
tb3.grid_rowconfigure(Row6d, weight = 1)
tb3.grid_columnconfigure(ColMiddle3, weight = 1)
tb3.grid_columnconfigure(Row5e, weight = 1)
tb3.grid_columnconfigure(Row5d, weight = 1)
tb3.grid_columnconfigure(Row6e, weight = 1)
tb3.grid_columnconfigure(Row6d, weight = 1)

#programa principal do vidro
etq1 = Label(ColMiddle3, text = "MEIO")
etq2 = Label(Row5e, font = "-weight bold -size 10", text = "História")
etq3 = Label(Row5d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row6e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row6d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)


#Página Metal
ColMiddle4 = Frame(tb4, width = 500)
Row7e = Frame(tb4, highlightbackground = "black", highlightthickness = 2)
Row8e = Frame(tb4, highlightbackground = "black", highlightthickness = 2)
Row7d = Frame(tb4, highlightbackground = "black", highlightthickness = 2)
Row8d = Frame(tb4, highlightbackground = "black", highlightthickness = 2)

ColMiddle4.grid(row = 0, column = 1, rowspan = 2)
Row7e.grid(row = 0, column = 0, padx = 30, pady = 50, sticky = 'NW')
Row8e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row7d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row8d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb4.grid_rowconfigure(ColMiddle4, weight = 1)
tb4.grid_rowconfigure(Row7e, weight = 1)
tb4.grid_rowconfigure(Row7d, weight = 1)
tb4.grid_rowconfigure(Row8e, weight = 1)
tb4.grid_rowconfigure(Row8d, weight = 1)
tb4.grid_columnconfigure(ColMiddle4, weight = 1)
tb4.grid_columnconfigure(Row7e, weight = 1)
tb4.grid_columnconfigure(Row7d, weight = 1)
tb4.grid_columnconfigure(Row8e, weight = 1)
tb4.grid_columnconfigure(Row8d, weight = 1)

#programa principal do Metal
etq1 = Label(ColMiddle4, text = "MEIO")
etq2 = Label(Row7e, font = "-weight bold -size 10", text = "História")
etq3 = Label(Row7d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row8e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row8d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)

#Página Orgânnico
ColMiddle5 = Frame(tb5, width = 500)
Row9e = Frame(tb5, highlightbackground = "black", highlightthickness = 2)
Row10e = Frame(tb5, highlightbackground = "black", highlightthickness = 2)
Row9d = Frame(tb5, highlightbackground = "black", highlightthickness = 2)
Row10d = Frame(tb5, highlightbackground = "black", highlightthickness = 2)

ColMiddle5.grid(row = 0, column = 1, rowspan = 2)
Row9e.grid(row = 0, column = 0, padx = 30, pady = 50, sticky = 'NW')
Row10e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row9d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row10d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb5.grid_rowconfigure(ColMiddle5, weight = 1)
tb5.grid_rowconfigure(Row9e, weight = 1)
tb5.grid_rowconfigure(Row9d, weight = 1)
tb5.grid_rowconfigure(Row10e, weight = 1)
tb5.grid_rowconfigure(Row10d, weight = 1)
tb5.grid_columnconfigure(ColMiddle5, weight = 1)
tb5.grid_columnconfigure(Row9e, weight = 1)
tb5.grid_columnconfigure(Row9d, weight = 1)
tb5.grid_columnconfigure(Row10e, weight = 1)
tb5.grid_columnconfigure(Row10d, weight = 1)

#programa principal do Orgânico
etq1 = Label(ColMiddle5, text = "MEIO")
etq2 = Label(Row9e, font = "-weight bold -size 10", text = "História")
etq3 = Label(Row9d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row10e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row10d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)

#Página Eletrônico
ColMiddle6 = Frame(tb6, width = 500)
Row11e = Frame(tb6, highlightbackground = "black", highlightthickness = 2)
Row12e = Frame(tb6, highlightbackground = "black", highlightthickness = 2)
Row11d = Frame(tb6, highlightbackground = "black", highlightthickness = 2)
Row12d = Frame(tb6, highlightbackground = "black", highlightthickness = 2)

ColMiddle6.grid(row = 0, column = 1, rowspan = 2)
Row11e.grid(row = 0, column = 0, padx = 30, pady = 50, sticky = 'NW')
Row12e.grid(row = 1, column = 0, padx = 30, pady = 50, sticky = 'SW')
Row11d.grid(row = 0, column = 2, padx = 30, pady = 50, sticky = 'NE')
Row12d.grid(row = 1, column = 2, padx = 30, pady = 50, sticky = 'SE')

tb6.grid_rowconfigure(ColMiddle6, weight = 1)
tb6.grid_rowconfigure(Row11e, weight = 1)
tb6.grid_rowconfigure(Row11d, weight = 1)
tb6.grid_rowconfigure(Row12e, weight = 1)
tb6.grid_rowconfigure(Row12d, weight = 1)
tb6.grid_columnconfigure(ColMiddle6, weight = 1)
tb6.grid_columnconfigure(Row11e, weight = 1)
tb6.grid_columnconfigure(Row11d, weight = 1)
tb6.grid_columnconfigure(Row12e, weight = 1)
tb6.grid_columnconfigure(Row12d, weight = 1)

#programa principal do Eletrônicos
etq1 = Label(ColMiddle6, text = "MEIO")
etq2 = Label(Row11e, font = "-weight bold -size 10", text = "História")
etq3 = Label(Row11d, font = "-weight bold -size 10", text = "Matéria Prima e Características")
etq4 = Label(Row12e, font = "-weight bold -size 10", text = "Processo de Reciclagem e Cuidados")
etq5 = Label(Row12d, font = "-weight bold -size 10", text ="Formas de Utilização e Reutilização")
etq1.grid(row = 0, column = 0,)
etq2.grid(row = 0, column = 0)
etq3.grid(row = 0, column = 0)
etq4.grid(row = 0, column = 0)
etq5.grid(row = 0, column = 0)

"""HOME"""
esqImg = Frame(tb0)
esqImg.grid(row=0,column=0)
dirImg = Frame(tb0)
dirImg.grid(row=0,column=2)
centText = Frame(tb0)
centText.grid(row=0,column=1)

tb0.grid_columnconfigure(esqImg, weight = 1)
tb0.grid_columnconfigure(dirImg, weight = 1)
tb0.grid_columnconfigure(centText, weight = 1)

img11 = PhotoImage(file = "Imagens\LogoQ(Vermelho).png")
img12 = PhotoImage(file = "Imagens\LogoQ(Amarelo).png")
img13 = PhotoImage(file = "Imagens\logoQ(verde).png")
img21 = PhotoImage(file = "Imagens\logoQ(azul).png")
img22 = PhotoImage(file = "Imagens\logoQ(laranja).png")
img23 = PhotoImage(file = "Imagens\logoQ(marrom).png")
imgmm = PhotoImage(file = "Imagens\maps.png")

HomeEtq1 = Label(centText, text = "Bem Vindo ao projeto Reciclando o Mundo\n")
HomeEtq2 = Label(centText, text = "Use as guias superiores para navegar por nossas páginas!")
HomeEtq3 = Label(centText, text = "As guias de Plástico à Eletrônico vão te dar informações a respeito de cada material")
HomeEtq4 = Label(centText, text = "Na guia MAPS você vai encontrar diversas formas de pesquisar por um ponto de reciclagem")
HomeEtq5 = Label(centText, text = "Na guia NEWS você será direcionado a um site a sua escolha onde poderá encontrar todas as novidades do assunto")
HomeEtq1.grid(row = 0, column = 1,)
HomeEtq2.grid(row = 1, column = 1,)
HomeEtq3.grid(row = 2, column = 1,)
HomeEtq4.grid(row = 3, column = 1,)
HomeEtq5.grid(row = 4, column = 1,)

pan11 = Label(esqImg, width=145, height=145, image = img11)
pan12 = Label(esqImg, width=145, height=145, image = img12)
pan13 = Label(esqImg, width=145, height=145, image = img13)
pan14 = Label(esqImg, width=145, height=145, image = imgmm)
pan21 = Label(dirImg, width=145, height=145, image = img21)
pan22 = Label(dirImg, width=145, height=145, image = img22)
pan23 = Label(dirImg, width=145, height=145, image = img23)
pan24 = Label(dirImg, width=145, height=145, image = imgmm)

pan11.grid(row=0, column=0, padx=5, pady=5, sticky = 'E')
pan12.grid(row=1, column=0, padx=5, pady=5, sticky = 'W')
pan13.grid(row=2, column=0, padx=5, pady=5, sticky = 'W')
pan14.grid(row=3, column=0, padx=5, pady=5, sticky = 'W')
pan21.grid(row=0, column=1, padx=5, pady=5, sticky = 'E')
pan22.grid(row=1, column=1, padx=5, pady=5, sticky = 'E')
pan23.grid(row=2, column=1, padx=5, pady=5, sticky = 'E')
pan24.grid(row=3, column=1, padx=5, pady=5, sticky = 'E')




"""PLÁSTICO"""
#História do Plástico
hist = Label(Row1e, wraplength=300, text = "\nO primeiro plástico sintético foi desenvolvido no início do século  XX, e registrou um desenvolvimento acelerado a partir de 1920. O plástico se tornou indispenável principalmente por inúmeros itens, que só existem devido a sua criação. Inicialmente, os materiais plásticos surgiram com o objetivo de substituir materiais de origem animal, como o marfim dos elefantes. E assim  se consolidou como um material leve, resistente e versátil.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row1d, wraplength=300, text = "\nPlásticos são materiais formados pela união de grandes cadeias moleculares chamadas polímeros, que, por sua vez, são formadas por moléculas menores, chamadas monômeros. A matéria-prima dos plásticos é o petróleo. Este é formado por uma complexa mistura de compostos. O plástico pode ser rígido ou flexível, transparente ou opaco, resistente à humidade ou solúvel em água, as possibilidades são praticamente infinitas.")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row2e, wraplength=300, text = "\n A reciclagem consiste em três processos: A primeira é a Coleta e Separação: é a separação dos resíduos, a segunda é a Revalorização, onde passa por um processo que faz com que ele volta a ser matéria-prima; A terceira é a Transformação onde se torna um novo produto. \nÉ muito importante todos se conscientizarem de fazer o descarte de maneira correta, não jogar lixo nas praias, ruas ou qualquer lugar inadequado.")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row2d,  wraplength=300, text = "\nAtualmente, os plásticos são utilizados na fabricação de materiais elétricos, como fios e cabos, geladeiras, embalagens para diversos produtos, bens de consumo (como escovas de dente, canetas, réguas). A lista é enorme, assim como as possibilidades de aplicação. A reciclagem de plásticos mantém os materiais ainda úteis fora dos aterros e estimula as empresas a desenvolver produtos novos e inovadores feitos a partir deles.")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img = PhotoImage(file = "imagens/logo(Vermelho).png")
panel = Label(ColMiddle, width=200, height=300, image = img)
panel.grid(row = 0, column = 0,)


"""PAPEL"""
#História do Papel
hist = Label(Row3e, wraplength=300, text = "\nO papel que conhecemos hoje teve origem na China. Misturando cascas de árvores e trapos de tecidos e depois de molhados, batidos até formarem uma pasta. Esta pasta era depositada em peneiras para escorrer a água, e depois de seca tornava-se uma folha de papel. Ainda hoje os trapos de algodão e linho são utilizados por alguns países na fabricação de papéis resistentes, como o papel-moeda.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row3d, wraplength=300, text = "\nA matéria-prima para a sua fabricação é a celulose, que pode ser extraída de árvores. Os papéis são fabricados basicamente com polpas de fibras e água. Outros componentes são incluídos de acordo com a finalidade do papel como, por exemplo, cargas minerais. Eles possuem características Visíveis (Gramatura, Espessura, Brancura, Opacidade, Cor e Textura) e Invisíveis (Tipo de Fibra, Colagem, pH e Umidade).")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row4e, wraplength=300, text = "\nA reciclagem do papel começa com a separação do material para ser colocado em contentores que irão gerar fibras novas, onde se tornam uma pasta de celulose. Ao final a pasta é levada para a secagem e formatação. Assim se tornando um novo papel. Para ser feito todo esse processo armazene o papel em local seco, Não jogue as embalagens em cestos com restos de outros resíduos que podem “contaminá-lo”.")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row4d,  wraplength=300, text = "\nO papel é um material utilizado para diversas finalidades, como a confecção de embalagens de alimentos, produtos hospitalares, materiais elétricos e de construção, de higiene pessoal e coletiva. Quando reciclamos o papel ou compramos papel reciclado estamos contribuindo com o meio ambiente, pois árvores deixaram de ser cortadas. E também gera renda para  catadores e recicladores de papel.")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img1 = PhotoImage(file = "imagens/logo(azul).png")
panel1 = Label(ColMiddle2, width=200, height=300, image = img1)
panel1.grid(row = 0, column = 0,)


"""VIDRO"""
#História do Vidro
hist = Label(Row5e, wraplength=300, text = "\n Com as peças devidamente separadas, torna-se possível dar a correta destinação a cada tipo de componente dos aparelhos. Ferro, alumínio, vidro e plástico, por exemplo, são enviados à reciclagem. Peças mais complexas, como placas de circuito (constituídas por mais de 20 componentes distintos), são trituradas e cada elemento é destinado a um fim.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row5d, wraplength=300, text = "\nSão basicamente compostos por areia, calcário, barrilha, alumina, corantes e descorantes. As matérias primas que compõem o vidro são os vitrificantes, fundentes e estabilizantes. As características do vidro são transparente, duro, impermeável, isolante térmico, baixo nível de condutividade térmica, reciclável, recurso abundante na natureza.")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row6e, wraplength=300, text = "\nO vidro usado retorna às vidrarias, onde é lavado, triturado e os cacos são misturados com mais areia, calcário, sódio e outros minerais e fundidos. Depois o material é esquentado onde é feito: a modelagem. É necessário sempre tomar cuidado em seu descarte, pois pode causar danos aos coletores de lixo. Não polui o solo, água ou ar, e não se decompõe e nem se desfaz na queima, podendo apenas derreter.")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row6d,  wraplength=300, text = "\nO vidro é usado nos pára-brisas e janelas dos automóveis, lâmpadas, garrafas, compotas, garrafões, frascos, recipientes, copos, janelas, lentes, tela de televisores e monitores, fibra ótica e etc. Recipientes de vidro, geralmente transparentes, são ótimos para serem utilizados como potes organizadores, Frascos de geléia são reaproveitados para armazenar alimentos, fracos de requeijão podem ser reaproveitados como copo. ")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img2 = PhotoImage(file = "imagens/logo(verde).png")
panel2 = Label(ColMiddle3, width=200, height=300, image = img2)
panel2.grid(row = 0, column = 0,)


"""METAL"""
#História do Metal
hist = Label(Row7e, wraplength=300, text = "\nO primeiro tipo de metal utilizado foi o cobre. Com o passar dos anos o estanho também foi utilizado como outro recurso na fabricação de armas e utensílios. Com a junção desses dois metais, por volta de 3000 a.C., tivemos o aparecimento do bronze. Só mais tarde é feita a descoberta do ferro. Manipulado por comunidades da Ásia Menor, cerca de 1500 a.C. o ferro teve um lento processo de propagação.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row7d, wraplength=300, text = "\nOs metais podem ser encontrados misturados no solo e nas rochas, sendo chamados de minérios, ele serve de mistura para fazer outras coisa como, objetos, eletrônicos, construções, e muitas outras coisas. Ele é sólido, não deixa passar luz e conduz bem a eletricidade e o calor, possuindo um brilho especial chamado de metálico. Quando aquecido é maleável, podendo ser moldado em várias formas.")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row8e, wraplength=300, text = "\nPrimeiro é feita a coleta, depois a separação, assim ele é levado para o processamento onde é feita A trituração é feita para promover o processo de fusão, depois é feita a fusão, a sucata é derretida em um grande forno, a purificação e por fim a solidificação. Deve-se ter muito cuidado no momento da reciclagem, pois em uma grande parte destas ligas há a presença de chumbo, que é um metal tóxico.")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row8d,  wraplength=300, text = "\nHoje em dia ele é encontrado em nossa casa (ex: panelas, armários, talheres), nos automóveis, nas embalagens de alimentos, etc. A grande vantagem do reaproveitamento de metais é que eles são 100% recicláveis, e esse processo pode ser feito inúmeras vezes, sem que o material perca a maioria das suas propriedades. Ou seja, não há um limite para a reutilização do metal.")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img3 = PhotoImage(file = "imagens/logo(Amarelo).png")
panel3 = Label(ColMiddle4, width=200, height=300, image = img3)
panel3.grid(row = 0, column = 0,)


"""ORGÂNICO"""
#História do Orgânico
hist = Label(Row9e, wraplength=300, text = "\nLixo orgânico é um material de origem biológica, pode ser proveniente da vida animal ou vegetal. Os restos de verduras, frutas e outros alimentos causam dúvidas na hora do descarte, eles representam metade dos resíduos sólidos urbanos gerados no Brasil. A sua reciclagem está relacionada com técnicas de sustentabilidade, uma vez que, se lançados em locais inapropriados podem causar impactos negativos no meio ambiente.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row9d, wraplength=300, text = "\nOs resíduos orgânicos são constituídos basicamente por restos de animais ou vegetais descartados de atividades humanas. Podem ter diversas origens, como doméstica ou urbana (restos de alimentos e podas), agrícola ou industrial (resíduos de agroindústria alimentícia, indústria madeireira, frigoríficos), de saneamento básico (lodos de estações de tratamento de esgotos), entre outras.")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row10e, wraplength=300, text = "\nExistem duas formas de reciclar o lixo orgânico: a compostagem, e por meio da produção de biogás. O processo de compostagem pode ser definido como a reciclagem de matéria orgânica. O objetivo é diminuir o impacto nos aterros sanitários, onde toda a matéria vira gás metano, prejudicial quando depositado no solo. É importante não misturar o lixo orgânico com o lixo reciclável. ")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row10d,  wraplength=300, text = "\nEle pode ser utilizado para a realização da compostagem, por exemplo, se pensarmos na área da agricultura. Outra maneira de reaproveitar os resíduos orgânicos é pela criação adequada de minhocas, ou tratamento realizado em minhocários. A minhoca alimenta-se de resíduos orgânicos, portanto o processo digestivo delas é uma outra forma de decomposição e reaproveitamento dos resíduos. ")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img4 = PhotoImage(file = "imagens/logo(marrom).png")
panel4 = Label(ColMiddle5, width=200, height=300, image = img4)
panel4.grid(row = 0, column = 0,)


"""ELETRÔNICO"""
#História do Orgânico
hist = Label(Row11e, wraplength=300, text = "\nA Terceira Revolução Industrial veio e percebeu-se que, para os fabricantes, assim que o produto sai da loja ele já deve ser considerado lixo e o consumidor deve ser bombardeado de propaganda para substituí-lo, já que ficou cada vez mais fácil de tornar os aparelhos obsoletos. A geração de resíduo é absurda e os impactos estão sendo sentidos em todas as esferas: ambiental, social e econômica.")
hist.grid(row = 1, column = 0,)

#Matéria Prima e Caracteristicas
mater = Label(Row11d, wraplength=300, text = "\nDentro de equipamentos eletroeletrônicos jogados no lixo são encontradas matérias-primas preciosas, como ouro, prata, paládio, além de cobre e alumínio. O lixo eletrônico ou Resíduos de Equipamentos Elétricos e Eletrônicos (REEE) são todos os dispositivos eletroeletrônicos, de celulares, tablets e computadores a TVs, lavadoras de louça e de roupa, geladeiras e etc., que foram descartados por seus donos.")
mater.grid(row = 1, column = 0,)

#Processo de Reciclagem e cuidados
recicla = Label(Row12e, wraplength=300, text = "\nApós a coleta do e-lixo, o processo de reciclagem de equipamentos eletrônicos se inicia por meio de uma triagem, há a separação dos equipamentos em condições de uso (que podem ser doados) dos que não podem ser reutilizados. Em hipótese alguma os eletrônicos devem ser descartados em lixo comum. Isso porque muitos desses itens têm substâncias nocivas ao meio ambiente, como chumbo ou mercúrio.")
recicla.grid(row = 1, column = 0,)

#Formas de Utilização e Reutilização
recicla = Label(Row12d,  wraplength=300, text = "\nO lixo, orgânico é utilizado para Reutilização de metais preciosos, Geração de empregos, Economia de energia, Movimenta a economia, Redução da poluição da atmosfera, Alívio dos aterros sanitários.  Com as peças devidamente separadas, torna-se possível dar a correta destinação a cada tipo de componente dos aparelhos. Ferro, alumínio, vidro e plástico, por exemplo, são enviados à reciclagem.")
recicla.grid(row = 1, column = 0,)

#Imagem do meio
img5 = PhotoImage(file = "imagens/logo(laranja).png")
panel5 = Label(ColMiddle6, width=200, height=300, image = img5)
panel5.grid(row = 0, column = 0,)

"""MAPS"""

# ----- Geral -----
inputPan = Frame(tb7, highlightbackground = "black", highlightthickness = 2)
listPan = Frame(tb7, highlightbackground = "black", highlightthickness = 2)

inputPan.grid(row = 0, column = 0, padx = 30, pady = 30, sticky = 'SE')
listPan.grid(row = 0, column = 1, rowspan = 2, padx = 30, pady = 30, sticky = 'NW')

listPan.config(width=40)

tb7.grid_rowconfigure(inputPan, weight = 1)
tb7.grid_rowconfigure(listPan, weight = 1)
tb7.grid_columnconfigure(inputPan, weight = 1)
tb7.grid_columnconfigure(listPan, weight = 1)

rowA = Frame(inputPan)
rowA.grid(row=0)
rowB = Frame(inputPan)
rowB.grid(row=1)
buttons = Frame(listPan)
buttons.grid(row=5,columnspan=2)

QuitButton = Button(tb7, text='Sair', command=tb7.quit) # cria o botão para finalizar o programa
QuitButton.grid(row=1, column=0)

def AbsoluteDistance(a, b):
    res = abs(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))
    return res

def AbsoluteConvertedDistance(a, b):
    difa = abs(a[0]-b[0])
    difb = abs(a[1]-b[1])
    res = abs(math.sqrt(difa**2 + difb**2))
    res = res * 111.118
    return res

def PointsOfMaterial(mat): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = []
    for i in range(len(cd.material)):
        if mat in cd.material[i] or mat == 'Qualquer':
            res.append([cd.nome[i],cd.endereco[i]])
    return res

def NearestPoint(lat, lon, mat): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = ['.','.',0]
    res[2] = 1000000000
    for i in range(len(cd.material)):
        hdist = AbsoluteDistance([cd.latitude[i],cd.longitude[i]], [lat, lon])
        if (mat in cd.material[i] or mat == 'Qualquer') and hdist < res[2]:
            res = [cd.nome[i],cd.endereco[i],hdist]
    res.pop(2)
    return res

def AllPointsInRange(lat, lon, mat, alc): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = []
    for i in range(len(cd.material)):
        hdist = AbsoluteConvertedDistance([cd.latitude[i],cd.longitude[i]], [lat, lon])
        if (mat in cd.material[i] or mat == 'Qualquer') and hdist <= alc:
            res.append([cd.nome[i],cd.endereco[i]])
    return res

def change(e):
    end = PointList.get(ACTIVE)[46:]
    for i in range(len(cd.endereco)):
        if cd.endereco[i] == end:
            NameVar.set(cd.nome[i])
            EndVar.set(cd.endereco[i])
    return

def UrlMap(e):
    end = PointList.get(ACTIVE)[46:]
    for i in range(len(cd.endereco)):
        if cd.endereco[i] == end:
            res = cd.nome[i]
    res = 'https://www.google.com.br/maps/search/' + res.replace(' ', '+') + '/'
    webbrowser.open(res, new=0, autoraise=True)
    return

def calculate(e):
    entries = []
    for i in e:
        entries.append(i.get())
    if entries[4] == '1':
        res = PointsOfMaterial(entries[0])
        PointList.delete(0, END)
        for i in res:
            xtext = ''
            for k in range(40):
                try:
                    xtext += i[0][k]
                except(IndexError):
                    xtext += '.'
            xtext += '... → '
            xtext += i[1]
            PointList.insert(END, xtext)
    elif entries[4] == '2':
        res = NearestPoint(float(entries[1]),float(entries[2]),str(entries[0]))
        PointList.delete(0, END)
        xtext = ''
        for k in range(40):
            try:
                xtext += res[0][k]
            except(IndexError):
                xtext += '.'
        xtext += '... → '
        xtext += res[1]
        PointList.insert(END, xtext)
    elif entries[4] == '3':
        res = AllPointsInRange(float(entries[1]), float(entries[2]), str(entries[0]), float(entries[3]))
        PointList.delete(0, END)
        for i in res:
            xtext = ''
            for k in range(40):
                try:
                    xtext += i[0][k]
                except(IndexError):
                    xtext += '.'
            xtext += '... → '
            xtext += i[1]
            PointList.insert(END, xtext)
    return

def Os(e) : # cria e atualiza o painel em que os dados serão inseridos e retorna constantemente os dados nas inputbox
    EtqLatitude=Label(rowB, text="Selecione o numero da função desejada:  ")
    EtqLatitude.grid(row=0, column=0)
    FunctList = OptionMenu(rowB, Opt, '1', '2', '3')
    FunctList.grid(row=0,column=1)

    EtqLatitude=Label(rowA, text="Material: ")
    EtqLatitude.grid(row=0, column=0)
    MaterList = OptionMenu(rowA, Material, 'Qualquer', 'Papel', 'Plástico', 'Metal', 'Vidro', 'Orgânico', 'Eletronico')
    MaterList.grid(row=0,column=1)

    EtqLatitude=Label(rowA, text="Latitude: ")
    EtqLatitude.grid(row=1, column=0)
    Latitude=Entry(rowA)
    Latitude.grid(row=1, column=1)

    EtqLongitude=Label(rowA, text="Longitude: ")
    EtqLongitude.grid(row=2, column=0)
    Longitude=Entry(rowA)
    Longitude.grid(row=2, column=1)

    EtqRaio=Label(rowA, text="Raio (em Km): ")
    EtqRaio.grid(row=3, column=0)
    Raio=Entry(rowA)
    Raio.grid(row=3, column=1)

    res = []
    res.append(Material)
    res.append(Latitude)
    res.append(Longitude)
    res.append(Raio)
    res.append(Opt)
    return res

 # ----- inputPan -----
e = Os(Opt) # executa e recebe constantemente o painel de dados
EtqDescrlist1=Label(rowB, text="Descrição:")
EtqDescrlist2=Label(rowB, text="1 - Realiza uma consulta a todos os pontos de coleta do")
EtqDescrlist3=Label(rowB, text="resíduo a sua escolha.")
EtqDescrlist4=Label(rowB, text="2 - Busca pelo ponto de coleta de determinado material")
EtqDescrlist5=Label(rowB, text="mais próximo a partir das suas coordenadadas geográficas.")
EtqDescrlist6=Label(rowB, text="3 - Indica todos os pontos de coleta de determinado")
EtqDescrlist7=Label(rowB, text="material em um raio a sua escolha a partir de suas coordenadas.")
EtqDescrlist1.grid(row=1, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist2.grid(row=2, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist3.grid(row=3, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist4.grid(row=4, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist5.grid(row=5, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist6.grid(row=6, column = 0, columnspan=3, sticky = 'W')
EtqDescrlist7.grid(row=7, column = 0, columnspan=3, sticky = 'W')
ExeButton = Button(rowB, text='Procurar', command=(lambda e=e: calculate(e))) # cria o botão de enviar os dados e define a execução condicional do seu comando
ExeButton.grid(row=0, column=2)

# ----- listPan -----
EtqDescr1=Label(listPan, text="Aqui estão os resultados encontrados") # lista de textos que exibem o nome e o endereço do ponto de coleta mais próximo do usuário
EtqDescr2=Label(listPan, text='clique em algum e pressione "ver" para ver a correspondencia completa logo abaixo')
EtqDescr3=Label(listPan, text="Nome: ") # lista de textos que exibem o nome e o endereço do ponto de coleta mais próximo do usuário
EtqDescr4=Label(listPan, text="Endereço: ")
EtqDescr5=Label(listPan, textvariable=NameVar) # lista de textos que exibem o nome e o endereço do ponto de coleta mais próximo do usuário
EtqDescr6=Label(listPan, textvariable=EndVar)

SeeButton = Button(buttons, text='Ver', command=(lambda e='.': change(e))) # cria o botão de enviar os dados e define a execução condicional do seu comando
SeeButton.grid(row=0, column=0, sticky = 'E', padx = 5)
MapsButton = Button(buttons, text='Pesquisar no google maps', command=(lambda e='.': UrlMap(e))) # cria o botão de enviar os dados e define a execução condicional do seu comando
MapsButton.grid(row=0, column=1, sticky = 'W', padx = 5)

PointList = Listbox(listPan)
PointList.grid(row=2, column=0, columnspan=2)
PointList.config(width = 75, height = 25)
# , yscrollcommand=scrollbar.set

EtqDescr1.grid(row=0, columnspan=2)
EtqDescr2.grid(row=1, column=0, columnspan=2)
EtqDescr3.grid(row=3, sticky = 'W')
EtqDescr5.grid(row=3, column=1)
EtqDescr4.grid(row=4, sticky = 'W')
EtqDescr6.grid(row=4, column=1)

"""NEWS"""
UrlList = Listbox(tb8)
UrlList.grid(row=1, column=0)
UrlList.config(width = 75, height = 25)

def GoUrl(e):
    end = UrlList.get(ACTIVE)
    for i in range(len(cd.urlName)):
        if cd.urlName[i] == end:
            res = cd.urlList[i]
    webbrowser.open(res, new=0, autoraise=True)
    return

newsEtq1=Label(tb8, text='Selecione um site na lista e pressione "Seguir Para o Site" para ser encaminhado') # lista de textos que exibem o nome e o endereço do ponto de coleta mais próximo do usuário
newsEtq1.grid(row=0)
tb8.grid_columnconfigure(newsEtq1, weight=1)

GoButton = Button(tb8, text='Seguir Para o Site', command=(lambda e='.': GoUrl(e))) # cria o botão de enviar os dados e define a execução condicional do seu comando
GoButton.grid(row=2, column=0, sticky = 'S', padx = 5)

for i in cd.urlName:
    UrlList.insert(END, i)

janela.mainloop()
