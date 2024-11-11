import logging
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
from grpc_reflection.v1alpha import reflection

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"Received a request with name: {request.name}")
        return service_pb2.HelloReply(message='Hello, %s!' % request.name)

class HealthServicer(service_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        logging.info(f"Received a health request")
        return service_pb2.HealthCheckResponse(status=service_pb2.HealthCheckResponse.SERVING)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    service_pb2_grpc.add_HealthServicer_to_server(HealthServicer(), server)

    # Reflection serviceの追加
    SERVICE_NAMES = [
        service_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        service_pb2.DESCRIPTOR.services_by_name['Health'].full_name,
        reflection.SERVICE_NAME,
    ]
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:9501')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

