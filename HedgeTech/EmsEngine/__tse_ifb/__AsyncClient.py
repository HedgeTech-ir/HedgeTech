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
from HedgeTech.Auth import AuthAsyncClient
from PIL.Image import open as image_open
from PIL.ImageFile import ImageFile
from io import BytesIO
from asyncio import sleep

# ========================================|======================================== #
#                                 Class Definitions                                 #
# ========================================|======================================== #
class Order:
    
    """
    Represents a single trading order in EMS Engine.

    This class provides methods to send, edit, check status,
    and delete an order after creation.

    An Order instance is usually created via
    `EmsEngine_TseIfb_AsyncClient` methods.
    """
    
    def __init__(
        self,
        *,
        SendOrder_RequestInfo : dict,
        AuthASyncClient : AuthAsyncClient,
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
        Represents a stock order in the EMS Engine for TSE IFB.

        This class allows sending, editing, deleting, and checking the status
        of a stock order using an asynchronous client.

        Attributes
        ----------
        ValidityType : str
            Type of order validity ('DAY', 'GTC', 'GTD', 'FAK', 'FOK').
        ValidityDate : int
            Expiration date of the order (for 'GTD' type).
        SymbolNameOrIsin : str
            Symbol name or ISIN code of the security.
        Price : int
            Order price.
        Volume : int
            Order volume.
        is_deleted : bool
            True if the order has been deleted.
        OrderId : HexUUID | None
            Unique identifier of the order after submission.

        Methods
        -------
        send()
            Sends the order asynchronously to the EMS engine.
        Edit(Order_ValidityType, ValidityDate, Price, Volume)
            Edits the existing order asynchronously.
        Status()
            Retrieves the current status of the order asynchronously.
        Delete()
            Deletes the order asynchronously.
        """    
    
        
        self.__AuthASyncClient = AuthASyncClient
        self.__SendOrder_RequestInfo = SendOrder_RequestInfo
        
        self.ValidityType : str = Order_ValidityType
        self.ValidityDate : int = ValidityDate
        self.SymbolNameOrIsin : str = SymbolNameOrIsin
        self.Price : int = Price 
        self.Volume : int = Volume
        self.is_deleted : bool = False

        self.OrderId : HexUUID | None = None   

    # +--------------------------------------------------------------------------------------+ #
    
    async def send(self)-> None:
        
        """
        Sends the order to the EMS engine asynchronously.

        If the order has not been sent before, it posts the request
        using the provided AuthAsyncClient.

        Returns
        -------
        None

        Example
        -------
        >>> order = await client.Buy_by_Name(symbolName="اطلس", Price=100000, Volume=10)
        >>> await order.send()
        >>> print(order.OrderId)
        '953097ac6ced45ca8ef205b76ca6faf2'
        """
        
        if self.OrderId is None : 
        
            SendOrder_Response = await self.__AuthASyncClient.httpx_Client.post(**self.__SendOrder_RequestInfo)
            
            match SendOrder_Response.status_code :
                
                case 200 :
                    
                    self.OrderId = SendOrder_Response.json()['Data']['order_uuid']
                    return None
                    
                case _ : return None
                            
        else : return None
        
    # +--------------------------------------------------------------------------------------+ #
    async def Edit(
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
        Edits an existing order asynchronously.

        Parameters
        ----------
        Order_ValidityType : str
            The new order validity type.
        ValidityDate : int
            New expiration date if validity type is 'GTD'.
        Price : int
            New order price.
        Volume : int
            New order volume.

        Returns
        -------
        None

        Example
        -------
        >>> await order.Edit(Price=105, Volume=15)
        """
        
        if self.OrderId is not None: 
        
            Edit_response = await self.__AuthASyncClient.httpx_Client.patch(
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

    async def Status(self)-> OrderStatus | None:
        
        """
        Retrieves the current status of the order asynchronously.

        Returns
        -------
        OrderStatus | None
            A dictionary containing the current order status with the following keys:
                - order_uuid: HexUUID, unique identifier of the order.
                - order_status: 'InQueue' | 'Cancelled' | 'Broken' | 'Settled'
                - Price: int, the order price.
                - Volume: int, the original order volume.
                - RemainedVolume: int, volume remaining unexecuted.
                - ExecutedVolume: int, executed volume.
                - OrderSide: 'Buy' | 'Sell', the order side.
                - ValidityType: 'DAY' | 'GTC' | 'GTD', the type of order validity.
                - ValidityDate: int, expiration date if applicable.

        Example
        -------
        >>> status = await order.Status()
        >>> print(status)
        {
            'order_uuid': '953097ac6ced45ca8ef205b76ca6faf2',
            'order_status': 'InQueue',
            'Price': 100,
            'Volume': 10,
            'RemainedVolume': 10,
            'ExecutedVolume': 0,
            'OrderSide': 'Buy',
            'ValidityType': 'DAY',
            'ValidityDate': 0
        }
        """
        
        if self.OrderId is not None:  
        
            status_respnse = await self.__AuthASyncClient.httpx_Client.get(
                url='https://core.hedgetech.ir/ems-engine/tse-ifb/order/status',
                params={'order_uuid' : self.OrderId}
            )
            
            match status_respnse.status_code :
                
                case 200:
                    
                    return status_respnse.json()['Data']
                    
                case _ : return None
                
        else : return None
            
    # +--------------------------------------------------------------------------------------+ #
    
    async def Delete(self)-> None:
        
        """
        Deletes the order asynchronously.

        Sets `is_deleted` to True if successful.

        Returns
        -------
        None

        Example
        -------
        >>> await order.Delete()
        >>> print(order.is_deleted)
        True
        """
                
        if self.OrderId is not None:  
        
            Delete_respnse =  await self.__AuthASyncClient.httpx_Client.delete(
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

class EmsEngine_TseIfb_AsyncClient:
    
    """
    Asynchronous EMS Engine client for TSE/IFB markets.

    This client manages authentication, OMS login,
    and order creation.
    """
    
    def __init__(
        self,
        AuthASyncClient : AuthAsyncClient,
    ):
      
        """
        Asynchronous client for interacting with the EMS Engine (TSE IFB).

        Provides methods for logging in, retrieving CAPTCHA, and creating buy/sell orders
        by symbol name or ISIN.

        Attributes
        ----------
        Customer_FullName : str | None
            Full name of the logged-in customer.
        Customer_TSEBourseCode : str | None
            TSE bourse code of the customer.
        oms_session : HexUUID | None
            Session token obtained after login.

        Methods
        -------
        Get_Captcha(OMS)
            Retrieves the login CAPTCHA image asynchronously.
            
        oms_login(username, password, captcha_value)
            Logs into the OMS asynchronously.
            
        Buy_by_Name(Order_ValidityType, ValidityDate, symbolName, Price, Volume)
            Creates a new buy order by symbol name asynchronously.
            
        Sell_by_Name(Order_ValidityType, ValidityDate, symbolName, Price, Volume)
            Creates a new sell order by symbol name asynchronously.
            
        Buy_by_isin(Order_ValidityType, ValidityDate, symbolIsin, Price, Volume)
            Creates a new buy order by ISIN asynchronously.
            
        Sell_by_isin(Order_ValidityType, ValidityDate, symbolIsin, Price, Volume)
            Creates a new sell order by ISIN asynchronously.
        """  
        
        self.__AuthASyncClient = AuthASyncClient
        
        self.Customer_FullName : str | None = None
        self.Customer_TSEBourseCode : str | None = None
        self.oms_session : HexUUID | None = None
        
    # +--------------------------------------------------------------------------------------+ #
    
    
    async def Get_Captcha(
        self,
        OMS : Literal[
            'Omex | Parsian',
            'Sahra | Karamad',
        ]
    )-> ImageFile:
        
        """
        Retrieves the CAPTCHA image for the specified OMS asynchronously.

        Parameters
        ----------
        OMS : str
            OMS identifier ('Omex | Parsian' or 'Sahra | Karamad').

        Returns
        -------
        ImageFile
            The CAPTCHA image object.

        Raises
        ------
        ValueError
            If the request fails or returns an error.

        Example
        -------
        >>> captcha = await client.Get_Captcha('Omex | Parsian')
        >>> captcha.show()
        """
        
        Captcha = await self.__AuthASyncClient.httpx_Client.get(
            url='https://core.hedgetech.ir/ems-engine/tse-ifb/oms/login',
            params={'oms' : OMS }
        )
        
        if Captcha.status_code == 200: return image_open(BytesIO(Captcha.content))
        
        else : raise ValueError(Captcha.json()['detail']['Status']['Description']['en'])
    
    
    # +--------------------------------------------------------------------------------------+ #
    
    async def oms_login(
        self,
        username: str,
        password: str,
        captcha_value: str,
    ) -> None :
        
        """
        Logs into the OMS asynchronously with provided credentials and CAPTCHA.

        Parameters
        ----------
        username : str
            OMS username.
        password : str
            OMS password.
        captcha_value : str
            Solved CAPTCHA value.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If login fails or CAPTCHA is invalid.

        Example
        -------
        >>> await client.oms_login("user123", "pass123", "abcd")
        >>> print(client.oms_session)
        'session_token_here'
        """

        response = await self.__AuthASyncClient.httpx_Client.post(
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
    
    
    async def Buy_by_Name(
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
        Creates a new buy order by symbol name asynchronously.

        Parameters
        ----------
        Order_ValidityType : str
            Order validity type.
        ValidityDate : int
            Expiration date if validity type is 'GTD'.
        symbolName : str
            Symbol name of the security.
        Price : int
            Order price.
        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            A new Order instance if OMS session exists, else None.

        Example
        -------
        >>> order = await client.Buy_by_Name(symbolName="اطلس", Price=100000, Volume=10)
        >>> await order.send()
        """
        
        await sleep(0)
        
        if self.oms_session is not None: 
        
            return Order(
                AuthASyncClient=self.__AuthASyncClient,
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
    
    
    async def Sell_by_Name(
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
        Creates a new sell order by symbol name asynchronously.

        Parameters
        ----------
        Order_ValidityType : str
            Order validity type.
        ValidityDate : int
            Expiration date if validity type is 'GTD'.
        symbolName : str
            Symbol name of the security.
        Price : int
            Order price.
        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            A new Order instance if OMS session exists, else None.

        Example
        -------
        >>> order = await client.Sell_by_Name(symbolName="اطلس", Price=100000, Volume=10)
        >>> await order.send()
        """
        
        await sleep(0)
        
        if self.oms_session is not None: 
            
            return Order(
                AuthASyncClient=self.__AuthASyncClient,
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

    async def Buy_by_isin(
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
        Creates a new buy order by symbol isin asynchronously.

        Parameters
        ----------
        Order_ValidityType : str
            Order validity type.
        ValidityDate : int
            Expiration date if validity type is 'GTD'.
        symbolIsin : str
            Symbol name of the security.
        Price : int
            Order price.
        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            A new Order instance if OMS session exists, else None.

        Example
        -------
        >>> order = await client.Buy_by_isin(symbolIsin="اطلس", Price=100000, Volume=10)
        >>> await order.send()
        """
        
        await sleep(0)    
    
        if self.oms_session is not None: 
            
            return Order(
                AuthASyncClient=self.__AuthASyncClient,
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
    
    async def Sell_by_isin(
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
        Creates a new sell order by symbol isin asynchronously.

        Parameters
        ----------
        Order_ValidityType : str
            Order validity type.
        ValidityDate : int
            Expiration date if validity type is 'GTD'.
        symbolIsin : str
            Symbol name of the security.
        Price : int
            Order price.
        Volume : int
            Order volume.

        Returns
        -------
        Order | None
            A new Order instance if OMS session exists, else None.

        Example
        -------
        >>> order = await client.Sell_by_isin(symbolIsin="اطلس", Price=100000, Volume=10)
        >>> await order.send()
        """
        
        await sleep(0)
        
        if self.oms_session is not None: 
        
            return Order(
                AuthASyncClient=self.__AuthASyncClient,
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
            