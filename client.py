import grpc
import handler_pb2
import handler_pb2_grpc

def run_client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = handler_pb2_grpc.handlerStub(channel)
        response = stub.Add(handler_pb2.AddRequest(num1=10, num2=5))
        print("Result: ", response.result)

if __name__ == '__main__':
    run_client()
