class Pessoa():
    def insert (dados, nome, idade):
        dados.nome = nome
        dados.idade = idade
    def output (dados):
        print(dados.nome, dados.idade)

j = Pessoa()
j.insert('JUNIOR', 40)
j.output()
