from fastapi import FastAPI

app = FastAPI()

itens = []

# Lista todos os itens
@app.get('/')
def lista_itens():
    return itens[0:]

# adicionar tarefa
@app.post('/itens')
def criar_item(item: str):
    itens.append(item)
    return itens

# Listar tarefa especifica
@app.get('/itens/{id_item}')
def lista_item(id_item: int):
    if id_item < len(itens):
        return itens[id_item]
    else:
        return "Error 404 - Item not found"
    
# Remover tarefa
@app.delete('/itens/remove/{id_item}')
def remove_item(id_item : int):
    if id_item < len(itens):
        itens.pop(id_item)
        return itens[0:]
    else:
        return "Error 404 - Item not found"