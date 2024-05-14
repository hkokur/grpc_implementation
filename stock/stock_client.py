import grpc

from stock import stock_pb2
from stock import stock_pb2_grpc
from google.protobuf.json_format import MessageToDict

from app.schemas.orders import Product

class StockClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel(f"localhost:50051")
        self.stub = stock_pb2_grpc.StockStub(self.channel)

    def checkStock(self, product: Product ):
        message = self.stub.CheckStock(stock_pb2.Product(
            id = product.id, quantity = product.quantity
            )
        )

        return MessageToDict(
            message= message, 
            preserving_proto_field_name=True, 
        )
    
    def reduceStock(self, product: Product):
        message = self.stub.ReduceStock(stock_pb2.Product(
            id = product.id, quantity = product.quantity
            )
        )

        return MessageToDict(
            message= message, 
            preserving_proto_field_name=True, 
        )
        
