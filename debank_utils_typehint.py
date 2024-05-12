from typing import TypedDict, Optional, List,Dict


class ParamsUserProtocolAllChain(TypedDict):
    id: str
    chainId: Optional[str]

class ParamsUserProtocol(TypedDict):
    id: str
    chainId: str

class ParamsUserTokenBalance(TypedDict):
    chain_id: str  # Chain ID, e.g., 'eth', 'bsc', 'xdai'.
    id: str  # User address.
    token_id: str  # Ethereum Address or native token id.

class ReturnUserTokenBalance(TypedDict):
    id: str  # The address of the token contract.
    chain: str  # The chain's name.
    name: Optional[str]  # The token's name. None if not defined.
    symbol: Optional[str]  # The token's symbol. None if not defined.
    display_symbol: str  # The token's displayed symbol.
    optimized_symbol: str  # For front-end display.
    decimals: Optional[int]  # The number of decimals of the token.
    logo_url: Optional[str]  # URL of the token's logo image.
    is_verified: bool  # Whether it has been verified.
    is_core: bool  # Whether it is considered a common token in the wallet.
    price: float  # USD price. A price of 0 indicates no data.
    time_at: int  # The timestamp of token deployment on the blockchain.
    amount: float  # The amount of the user's token.
    raw_amount: int  # The raw amount of the user's token.

class ReturnUserTotalBalance(TypedDict):
    total_usd_value: float  # The total price of all assets in USD in the user's account.

class ReturnUserTotalBalance(TypedDict):
    total_usd_value: float  # The total price of all assets in USD in the user's account.
    balances_by_chain: Dict[str, float]  # Optional: Balances per chain, key is the chain name, value is the balance.

class TokenDetails(TypedDict, total=False):
    id: str  # The address of the token contract.
    chain: str  # The chain's name.
    name: Optional[str]  # The token's name. None if not defined.
    symbol: Optional[str]  # The token's symbol. None if not defined.
    display_symbol: str  # The token's displayed symbol.
    optimized_symbol: str  # For front-end display. Uses optimized_symbol, display_symbol, or symbol.
    decimals: Optional[int]  # The number of decimals of the token.
    logo_url: Optional[str]  # URL of the token's logo image.
    is_core: bool  # Whether it is considered a common token in the wallet.
    price: float  # USD price. A price of 0 indicates no data.
    time_at: int  # The timestamp of token deployment on the blockchain.
    amount: float  # The amount of the user's token.
    raw_amount: int  # The raw amount of the user's token.

class ReturnUserTokenList(TypedDict):
    tokens: List[TokenDetails]  # List of tokens.

class ParamsAllTokenList(TypedDict, total=False):
    id: str  # User address.
    is_all: Optional[bool]  # True if all tokens are returned, including special cases. Defaults to True.
    chain_ids: Optional[List[str]]  # Optional list of chain IDs, e.g., 'eth', 'bsc', 'xdai'.

class ReturnAllTokenList(TypedDict):
    tokens: List[TokenDetails]  # List of tokens.


