import logging
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc

# ロギングの設定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Greeter(service_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        logging.info(f"Received a request with name: {request.name}")
        return service_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:9501')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

