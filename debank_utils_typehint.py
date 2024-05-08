from typing import TypedDict, Optional

class ParamUserProtocolAllChain(TypedDict):
    id: str
    chainId: Optional[str]

class ParamUserProtocol(TypedDict):
    id: str
    chainId: str

