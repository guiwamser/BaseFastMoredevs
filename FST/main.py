from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Hello world, more devs"}

alunos = {
    1: "Lirinha",
    2: "Lirinha",
    3: "Lirinha",
    4: "Lirinha",
}

@app.get('/alunos')
async def alunos():
    return alunos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level= "info",
        reload = True
    )