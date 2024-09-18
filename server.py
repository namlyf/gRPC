from concurrent import futures
import grpc
import string_service_pb2
import string_service_pb2_grpc

# Triển khai StringServiceServicer
class StringServiceServicer(string_service_pb2_grpc.StringServiceServicer):
    def Capitalize(self, request, context):
        response_text = request.text.upper()
        return string_service_pb2.CapitalizeResponse(text=response_text)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    string_service_pb2_grpc.add_StringServiceServicer_to_server(StringServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
