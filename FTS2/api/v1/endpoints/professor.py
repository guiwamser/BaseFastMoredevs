from typing import List

from fastapi import APIRouter 
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.professor_models import ProfessorModel
from schemas.professor_schema import ProfessorSchema
from core.deps import get_session

router = APIRouter()

#GET Aluno
@router.get('/{aluno_id}', response_model=ProfessorSchema, status_code = status.HTTP_200_OK)
async def get_aluno(aluno_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == aluno_id)
        result = await session.execute(query)
        aluno = result.scalar_one_or_none()

        if aluno:
            return aluno
        else:
            raise HTTPException(detail='Aluno Nao Encontrado', status_code=status.HTTP_404_NOT_FOUND)

#GET Professor
@router.get('/', response_model=List[ProfessorSchema])
async def get_professor(db: AsyncSession = Depends(get_session)):

    async with db as session:
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores : List[ProfessorModel] = result.scalars().all()

        return professores


# Post aluno
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def post_aluno(aluno: ProfessorSchema, db: AsyncSession = Depends(get_session)):

    novo_professor = ProfessorModel( nome = professor.nome, email = professor.email)

    db.add(novo_professor)
    await db.commit()

    return novo_professor


#PUT Professor
@router.put('/{professor_id}', response_model=ProfessorSchema, status_code= status.HTTP_202_ACCEPTED)
async def put_professor(professor_id: int, professor: ProfessorSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_up = result.scalar_one_or_none()

        if professor_up: 
            professor_up.nome = professor.nome
            professor_up.email = professor.email
            professor_up.salario = professor.salario
            await session.commit()
            return professor_up
        else:
            raise HTTPException(detail='Professor Nao Encontrado', status_code=status.HTTP_404_NOT_FOUND)
       