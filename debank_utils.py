from debank_utils_typehint import ParamUserProtocolAllChain, ParamUserProtocol
from custom_logging import setup_logging
import requests, os

from dotenv import load_dotenv
load_dotenv()

import logging

logger_info, logger_error = setup_logging("debank_utils_info.log", "debank_utils_error.log")

# Use these loggers throughout your code
logger_info.info("This is an info message")
logger_error.error("This is an error message")

if os.getenv("ACCESS_KEY") == None:
    error_message = "Access key was not found in .env file"
    logger_error.error(error_message)
    raise Exception(error_message)

else:
    success_message = f'Loaded access key: {os.getenv("ACCESS_KEY")}'
    logging.info(success_message)
    print(success_message)

class Get:

    headers = {
        'accept': 'application/json',
        'AccessKey': os.getenv("ACCESS_KEY")
    }

    def get_user_protocol(strategy_name:str, params):
        
        switcher = {

        }

    def _get_user_protocol_complex_list(params: ParamUserProtocol):
        '''
        Parameters
            chain_id : required, chain id, eg: eth, bsc, xdai, for more info.
            id : required, user address

        Returns
            Return user's positions list from all the protocols

            Array of object:
            id : string - The protocol's id.
            chain : string - The chain's id.
            name : string - The protocol's name. null if not defined in the contract and not available from other sources.
            logo_url : string - URL of the protocol's logo image. null if not available.
            site_url : string - prioritize websites that can be interacted with, not official websites.
            has_supported_portfolio : boolean - Is the portfolio already supported.
            portfolio_item_list : Array of PortfolioItemObject
        '''

        api_endpoint = APIManager.parse_path("/v1/user/complex_protocol_list")
        data = APIManager.call_endpoint(api_endpoint, params)
        print(data)

    def _get_user_protocol_all_complex_list(params: ParamUserProtocolAllChain):
        

        '''
        Parameters
            id : required, user address
            chain_ids : optional, list of chain id, eg: eth, bsc, xdai, for more info.

        Returns
            
            Array of Object - return list of protocols with user assets.An object with following fields:
                id : string - The protocol's id.
                chain : string - The chain's id.
                name : string - The protocol's name. null if not defined in the contract and not available from other sources.
                logo_url : string - URL of the protocol's logo image. null if not available.
                site_url : string - prioritize websites that can be interacted with, not official websites.
                has_supported_portfolio : boolean - Is the portfolio already supported.
                net_usd_value : double - The amount of the user's net assets in the protocol.
                asset_usd_value : double - The amount of the user's total assets in the protocol.
                debt_usd_value : double - The Debt USD value.

        Example of curl : "https://pro-openapi.debank.com/v1/user/all_complex_protocol_list?id=YOUR_ADDRESS&chain_ids=bsc,eth \ -H "accept: application/json" -H 'AccessKey: YOUR_ACCESSKEY'
        '''

        api_endpoint = APIManager.parse_path("/v1/user/all_complex_protocol_list")
        data = APIManager.call_endpoint(api_endpoint, params)
        print(data)
        
        

class APIEndpoint:
    
    api_base_url = f'https://pro-openapi.debank.com'

    def parse_path(api_path:str):
        api_endpoint = f"{APIEndpoint.api_base_url}{api_path}"
        return api_endpoint
    
    def call_endpoint(api_endpoint: str, params):        
        
        try:
            # Making the GET request
            response = requests.get(api_endpoint, headers= Get.headers, params=params)
            
            # Check if the request was successful
            if response.status_code == 200:
                # If the request was successful, parse the JSON response
                data = response.json()
                return data
            else:
                # Handle potential errors - for instance, by logging the error
                error_message = f"Error occurred: {response.status_code} - {response.text}"
                print(error_message)
                logger_error.error(error_message)
                return None
            
        except Exception as e:
            # Log any exceptions that occur during the request
            error_message = "An exception occurred"
            print(error_message)
            logging.exception(error_message)
            return None

class APIManager(APIEndpoint):
    
    instance = None

    def __init__(self):
        
        if APIManager.instance == None:
            self.access_key = os.getenv("ACCESS_KEY")
            APIManager.instance = self

        else:
            return APIManager.instance

# Example usage
if __name__ == "__main__":
    # TEST fn
    test_get_complex_protocol_param = {
        "id": "0x803a897bDEfdba303738c601f082bf563f5a8B6E",
        "chain_id": "blast"
    }

    test_get_all_complex_protocol_param = {
        "id": "0x803a897bDEfdba303738c601f082bf563f5a8B6E"
    }
    jd_data = Get._get_user_protocol_complex_list(test_get_complex_protocol_param)
    print(jd_data)
    pass