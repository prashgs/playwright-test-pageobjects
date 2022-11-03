from pydantic import BaseModel
from typing import List, Optional


class NewComputer(BaseModel):
    computerName: str
    introducedData: Optional[str]
    discontinuedData: Optional[str]
    company: Optional[str]


class NewComputersModel(BaseModel):
    newComputers: List[NewComputer]
