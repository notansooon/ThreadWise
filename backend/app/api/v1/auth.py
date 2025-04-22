from fastapi import APIRouter, Requests


router = APIRouter(prefix='/auth')

@router.get("/login")
def login(requests : Requests):
    redirect_url = requests.url_for('callback')
           
@router.get("/callback")
def callback(requests: Requests):
    
    
    
    