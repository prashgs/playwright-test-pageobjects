from pydantic import BaseModel
from typing import List, Optional


class NewComputerModel(BaseModel):
    name: str
    introducedData: Optional[str]
    discontinuedData: Optional[str]
    company: Optional[str]


class NewComputers(BaseModel):
    computers = List[NewComputerModel]
