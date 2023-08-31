import json
def extract_route(request):
    string = ''
    start = False
    contagem = 0
    for i in request:
        if i == '/'and contagem == 0:
            start = True
            contagem = 1
        
        elif i == ' ':
            start = False

        elif start:
            string += i
    return string

def read_file(path):
    with open(path, mode ='r+b') as file:
        return(file.read())

def load_data(jsons):
    with open(f'data/{jsons}', mode ='r') as file:
        return(json.loads(file.read()))
    
def load_template(arquivo):
    with open(f'templates/{arquivo}', mode ='r') as file:
        return(f'{file.read()}')
    
def write_json(dic):
    lista = load_data('notes.json')
    lista.append(dic)
    with open ('data/notes.json', mode = 'w') as file:
        json.dump(lista, file, indent = 4, ensure_ascii = False)

def build_response(body='', code = 200, reason = 'OK', headers = ''):
    final = f'HTTP/1.1 {code} {reason}'
    if headers:
        final += "\n" + headers
    
    final += "\n\n" + body
    return final.encode()