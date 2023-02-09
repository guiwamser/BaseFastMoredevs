from core.configs import settings
from core.database import engine 
from models.aluno_models import AlunoModel

print("executando pra ver se deu boa")

async def create_table():
    print("entrando na funcao")
    
    async with engine.begin() as conn: 
        await conn.run_sync(settings.DB_BaseModel.metadata.drop_all)
        await conn.run_sync(settings.DB_BaseModel.metadata.create_all)
    
    print('Tabela criada com sucesso')


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_table())
