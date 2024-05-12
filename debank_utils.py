from debank_utils_typehint import ParamsUserProtocolAllChain, ParamsUserProtocol
from ratelimit import limits, sleep_and_retry
from custom_logging import setup_logging
import requests, os, json

from dotenv import load_dotenv
load_dotenv()

import logging



def read_json_data(primary_file, backup_file):
    try:
        if os.path.exists(primary_file) and os.path.getsize(primary_file) > 0:
            with open(primary_file, 'r') as file:
                data = json.load(file)
                if data:  # Checks if data is not empty
                    return data
        # If primary file is empty or doesn't exist, read from backup file
        if os.path.exists(backup_file) and os.path.getsize(backup_file) > 0:
            with open(backup_file, 'r') as file:
                data = json.load(file)
                return data
        return []  # Returns empty list if both files are empty or don't exist
    except json.JSONDecodeError:
        return []  # Handles the case where file content is not valid JSON

class Get:

    headers = {
        'accept': 'application/json',
        'AccessKey': os.getenv("ACCESS_KEY")
    }

    def user_protocol(strategy_name:str, params):
        
        strategy = {
            "simple_list": Get.__user_protocol_simple_list,
            "all_simple_list": Get.__user_protocol_all_simple_list,
            "complex_list" : Get.__user_protocol_complex_list,
            "all_complex_list" : Get.__user_protocol_all_complex_list
        }
        data = strategy[strategy_name](params)
        print(data)
        return data
        
    
    def __user_protocol_simple_list( params:ParamsUserProtocolAllChain):
        """
        Parameters
            chain_id : required, chain id, eg: eth, bsc, xdai, for more info.

            id : required, user address

        Returns
            return list of protocols with user assets.
            Array of Object - An object with following fields:
            id : string - The protocol's id.
            chain : string - The chain's id.
            name : string - The protocol's name. null if not defined in the contract and not available from other sources.
            logo_url : string - URL of the protocol's logo image. null if not available.
            site_url : string - prioritize websites that can be interacted with, not official websites.
            has_supported_portfolio : boolean - Is the portfolio already supported.
            net_usd_value : double - The amount of the user's net assets in the protocol.
            asset_usd_value : double - The amount of the user's total assets in the protocol.
            debt_usd_value : double - The Debt USD value.
        """
        api_endpoint = APIManager.parse_path("/v1/user/simple_protocol_list")
        data = APIManager.call_endpoint(api_endpoint, params)
        
        return data

    def __user_protocol_all_simple_list( params:ParamsUserProtocolAllChain):
        api_endpoint = APIManager.parse_path("/v1/user/all_simple_protocol_list")
        data = APIManager.call_endpoint(api_endpoint, params)
        
        return data

    def __user_protocol_complex_list( params: ParamsUserProtocol):
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
        
        return data

    def __user_protocol_all_complex_list(params: ParamsUserProtocolAllChain):
        

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
        
        return data       

# This class parses endpoint path and interact directly with API
class APIEndpoint:
    '''
    functions all uses logger
        parse_path
        call_endpoint 
    '''
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
                logger_info.info(f'Called endpoint {api_endpoint} : Success\nParamters: {params}')
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

# Singleton
class APIManager(APIEndpoint):
    
    instance = None

    def __init__(self):
        
        if APIManager.instance == None:
            self.access_key = os.getenv("ACCESS_KEY")
            APIManager.instance = self

        else:
            return APIManager.instance


if __name__ == "__main__":

    

    def read_json_data(primary_file, backup_file):
        try:
            # First try to read from the primary file (input_address.test.json)
            if os.path.exists(primary_file) and os.path.getsize(primary_file) > 0:
                with open(primary_file, 'r') as file:
                    data = json.load(file)
                    if data:  # Checks if data is not empty
                        return data
            # If primary file is empty or doesn't exist, read from backup file (input_address.json)
            if os.path.exists(backup_file) and os.path.getsize(backup_file) > 0:
                with open(backup_file, 'r') as file:
                    data = json.load(file)
                    return data
            return []  # Returns empty list if both files are empty or don't exist
        except json.JSONDecodeError:
            return []  # Handles the case where file content is not valid JSON

    # File paths, switched to prioritize input_address.test.json
    primary_file_path = 'input_address.test.json'
    backup_file_path = 'input_address.json'


    logger_info, logger_error = setup_logging("debank_utils_info.log","debank_utils_error.log")
    # Write the data to a JSON file
    
    # Constants
    RATE_LIMIT_CALLS = 70
    RATE_LIMIT_PERIOD = 60  # 70 calls per 60 seconds

    @sleep_and_retry
    @limits(calls=RATE_LIMIT_CALLS, period=RATE_LIMIT_PERIOD)
    def rate_limited_user_protocol(wallet):
        # Assuming that 'params' takes a dictionary with 'id'
        return Get.user_protocol("all_complex_list", params={"id": wallet})

    def gather_data(wallets):
        results = []
        for each_wallet in wallets:
            data = rate_limited_user_protocol(each_wallet)
            if data:
                results.append(data)
        return results

    def write_to_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to {file_path}")

    # Main execution function
    def main():
        # Example wallet addresses loaded into 'meow'
        
            # Read data and store in variable 'meow'
        meow = read_json_data(primary_file_path, backup_file_path)
        
        # Gather data
        compiled_data = gather_data(meow)
        
        # Write data to JSON file
        write_to_json("output_data.json", compiled_data)
        
    main()

    ####
    '''
    jd_data = Get.user_protocol(strategy_name="all_complex_list",params=test_get_complex_protocol_params)
    print(jd_data)
    
    
    '''
    ####
    pass