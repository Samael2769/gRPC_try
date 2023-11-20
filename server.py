import grpc
import handler_pb2
import handler_pb2_grpc
from concurrent import futures

class handlerServicer(handler_pb2_grpc.handlerServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return handler_pb2.AddResponse(result=result)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    handler_pb2_grpc.add_handlerServicer_to_server(handlerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
