import grpc
from google.protobuf.json_format import MessageToDict
from pb import transaction_pb2
from pb import transaction_pb2_grpc

from schemas.orders import Transaction

class TransactionClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel(f"localhost:50052")
        self.stub = transaction_pb2_grpc.TransactionStub(self.channel)

    def makeTransaction(self, transaction: Transaction):
        message = self.stub.MakeTransaction(transaction_pb2.TransactionMessage(
            receiver = str(transaction.receiver.id), sender = str(transaction.sender.id),
              amount = transaction.amount
            )
        )
        return MessageToDict(
            message= message, 
            preserving_proto_field_name=True, 
        )

