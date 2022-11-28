from flask import Flask, jsonify , request

app = Flask(__name__)

jogadores = [
       {
        'ano':1930,
        'nome':'José Nasazzi',
        'seleção':'Uruguai'
       },
       {
        'ano':1934,
        'nome':'Giuseppe Meazza',
        'seleção':'Itália'
       },
       {
        'ano':1938,
        'nome':'Leônanoas da Silva',
        'seleção':'Brasil'
       },
       {
        'ano':1950,
        'nome':'Zizinho',
        'seleção':'Brasil'
       },
       {
        'ano':1954,
        'nome':'Puskas',
        'seleção':'Hungria'
       },
       {
        'ano':1958,
        'nome':'Pelé',
        'seleção':'Brasil'
       },
       {
        'ano':1962,
        'nome':'Garrincha',
        'seleção':'Brasil',
       },
       {
        'ano':1966,
        'nome':'Bobby Charlton',
        'seleção':'Inglaterra'
       },
       {
        'ano':1970,
        'nome':'Pelé',
        'seleção':'Brasil'
       },
       {
        'ano':1974,
        'nome':'Cruyff',
        'seleção':'Holanda'
       },
       {
        'ano':1978,
        'nome':'Mario Kempes',
        'seleção':'Argentina'
       },
       {
        'ano':1982,
        'nome':'Paolo Rossi',
        'seleção':'Itália'
       },
       {
        'ano':1986,
        'nome':'Maradona',
        'seleção':'Argentina'
       },
       {
        'ano':1990,
        'nome':'Schillaci',
        'seleção':'Itália'
       },
       {
        'ano':1994,
        'nome':'Romário',
        'seleção':'Brasil'
       },
       {
        'ano':1998,
        'nome':'Ronaldo',
        'seleção':'Brasil'
       },
       {
        'ano':2002,
        'nome':'Kahn',
        'seleção':'Alemanha'
       },
       {
        'ano':2006,
        'nome':'Zanoane',
        'seleção':'França'
       },
       {
        'ano':2010,
        'nome':'Diego Forlán',
        'seleção':'Uruguai'
       },
       {
        'ano':2014,
        'nome':'Messi',
        'seleção':'Argentina'
       },
       {
        'ano':2018,
        'nome':'Modric',
        'seleção':'Croácia'
       },
]

#Buscar todas informações.
@app.route('/jogadores', methods=['GET'])
def  obter_jogadores():
     return jsonify(jogadores)


#Buscar por ano.
@app.route('/jogadores/<int:ano>', methods=['GET'])
def obter_jogador_por_ano(ano):
    for jogador in jogadores:
        if jogador.get('ano') == ano:
             return jsonify (jogador)

#Editar Jogadores.
@app.route('/jogadores/<int:ano>',methods=['PUT'])
def editar_jogador_por_ano(ano):
     jogador_alterado = request.get_json() 
     for indice,jogador in enumerate (jogadores):
          if jogador.get(ano) == ano:
               jogadores[indice].update(jogador_alterado)
               return jsonify(jogadores[indice])



#Adicionar novo jogador.
@app.route('/jogadores',methods=['POST'] )
def incluir_novo_jogador():
     novo_jogador = request.get_json()
     jogadores.append(novo_jogador)

     return jsonify (jogadores)



#Excluir um jogador.
@app.route('/jogadores/<int:ano>',methods=['DELETE'] )
def excluir_jogador(ano):
     for indice, jogador in enumerate(jogadores):
          if jogador.get('ano') == ano:
               del jogadores[indice]

               return jsonify (jogadores)            


app.run(port=5000,host='localhost',debug=True)