from enum import Enum
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    magicword: str


class Transaction(BaseModel):
    id: int
    receiver: User
    sender: User
    amount: float


# sender = owner, they are equal
class Product(BaseModel):
    id: int
    owner: User
    name: str
    quantity: int
    price: float


class Order(BaseModel):
    id: int
    products: list[Product]
    buyer: User
