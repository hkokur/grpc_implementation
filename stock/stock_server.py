from concurrent import futures

import grpc

import stock_pb2
import stock_pb2_grpc



database = {
    # product id : stock
    1 : 10,
    2 : 20, 
    3 : 30,
    4 : 40
}

## CAN ADD GRPC EXCEPTIONS

class StockServicer(stock_pb2_grpc.StockServicer):
    def CheckStock(self, request, context):
        checkResponse = stock_pb2.ProductStockCheckResponse()
        product_stock = database.get(request.id, None)
        if product_stock is not None:
            if product_stock >= request.quantity:
                print(f"{request.id} stock is enough!")
                checkResponse.isEnough = True
                return checkResponse
        checkResponse.isEnough = False
        return checkResponse

    def ReduceStock(self, request, context):
        reduceResponse = stock_pb2.ProductStockReduceResponse()
        product_stock = database.get(request.id, None)
        if product_stock is not None:
            if product_stock >= request.quantity: 
                print(f"{request.id} stock is reduced({request.quantity})")
                database[request.id] -= request.quantity
                reduceResponse.isSuccess = True
                return reduceResponse
        reduceResponse.isSuccess = False
        return reduceResponse

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_pb2_grpc.add_StockServicer_to_server(StockServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
