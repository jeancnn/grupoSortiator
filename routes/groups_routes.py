from fastapi import APIRouter

router = APIRouter(
    prefix='/groups',
    tags=['groups']
)

@router.get('/')
def listaGroups():
        pass


@router.post('/')
def listaGroups():
        pass