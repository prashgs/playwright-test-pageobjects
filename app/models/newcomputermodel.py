from pydantic import BaseModel
from typing import List, Optional


class NewComputer(BaseModel):
    computerName: str
    introducedData: Optional[str]
    discontinuedData: Optional[str]
    company: Optional[str]


class NewComputersModel(BaseModel):
    newComputers: List[NewComputer]


# data = {"newComputers": [
#     {
#         "computerName": "Test 111",
#         "introducedData": "2020-01-01",
#         "discontinuedData": "2022-01-01",
#         "company": "Samsung Electronics"
#     },
#     {
#         "computerName": "Test 222",
#         "introducedData": "2020-01-01",
#         "discontinuedData": "2022-01-01",
#         "company": "ASUS"
#     }
# ]}

# a = NewComputersModel(**data)
# print(a)
