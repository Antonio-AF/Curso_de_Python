

from tkinter import *
from functools import partial


class Calculadora(object):
    def __init__(self, window):
        self.font = ('Verdana', '16', 'bold')
        self.fontBotoes = ('Verdana', '10', 'bold')

        # Logo do Python.
        logo = PhotoImage(file ='imagens/logo_python.gif')

        # Logo do Botão Delete.
        self.bg_del = PhotoImage(file ='imagens/button_del.gif')

        # Frame do logo
        self.frame_logo = Frame(window)
        self.frame_logo['bg'] = '#EDF5E9'

        # Frame que contem os checkbuttons
        self.frame1 = Frame(window)
        self.frame1['bg'] = '#EDF5E9'


        # Frama que contem a entrada de texto.
        self.frame2 = Frame(window, pady=20)
        self.frame2['bg'] = '#EDF5E9'


        # Frame que contem o botão calcular.
        self.frame3 = Frame(window)
        self.frame3['bg'] = '#EDF5E9'


        # Frame que contem o texto das formular.
        self.frame4 = Frame(window, pady = 20)
        self.frame4['bg'] = '#EDF5E9'

        # Frame das variaveis Binomial e Poisson
        self.frame_variaveis = Frame(window)
        self.frame_variaveis['bg'] = '#EDF5E9'

        # Frame que contem os botões especificos.
        self.frame5 = Frame(window, bg='white')
        self.frame5['bg'] = '#EDF5E9'


        # Empacotando as Frames.
        self.frame_logo.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame_variaveis.pack()
        self.frame4.pack()
        self.frame5.pack()
        

        # Logo da Calculadora
        self.logo = Label(self.frame_logo)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        # Entrada de Variaveis
        self.l1 = Label(self.frame_variaveis, text='n = ', pady = 20, padx = 10, font = self.fontBotoes)
        self.e1 = Entry(self.frame_variaveis)
        self.l2 = Label(self.frame_variaveis, text='p = ', padx = 10, font = self.fontBotoes)
        self.e2 = Entry(self.frame_variaveis)




        # Chechbutton Binomial
        self.bino_s = False
        self.b_binomial = Checkbutton(self.frame1, text='Modo Binomial', bg='#EDF5E9', font = self.fontBotoes, command = self.AtvBinomial)
        self.b_binomial.pack(side=LEFT)


        self.poisson_s = False
        self.b_poisson = Checkbutton(self.frame1, text='Modo Poisson', bg='#EDF5E9', font=self.fontBotoes, command=self.AtvPoisson)
        self.b_poisson.pack()


        # Comando para a inserção de entrada de texto.
        self.form = Entry(self.frame2, bg='#DCF5F1', width=50)
        self.form.pack()

        # Comando para instaciar um Botão.
        self.calc = Button(self.frame3, text='Calcular', bg = '#DCF5F1', command= self.calcular, font=self.font)
        self.calc.pack()

        # Texto com o resultado do calculo.
        self.resultado = Label(self.frame4, text="Resultado", fg="blue", font = self.font)
        self.resultado.pack()



        botoes = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menos = 0)', 'media', 'desvio', 'moda',
                  'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)',
                  'p(k1 <= x <= k2)')

        for i in range(len(botoes)):
            if i % 3 == 0:
                subframe = Frame(self.frame5, pady = 1)
                subframe.pack()
            a = Button(subframe, text = botoes[i], bg='#97A8A6', width=25, bd=1.5, padx=5, font=self.fontBotoes, command = partial(self.ColocaTexto, botoes[i]))
            a.pack(side=LEFT)


        self.delete = Button(subframe, bd=0, padx=5, font=self.fontBotoes, command = self.Del)
        self.delete['image'] = self.bg_del
        self.delete.pack(side=LEFT)

    def mostra_elementos(self):
        self.l1.pack(side=LEFT)
        self.e1.pack(side=LEFT)
        self.l2.pack(side=LEFT)
        self.e2.pack(side=LEFT)

    def some_elementos(self):
        self.l1.pack_forget()
        self.e1.pack_forget()
        self.l2.pack_forget()
        self.e2.pack_forget()


    def Del(self):
        self.form.delete(0, END)


    def ColocaTexto(self, texto):
        self.form.insert(END, texto)


    def MSG(self, text, cor):
        self.resultado['text'] = text
        self.resultado['fg'] = cor


    def calcular(self):
        self.MSG(self.form.get(), 'green')
        self.form.delete(0, END)
        #self.resultado['text'] = self.form.get()
        #self.resultado['fg'] = 'green'


    def conf_binomial(self):
        self.l1['text'] = 'n = '
        self.l2['text'] = 'p = '


    def conf_poisson(self):
        self.l1['text'] = 'l = '
        self.l2['text'] = 't = '

    def AtvBinomial(self):
        self.bino_s = not self.bino_s
        if self.bino_s:
            self.MSG('Binomial Ativado', cor = 'red')
            self.mostra_elementos()
            if self.poisson_s:
                self.poisson_s = False
                self.b_poisson.deselect()
            else:
                self.mostra_elementos()
            self.conf_binomial()
        else:
            self.MSG('Binomial Desativado', cor = 'black')
            self.some_elementos()



    def AtvPoisson(self):
        self.poisson_s = not self.poisson_s
        if self.poisson_s:
            self.MSG('Poisson Ativado', cor='red')
            self.mostra_elementos()
            if self.bino_s:
                self.bino_s = False
                self.b_binomial.deselect()
            else:
                self.mostra_elementos()
            self.conf_poisson()
        else:
            self.MSG('Poisson Desativado', cor='black')
            self.some_elementos()




# Instacia de nossa Tela.
window = Tk()

# Criando uma instancia da calculadora.
Calculadora(window)


# Titulo da nossa janela/projeto.
window.title('Calculadora de Estatística')

# Comando para dimensionar a nossa tela.
window.geometry("900x700")

# Defini a cor de fundo de nossa Tela.
window['bg'] = '#EDF5E9'

# Comando para manter a visualização da tela.
window.mainloop()