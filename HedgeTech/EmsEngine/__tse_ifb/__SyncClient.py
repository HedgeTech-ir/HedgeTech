# ========================================|======================================== #
#                                      Imports                                      #
# ========================================|======================================== #

from typing import (
    Literal,
)
from .__io_types import (
    HexUUID,
    OrderStatus,
)
from HedgeTech.Auth import AuthSyncClient
from PIL.Image import open as image_open
from PIL.ImageFile import ImageFile
from io import BytesIO

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #

class Order:
    
    """
    Represents a single trading order in EMS Engine.

    This class provides methods to send, edit, check status,
    and delete an order after creation.

    An Order instance is usually created via
    `EmsEngine_TseIfb_SyncClient` methods.
    """
    
    def __init__(
        self,
        *,
        SendOrder_RequestInfo : dict,
        AuthSyncClient : AuthSyncClient,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        SymbolNameOrIsin : str,
        Price : int,
        Volume :int,
    ):
        
        """
        Initialize a new Order object.

        Parameters
        ----------
        SendOrder_RequestInfo : dict
            HTTP request configuration for sending the order.

        AuthSyncClient : AuthSyncClient
            Authenticated HTTP client.

        Order_ValidityType : Literal
            Order validity type.

        ValidityDate : int
            Expiration date (for GTD orders).

        SymbolNameOrIsin : str
            Symbol name or ISIN code.

        Price : int
            Order price.

        Volume : int
            Order volume.

        Examples
        --------
        >>> order = client.Buy_by_Name(
        ...     symbolName="اهرم",
        ...     Price=12000,
        ...     Volume=1000
        ... )
        """
        
        self.__AuthSyncClient = AuthSyncClient
        self.__SendOrder_RequestInfo = SendOrder_RequestInfo
        
        self.ValidityType : str = Order_ValidityType
        self.ValidityDate : int = ValidityDate
        self.SymbolNameOrIsin : str = SymbolNameOrIsin
        self.Price : int = Price 
        self.Volume : int = Volume
        self.is_deleted : bool = False
        
        self.OrderId : HexUUID | None = None   
        

    # +--------------------------------------------------------------------------------------+ #
    
    def send(self)-> None:
        
        """
        Send the order to the trading engine.

        This method submits the order to EMS Engine
        and assigns OrderId on success.

        Returns
        -------
        None

        Notes
        -----
        - Can be called only once.
        - Subsequent calls have no effect.

        Examples
        --------
        >>> order.send()
        >>> print(order.OrderId)
        '0xA23F...'
        """
        
        if self.OrderId is None : 
        
            SendOrder_Response = self.__AuthSyncClient.httpx_Client.post(**self.__SendOrder_RequestInfo)
            
            match SendOrder_Response.status_code :
                
                case 200 :
                    
                    self.OrderId = SendOrder_Response.json()['Data']['order_uuid']
                    return None
                    
                case _ : return None
            
        else : return None

    # +--------------------------------------------------------------------------------------+ #
    
    def Edit(
        self,
        *,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        Price : int,
        Volume :int,
    )-> None:
        
        """
        Edit an existing order.

        Parameters
        ----------
        Order_ValidityType : Literal
            New validity type.

        ValidityDate : int
            New expiration date.

        Price : int
            New order price.

        Volume : int
            New order volume.

        Returns
        -------
        None

        Raises
        ------
        None

        Examples
        --------
        >>> order.Edit(Price=12500, Volume=800)
        """
        
        if self.OrderId is not None: 
        
            Edit_response = self.__AuthSyncClient.httpx_Client.patch(
                url='https://core.hedgetech.ir/ems-engine/tse-ifb/order/edit',
                data={
                    'order_uuid' : self.OrderId,
                    'Order_ValidityType' : Order_ValidityType,
                    'ValidityDate' : ValidityDate,
                    'Price' : Price,
                    'Volume' : Volume
                }
            )
            
            
            match Edit_response.status_code:
                
                case 200:
                    
                    Edit_response = Edit_response.json()
                    
                    self.OrderId = Edit_response['Data']['order_uuid']
                    self.ValidityType = Edit_response['Data']['order_validity_type']
                    self.ValidityDate = ValidityDate
                    self.Price = Edit_response['Data']['order_price']
                    self.Volume = Edit_response['Data']['order_volume']
                    
                    return None
                                    
                case _ : return None
        
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #
    
    def Status(self)-> OrderStatus | None:
        
        """
        Retrieve the current status of the order.

        This method queries the EMS Engine and returns detailed
        execution and lifecycle information of the order.

        Returns
        -------
        OrderStatus | None
            A dictionary containing order status information.

            On success, the returned object contains the following fields:

            - order_uuid : HexUUID
                Unique identifier of the order.

            - order_status : Literal['InQueue', 'Cancelled', 'Broken', 'Settled']
                Current lifecycle state of the order.

                * InQueue   : Order is waiting for execution.
                * Cancelled : Order was cancelled.
                * Broken    : Order was rejected or failed.
                * Settled   : Order fully executed.

            - Price : int
                Order price.

            - Volume : int
                Total requested volume.

            - RemainedVolume : int
                Remaining unexecuted volume.

            - ExecutedVolume : int
                Total executed volume.

            - OrderSide : Literal['Buy', 'Sell']
                Side of the order.

            - ValidityType : Literal['DAY', 'GTC', 'GTD']
                Order validity type.

            - ValidityDate : int
                Expiration date (for GTD orders).

            Returns None if the request fails or if the order
            has not been sent yet.

        Raises
        ------
        None

        Notes
        -----
        - This method requires a valid OrderId.
        - If OrderId is None, None is returned.
        - Network or server errors are silently ignored.

        Examples
        --------
        >>> status = order.Status()
        >>> print(status["order_status"])
        'Settled'

        >>> print(status["ExecutedVolume"])
        1000

        >>> if status["RemainedVolume"] == 0:
        ...     print("Order fully executed")

        Example Output
        --------------
        {
            "order_uuid": "0xA91F23BC...",
            "order_status": "Settled",
            "Price": 12000,
            "Volume": 1000,
            "RemainedVolume": 0,
            "ExecutedVolume": 1000,
            "OrderSide": "Buy",
            "ValidityType": "DAY",
            "ValidityDate": 0
        }
        """
        
        if self.OrderId is not None:  
        
            status_respnse = self.__AuthSyncClient.httpx_Client.get(
                url='https://core.hedgetech.ir/ems-engine/tse-ifb/order/status',
                params={'order_uuid' : self.OrderId}
            )
            
            match status_respnse.status_code :
                
                case 200:
                    
                    return status_respnse.json()['Data']
                    
                case _ : return None
                
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #
    
    def Delete(self)-> None :
        
        """
        Cancel/Delete the order.

        Sends delete request to EMS Engine.

        Returns
        -------
        None

        Notes
        -----
        After deletion, `is_deleted` becomes True.

        Examples
        --------
        >>> order.Delete()
        >>> print(order.is_deleted)
        True
        """
        
        if self.OrderId is not None:  
            
            Delete_respnse =  self.__AuthSyncClient.httpx_Client.delete(
                url= 'https://core.hedgetech.ir/ems-engine/tse-ifb/order/delete',
                params={'order_uuid' : self.OrderId}
            )
            

            match Delete_respnse.status_code :
                
                case 200:
                    
                    self.is_deleted = True
                    return None
                
                case _ : return None
        
        else : return None
            
# ================================================================================= #

class EmsEngine_TseIfb_SyncClient:
    
    """
    Synchronous EMS Engine client for TSE/IFB markets.

    This client manages authentication, OMS login,
    and order creation.
    """
    
    def __init__(
        self,
        AuthSyncClient : AuthSyncClient,
    ):
        
        
        self.__AuthSyncClient = AuthSyncClient
        
        self.Customer_FullName : str | None = None
        self.Customer_TSEBourseCode : str | None = None
        self.oms_session : HexUUID | None = None
        
    
    # +--------------------------------------------------------------------------------------+ #
    
    def Get_Captcha(
        self,
        OMS : Literal[
            'Omex | Parsian',
            'Sahra | Karamad',
        ]
    )-> ImageFile:
        
        """
        Fetch captcha image for OMS login.

        Parameters
        ----------
        OMS : Literal
            OMS provider name.

        Returns
        -------
        ImageFile
            Captcha image.

        Raises
        ------
        ValueError
            If server returns error.

        Examples
        --------
        >>> img = client.Get_Captcha("Omex | Parsian")
        >>> img.show()
        """
        
        Captcha = self.__AuthSyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/ems-engine/tse-ifb/oms/login',
            params={'oms' : OMS }
        )
        
        if Captcha.status_code == 200: return image_open(BytesIO(Captcha.content))
        
        else : raise ValueError(Captcha.json()['detail']['Status']['Description']['en'])

    # +--------------------------------------------------------------------------------------+ #
            
    def oms_login(
        self,
        username: str,
        password: str,
        captcha_value: str,
    ) -> None :
        """
        Authenticate user in OMS system.

        Parameters
        ----------
        username : str
            Trading account username.

        password : str
            Trading account password.

        captcha_value : str
            Captcha solution.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If authentication fails.

        Examples
        --------
        >>> client.oms_login("user1", "pass123", "A7B9")
        """
        
        response = self.__AuthSyncClient.httpx_Client.post(
            url='https://core.hedgetech.ir/ems-engine/tse-ifb/oms/login',
            data={
                'username' : username,
                'Password' : password,
                'Captcha_Value' : captcha_value
            },
        )
        
        match response.status_code :
            
            case 200 :
                
                data = response.json()

                self.Customer_FullName = data['Data']['Customer_FullName']
                self.Customer_TSEBourseCode = data['Data']['Customer_TSEBourseCode']
                self.oms_session = data['Data']['oms_session']

                return None
                
            case 400 :
                
                raise ValueError(response.json()['detail']['Status']['Description']['en'])

            case _ :
                
                raise ValueError(response.text)



    # +--------------------------------------------------------------------------------------+ #
    
    
    def Buy_by_Name(
        self,
        *,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        symbolName : str,
        Price : int,
        Volume :int,
    )-> Order | None:
        
        """
        Create a buy order using symbol name.

        Parameters
        ----------
        symbolName : str
            Trading symbol name.

        Price : int
            Order price.

        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            Order instance if logged in, otherwise None.

        Examples
        --------
        >>> order = client.Buy_by_Name(
        ...     symbolName="اهرم",
        ...     Price=12000,
        ...     Volume=1000
        ... )
        >>> order.send()
        """
        
        if self.oms_session is not None: 
        
            return Order(
                AuthSyncClient=self.__AuthSyncClient,
                Order_ValidityType=Order_ValidityType,
                ValidityDate=ValidityDate,
                SymbolNameOrIsin = symbolName,
                Price=Price,
                Volume=Volume,
                SendOrder_RequestInfo = {
                    'url' : 'https://core.hedgetech.ir/ems-engine/tse-ifb/order/new/buy/name',
                    'data' : {
                        'oms_session' : self.oms_session,
                        'Order_ValidityType' : Order_ValidityType,
                        'ValidityDate' : ValidityDate,
                        'symbolName' : symbolName,
                        'Price' : Price,
                        'Volume' : Volume
                    }
                }
            )
            
        else : return None
                        

    # +--------------------------------------------------------------------------------------+ #
    
    
    def Sell_by_Name(
        self,
        *,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        symbolName : str,
        Price : int,
        Volume :int,
    )-> Order | None:
        
        """
        Create a sell order using symbol name.

        Parameters
        ----------
        symbolName : str
            Trading symbol name.

        Price : int
            Order price.

        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            Order instance if logged in, otherwise None.

        Examples
        --------
        >>> order = client.Sell_by_Name(
        ...     symbolName="اهرم",
        ...     Price=12000,
        ...     Volume=1000
        ... )
        >>> order.send()
        """
        
        if self.oms_session is not None: 
        
            return Order(
                AuthSyncClient=self.__AuthSyncClient,
                Order_ValidityType=Order_ValidityType,
                ValidityDate=ValidityDate,
                SymbolNameOrIsin = symbolName,
                Price=Price,
                Volume=Volume,
                SendOrder_RequestInfo = {
                    'url' : 'https://core.hedgetech.ir/ems-engine/tse-ifb/order/new/sell/name',
                    'data' : {
                        'oms_session' : self.oms_session,
                        'Order_ValidityType' : Order_ValidityType,
                        'ValidityDate' : ValidityDate,
                        'symbolName' : symbolName,
                        'Price' : Price,
                        'Volume' : Volume
                    }
                }
            )
            
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #

    def Buy_by_isin(
        self,
        *,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        symbolIsin : str,
        Price : int,
        Volume :int,
    )-> Order | None:
        
        """
        Create a buy order using symbol isin.

        Parameters
        ----------
        symbolIsin : str
            Trading symbol isin.

        Price : int
            Order price.

        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            Order instance if logged in, otherwise None.

        Examples
        --------
        >>> order = client.Buy_by_isin(
        ...     symbolName="اهرم",
        ...     Price=12000,
        ...     Volume=1000
        ... )
        >>> order.send()
        """
        
        if self.oms_session is not None: 
        
            return Order(
                AuthSyncClient=self.__AuthSyncClient,
                Order_ValidityType=Order_ValidityType,
                ValidityDate=ValidityDate,
                SymbolNameOrIsin = symbolIsin,
                Price=Price,
                Volume=Volume,
                SendOrder_RequestInfo = {
                    'url' : 'https://core.hedgetech.ir/ems-engine/tse-ifb/order/new/buy/isin',
                    'data' : {
                        'oms_session' : self.oms_session,
                        'Order_ValidityType' : Order_ValidityType,
                        'ValidityDate' : ValidityDate,
                        'symbolIsin' : symbolIsin,
                        'Price' : Price,
                        'Volume' : Volume
                    }
                }
            )
            
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #
    
    def Sell_by_isin(
        self,
        *,
        Order_ValidityType : Literal[
            'DAY',
            'GTC', # Good Till Cancelled
            'GTD', # Good Till Date
            'FAK', # Fill And Kill
            'FOK', # Fill Or Kill
        ] = 'DAY',
        ValidityDate : int = 0,
        symbolIsin : str,
        Price : int,
        Volume :int,
    )-> Order | None:
        
        """
        Create a sell order using symbol isin.

        Parameters
        ----------
        symbolIsin : str
            Trading symbol isin.

        Price : int
            Order price.

        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            Order instance if logged in, otherwise None.

        Examples
        --------
        >>> order = client.Sell_by_isin(
        ...     symbolName="اهرم",
        ...     Price=12000,
        ...     Volume=1000
        ... )
        >>> order.send()
        """
        
        if self.oms_session is not None: 
        
            return Order(
                AuthSyncClient=self.__AuthSyncClient,
                Order_ValidityType=Order_ValidityType,
                ValidityDate=ValidityDate,
                SymbolNameOrIsin = symbolIsin,
                Price=Price,
                Volume=Volume,
                SendOrder_RequestInfo = {
                    'url' : 'https://core.hedgetech.ir/ems-engine/tse-ifb/order/new/sell/isin',
                    'data' : {
                        'oms_session' : self.oms_session,
                        'Order_ValidityType' : Order_ValidityType,
                        'ValidityDate' : ValidityDate,
                        'symbolIsin' : symbolIsin,
                        'Price' : Price,
                        'Volume' : Volume
                    }
                }
            )
            
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #
            