from dotenv import load_dotenv
import requests, os

ACCESS_KEY = os.getenv('ACCESS_KEY')

class APIManager:
    
    instance = None

    def __init__(self):
        
        if APIManager.instance == None:
            self.access_key = os.get_env("ACCESS_KEY")
            APIManager.instance = self

        else:
            return APIManager.instance

    



# Example usage
if __name__ == "__main__":
    # TEST fn
    pass