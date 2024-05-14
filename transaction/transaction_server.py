from concurrent import futures

import grpc
import transaction_pb2
import transaction_pb2_grpc

database = {
    # user id : money in account
    "1" : 1000,
    "2" : 2500,
    "3" : 3000
}

class TransactionServicer(transaction_pb2_grpc.TransactionServicer):
    def MakeTransaction(self, request, context):
        transactionResponse = transaction_pb2.TransactionResponse()
        sender_amount = database.get(request.sender, None)
        if sender_amount >= request.amount:
            if database.get(request.receiver, None) is not None:
                print(f"Money transfered from user {request.sender} to user {request.receiver}")
                database[request.receiver] += request.amount
                database[request.sender] -+ request.amount
                transactionResponse.isSuccess = True
                return transactionResponse
        transactionResponse.isSuccess = False
        return transactionResponse


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_pb2_grpc.add_TransactionServicer_to_server(
        TransactionServicer(), server
    )
    server.add_insecure_port("localhost:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
