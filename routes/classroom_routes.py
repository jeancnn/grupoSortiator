from controller.classroom_controller import buscaClasseAlunos, cadastraClasse
from controller.groups_controller import findGroupsClassroom
from fastapi import APIRouter, status, Response
from models.model import ClassRoom
from models.model import Student

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import json


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
    # response_model=List[ClassRoom],
    status_code=status.HTTP_200_OK)

def busca_classes(response: Response):
    lista_classes = buscaClasseAlunos()
    print(jsonable_encoder(lista_classes))
    
    if lista_classes:
        response.status_code = status.HTTP_200_OK

        lista_classesJSON = jsonable_encoder(lista_classes)
        
        for classe in lista_classesJSON:
            classe["students"] = jsonable_encoder(buscaClasseAlunos(classe["id"]))
            #Preciso criar uma função retornando uma lista de grupos de um ID de classe específico
            classe["groups"] = jsonable_encoder(findGroupsClassroom(classe["id"]))

        return lista_classesJSON

    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

##
### Busca/lista todos os alunos na Classes
##
@router.get(
    '/{id}',
    summary='Retorna uma lista alunos de uma Classes/Salas',
    response_model=List[Student],
    status_code=status.HTTP_200_OK)

def busca_classe_students(id:int, response: Response):
    lista_classes_alunos = buscaClasseAlunos(id)
    if lista_classes_alunos:
        response.status_code = status.HTTP_200_OK
        print(lista_classes_alunos)
        return lista_classes_alunos
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
