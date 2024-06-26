# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pb.stock_pb2 as stock__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in stock_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class StockStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckStock = channel.unary_unary(
                '/stock.Stock/CheckStock',
                request_serializer=stock__pb2.Product.SerializeToString,
                response_deserializer=stock__pb2.ProductStockCheckResponse.FromString,
                _registered_method=True)
        self.ReduceStock = channel.unary_unary(
                '/stock.Stock/ReduceStock',
                request_serializer=stock__pb2.Product.SerializeToString,
                response_deserializer=stock__pb2.ProductStockReduceResponse.FromString,
                _registered_method=True)


class StockServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckStock(self, request, context):
        """checking the stock to start transactions - unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReduceStock(self, request, context):
        """reduce the stock after transactions - unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckStock': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckStock,
                    request_deserializer=stock__pb2.Product.FromString,
                    response_serializer=stock__pb2.ProductStockCheckResponse.SerializeToString,
            ),
            'ReduceStock': grpc.unary_unary_rpc_method_handler(
                    servicer.ReduceStock,
                    request_deserializer=stock__pb2.Product.FromString,
                    response_serializer=stock__pb2.ProductStockReduceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stock.Stock', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Stock(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/stock.Stock/CheckStock',
            stock__pb2.Product.SerializeToString,
            stock__pb2.ProductStockCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReduceStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/stock.Stock/ReduceStock',
            stock__pb2.Product.SerializeToString,
            stock__pb2.ProductStockReduceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
