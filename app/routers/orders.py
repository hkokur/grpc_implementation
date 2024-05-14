from schemas.orders import Order, Product, User, Transaction
from business_logic.orders import OrderLogic

from fastapi import APIRouter, Depends
from typing import List

router = APIRouter()

@router.get("/getproducts", status_code=200)
def get_product()-> List[Product]:
    products = []
    products.append(Product(
        id=1,
        owner= User(id=1, username = "Harrey", magicword="Arresto Momentum"),
        name = "produc 1",
        quantity=1,
        price= 14.5
    ))
    products.append(Product(
        id=2,
        owner= User(id=2, username = "Hermione", magicword="Appare Vestigium"),
        name = "produc 2",
        quantity=1,
        price= 104.5
    ))
    products.append(Product(
        id=3,
        owner= User(id=3, username = "Draco", magicword="Caterwauling"),
        name = "produc 3",
        quantity=1,
        price= 124.5
    ))
    products.append(Product(
        id=4,
        owner= User(id=4, username = "Ron", magicword="Expecto Patronum"),
        name = "produc 4",
        quantity=1,
        price= 4.5
    ))
    return products

@router.post("/createorder", status_code=200)
def create_order(
    order_create: Order,
    order_logic: OrderLogic = Depends(OrderLogic)
    ):
    # check the stock all products is avaiable
    # reduce the stock 
    # make transaction between peers
    for product in order_create.products:
        # should be the products will be uniqe by id
        # change quantity if  buy more
        response = order_logic.check_stock(product)
        if response.get("isEnough", False):
            continue
        else:
            return {"message" : "don't enough stock"}
        
    for product in order_create.products:
        response = order_logic.reduce_stock(product)
        if response.get("isSuccess", False):
            continue
        else:
            return {"message" : "can't reduce stock"}
        
     # should check the transaction is possible before the actual transaction
    for product in order_create.products:
        transaction = Transaction(id = 0, receiver=product.owner,
                                  sender = order_create.buyer,
                                  amount = product.price * product.quantity)
        response = order_logic.make_transaction(transaction)
        if response.get("isSuccess", False):
            continue
        else:
            return {
                "message" : "transaction can't be done by peers"
            }    
    
    return {"message" : "success"}

