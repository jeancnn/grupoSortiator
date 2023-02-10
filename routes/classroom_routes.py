from controller.classroom_controller import buscaClasseAlunos, cadastraClasse
from fastapi import APIRouter, status, Response
from models.model import ClassRoom

from typing import Optional, List


router = APIRouter(
    prefix='/classroom',
    tags=['classroom']
)

##
### Busca/lista todos as Classes
##
@router.get(
    '/',
    summary='Retorna uma lista Classes/Salas',
    description='Retorna uma lista de todas as Classes/Salas cadastradas em formato JSON',
    response_description='Lista de Classes/Salas cadastradas',
    response_model=List[ClassRoom],
    status_code=status.HTTP_200_OK)

def busca_classes(response: Response):
    lista_classes = buscaClasseAlunos()
    if lista_classes:
        response.status_code = status.HTTP_200_OK
        return lista_classes
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND



##
### Cadastro de Classes
##
@router.post(
    '/',
    summary='Cadastrar uma nova Classe',
    status_code=status.HTTP_200_OK)    

def cadastrar_classe(classe: ClassRoom, response: Response):
    """
    Cadastra uma nova Classe no sistema
    - **name:** nome da Classe ou Sala
    """
    novaClasse = cadastraClasse(classe)
    if novaClasse:
        response.status_code = status.HTTP_200_OK
        return novaClasse
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND        
