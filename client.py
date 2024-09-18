import grpc
import string_service_pb2
import string_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = string_service_pb2_grpc.StringServiceStub(channel)

        while True:
        
            text = input("Your message: ")

            request = string_service_pb2.CapitalizeRequest(text=text)
            response = stub.Capitalize(request)

            print(f"Original Text: {text}")
            print(f"Capitalized Text: {response.text}")

if __name__ == '__main__':
    run()
