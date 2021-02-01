from flask import Flask, render_template, request
# utilizando "from" para pegar dentro do pacote flask o import Flask apenas e não o pacorte inteiro


app = Flask(__name__) # name é o nome do meu modulo da aplicação

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tibia', 'RPG', 'Desktop')
jogo2 = Jogo('Diablo 2', 'RPG', 'Nitendo Switch')
jogo3 = Jogo('CS GO', 'MMO', 'Desktop')

lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index(): # function

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console) #instanciando a classe Jogo
    lista.append(jogo) # após tirar a minha lista da função ola e deixa-la na classe
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)


