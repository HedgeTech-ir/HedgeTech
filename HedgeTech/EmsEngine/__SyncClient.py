# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from typing import (
    Literal,
    Union
)
from HedgeTech.Auth import AuthSyncClient
from PIL.Image import open as image_open
from PIL.ImageFile import ImageFile
from io import BytesIO

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

class EmsEngine_TseIfb_SyncClient:
    
    def __init__(
        self,
        AuthSyncClient : AuthSyncClient,
    ):
        
        
        self.__AuthSyncClient = AuthSyncClient
        
        self.Customer_FullName : str | None = None
        self.Customer_TSEBourseCode : str | None = None
        self.oms_session : str | None = None
        
        
    def Get_Captcha(
        self,
        OMS : Literal[
            'Omex | Parsian',
            'Sahra | Karamad',
        ]
    )-> Union[ImageFile,None] :
        
        Captcha = self.__AuthSyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/ems-engine/tse-ifb/oms/login',
            params={'oms' : OMS }
        )
        
        if Captcha.status_code == 200: return image_open(BytesIO(Captcha.content))
    
        else : return None
    
    
    def OmsLogin(
        self,
        username: str,
        Password: str,
        Captcha_Value : str
    )-> None :
        
        login_response = self.__AuthSyncClient.httpx_Client.post(
            url='https://core.hedgetech.ir/ems-engine/tse-ifb/oms/login',
            data={
                'username' : username,
                'Password' : Password,
                'Captcha_Value' : Captcha_Value
            }
        )
        
    
        if login_response.status_code == 200:
            
            login_response = login_response.json()
            
            print(login_response['Status']['Description']['en'])
            
            self.Customer_FullName = login_response['Data']['Customer_FullName']
            self.Customer_TSEBourseCode = login_response['Data']['Customer_TSEBourseCode']
            self.oms_session = login_response['Data']['oms_session']
            
            return login_response
        
        else :
            
            if login_response.status_code == 400:
                
                raise ValueError(login_response.json()['detail']['Status']['Description']['en'])

            else : raise ValueError(login_response.text)
                    
