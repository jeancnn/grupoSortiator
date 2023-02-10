from controller.students_controller import findStudent, createStudent, editStudent, deleteStudent
from fastapi import APIRouter, Response
from fastapi import status
from models.model import Student

router = APIRouter(
    prefix='/students',
    tags=['students']
)

##
### Busca/lista todos os estudantes
##
@router.get(
    '/',
    summary='Retorna uma lista de estudantes',
    description='Retorna uma lista de todos os estudantes cadastrados em formato JSON',
    response_description='Lista de estudantes cadastrados',
    status_code=status.HTTP_200_OK)

def busca_alunos(response: Response):
    lista_alunos = findStudent()
    if lista_alunos:
        response.status_code = status.HTTP_200_OK
        return lista_alunos
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

##
### Busca de estudantes por ID
##
@router.get(
    '/{id}',
    summary='Retorna um estudante com base no ID especificado',
    description='Retorna um estudante cadastrado em formato JSON',
    response_description='JSON do estudante cadastrado',
    status_code=status.HTTP_200_OK)

def busca_alunosID(id: int, response: Response):
    lista_alunos = findStudent(id)
    if lista_alunos:
        response.status_code = status.HTTP_200_OK
        return lista_alunos
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
    
##
### Cadastro de alunos
##
@router.post(
    '/',
    summary='Cadastrar um novo aluno',
    description='Cadastra um novo aluno no banco de dados e retorna o aluno cadastrado',
    response_description='Retorna o aluno cadastrado',
    status_code=status.HTTP_200_OK)    

def cadastraAluno(classID: int, aluno: Student, response: Response):
    """
    Cadastra um estudante em uma classe do sistema
    - **name:** nome do estudante
    - **contact:** telefone do estudante
    """
    novoAluno = createStudent(classID, aluno)
    if novoAluno:
        response.status_code = status.HTTP_200_OK
        return novoAluno
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND        


##
### Editar alunos
##
@router.patch(
    '/{id}',
    summary='Edita aluno com base no ID especificado',
    status_code=status.HTTP_200_OK)    

def editaAluno(alunoID: int, aluno: Student, response: Response):
    """
    Edita os dados de um estudante do sistema
    - **name:** nome do estudante
    - **contact:** telefone do estudante
    """
    alunoEditado = editStudent(alunoID, aluno)
    if alunoEditado:
        response.status_code = status.HTTP_200_OK
        return alunoEditado
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND        

##
### Deletar alunos
##
@router.delete(
    '/{id}',
    summary='Apaga aluno com base no ID especificado',
    status_code=status.HTTP_200_OK)    

def apagaAluno(id: int, response: Response):
    """
    Edita os dados de um estudante do sistema
    - **name:** nome do estudante
    - **contact:** telefone do estudante
    """
    alunoApagado = deleteStudent(id)
    if alunoApagado:
        response.status_code = status.HTTP_200_OK
        return {
            "mensagem": f"Aluno com ID: {id} apagado com sucesso"
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND        