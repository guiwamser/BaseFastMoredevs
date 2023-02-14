from fastapi import APIRouter

from v1.endpoints import aluno

api_router = APIRouter()

#/api/v1/alunos
api_router.include_router(aluno.router, prefix='/alunos', tags=["alunos"])