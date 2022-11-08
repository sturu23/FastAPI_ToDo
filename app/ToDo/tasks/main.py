from fastapi import APIRouter, Depends, status, Response
from app.database import schemas, models
from app.database.schemas import Task
from app.dependencies import get_db
from app.database.db import Session

router = APIRouter(
    prefix='/tasks'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def add_task(request: Task, db: Session = Depends(get_db)):
    info = models.Task(body=request.body, is_active=False)
    db.add(info)
    db.commit()
    db.refresh(info)

    return info


@router.put('/take-task/{id}', status_code=status.HTTP_200_OK)
def take_task(id: int, response: Response, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()

    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Task with the id {id} is not avaliable'}
    task.is_active = True
    db.commit()
    db.refresh(task)

    return task


@router.get('/get-tasks', status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db)):
    all = db.query(models.Task).all()

    return all


@router.get('/get-tasks-by-id/{id}', status_code=status.HTTP_200_OK)
def get_tasks_id(id: int, response: Response, db: Session = Depends(get_db)):
    _id = db.query(models.Task).filter(models.Task.id == id).first()

    if not _id:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'task is not avaliable with that id {id}'}

    return _id


@router.delete('/delete-task/{id}', status_code=status.HTTP_200_OK)
def delete(id: int, response: Response, db: Session = Depends(get_db)):
    delete_it = db.query(models.Task).filter(models.Task.id == id).first()

    if not delete_it:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'can not delete task with that id {id}'}

    db.delete(delete_it)
    db.commit()

    return {'detail': f'task with the id {id} , deleted successfully'}
