from fastapi import Depends, Header,HTTPException,status
from sqlalchemy.orm import Session
from typing import Annotated,Union
from security.authHandler  import AuthHandler
from service.userService import UserService
from db.database import get_db
from db.schema.userSchemas import UserResponse

AUTH_PREFIX="Bearer "

def get_current_user(session:Session=Depends(get_db),
                     authorization:Annotated[Union[str,None],Header()]=None)->UserResponse:
    print("function reached here!!1st")
    auth_expection=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authentication Credentials"
    ) 

    print("function reached here!!2nd")

    print("len(AUTH_PREFIX):",len(AUTH_PREFIX),AUTH_PREFIX)

    if not authorization:
        raise auth_expection
    
    if not authorization.startswith(AUTH_PREFIX):
        raise auth_expection
    

    payload=AuthHandler.decode_jwt(token=authorization[len(AUTH_PREFIX):])

    print("2nd len(AUTH_PREFIX):",len(AUTH_PREFIX),authorization[len(AUTH_PREFIX):])

    if payload and payload['user_id']:
        try:
            user=UserService(session=session).get_user_by_user_id(user_id=payload['user_id'])
            return UserResponse(
                id=user.id,
                name=user.name,
                email=user.email
            )
        except Exception as e:
            raise e
    raise auth_expection