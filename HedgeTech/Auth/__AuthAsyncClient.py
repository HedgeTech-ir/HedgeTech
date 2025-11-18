# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from httpx import (
    AsyncClient ,
    Timeout ,
    Response
)
from jwt import decode

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

class AuthAsyncClient:
    
    def __init__(
        self,
        *,
        httpx_Client:AsyncClient,
        token:dict[str,str],
    ):
        
        
        self.httpx_Client : AsyncClient = httpx_Client
        self.token : dict[str,str] = token
        
        self.UpdatePermission
    
    
    @property
    def UpdatePermission(self)-> None:
        
        try : 
        
            self.Permissions = decode(
                jwt=self.token['Authorization'].encode(),
                algorithms='HS256',
                options={"verify_signature": False},
            )
            
        except Exception as e:
            
            raise ValueError(e)
            
        
    @classmethod
    async def login(
        cls,
        *,
        UserName_or_Email : str,
        Password : str
    )-> "AuthAsyncClient":
        
        httpx_Client = AsyncClient(
            verify=True ,
            http1=False ,
            http2=True ,
            timeout=Timeout(
                connect=.5,
                read=1,
                write=1,
                pool=.5,
            ),
        )
        
        
        login_res : Response = await httpx_Client.post(
            url='https://core.hedgetech.ir/auth/user/token/issue',
            data={
                'UserName_or_Email' : UserName_or_Email,
                'Password' : Password
            }
        )
        

        if login_res.status_code == 201:
            
            return cls(
                httpx_Client = httpx_Client,
                token = login_res.json()
            )
        
        else :
            
            raise ValueError(login_res.json().get('detail'))