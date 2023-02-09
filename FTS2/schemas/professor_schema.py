from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProfessorSchema(SCBaseModel):
        id: Optional[int]
        nome: str
        email: str
        salario: int

        class Config:
            orm_mode = True