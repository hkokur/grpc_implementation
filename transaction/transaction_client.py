import grpc
from google.protobuf.json_format import MessageToDict
from transaction import transaction_pb2
from transaction import transaction_pb2_grpc

from app.schemas.orders import Transaction

class TransactionClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel(f"localhost:50052")
        self.stub = transaction_pb2_grpc.TransactionStub(self.channel)

    def makeTransaction(self, transaction: Transaction):
        message = self.stub.MakeTransaction(transaction_pb2.TransactionMessage(
            reciever = transaction.reciever.id, sender = transaction.sender.id,
              amount = transaction.amount
            )
        )
        return MessageToDict(
            message= message, 
            preserving_proto_field_name=True, 
            including_default_value_fields = True
        )

