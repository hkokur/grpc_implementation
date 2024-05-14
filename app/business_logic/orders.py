from grpc_clients.stock_client import StockClient
from grpc_clients.transaction_client import TransactionClient


class OrderLogic():
    def __init__(self):
        self.stock_client = StockClient()
        self.transaction_client = TransactionClient()

    def check_stock(self, product):
        return self.stock_client.checkStock(product)
        
    def reduce_stock(self, product):
        return self.stock_client.reduceStock(product)
        
    def make_transaction(self,transaction):
        return self.transaction_client.makeTransaction(transaction)


