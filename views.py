from utils import load_data, load_template, write_json, build_response
from database import Database, Note
import urllib.parse

db = Database("banco")
def e404():
    response = build_response()
    return response + load_template('404.html').encode()

def edit(request, id):
    card = db.get(id)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith('titulo'):
                titulo = urllib.parse.unquote_plus(chave_valor[7:])
                params['titulo'] = titulo
            elif chave_valor.startswith('detalhes'):
                detalhe = urllib.parse.unquote_plus(chave_valor[9:])
                params['detalhes'] = detalhe
        note_object = Note(title = params["titulo"], content = params["detalhes"], id = id)
        db.update(note_object)
        response = build_response(code=303, reason='See Other', headers='Location: /')
    else:
        response = build_response()
    return response + load_template('edit.html').format(titulo=card.title, conteudo=card.content).encode()
    
def delete(id):
    db.delete(id)
    return  build_response(code=303, reason='See Other', headers='Location: /')

def index(request):
    print(request)
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith('titulo'):
                titulo = urllib.parse.unquote_plus(chave_valor[7:])
                params['titulo'] = titulo
            elif chave_valor.startswith('detalhes'):
                detalhe = urllib.parse.unquote_plus(chave_valor[9:])
                params['detalhes'] = detalhe
            else:
                id = urllib.parse.unquote_plus(chave_valor[2:])
                params['id'] = id
        # write_json(params)
        note_object = Note(title = params["titulo"], content = params["detalhes"])
        db.add(note_object)
        response = build_response(code=303, reason='See Other', headers='Location: /')
    else:
        response = build_response()

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=note_object.title, details=note_object.content, id=note_object.id)
        for note_object in db.get_all()
        ]
    notes = '\n'.join(notes_li)
    return response + load_template('index.html').format(notes=notes).encode()