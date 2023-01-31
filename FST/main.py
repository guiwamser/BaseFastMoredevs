from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Aluno
from fastapi import Response


app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "oi ????"}

alunos = {
    
    1: {"nome" : "nicolas", "idade" : 19, "email" : "asas@gmail"},
    2: {"nome" : "haiko", "idade" : 12, "email" : "qwqw@gmail"},
    3: {"nome" : "w", "idade" : 39, "email" : "asas@gmail"},
    4: {"nome" : "joao", "idade" : 17, "email" : "nicqwk@gmail"}

}

@app.get('/alunos')
async def get_alunos():
    return alunos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True

    )

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get('/alunos/{alunos_id}')
async def read_item(alunos_id: int):
    aluno = alunos[alunos_id]
    alunos.update({'id': alunos_id})
    
    return aluno 

@app.get('/alunos/{alunos_id}')
async def read_item(alunos_id: int):
    try:
        aluno = alunos[alunos_id]
        alunos.update({'id':alunos_id})
        return aluno
    except KeyError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = 'Não encontramos'
        )
     
@app.post("/aluno")
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    del aluno.id
    return aluno


@app.delete('/alunos/{aluno_id')
async def delete_aluno(aluno:_id: int):
    