# import ..gen.py.test_pb2_grpc as test_pb2_grpc

import sys
import os

os.chdir('..')
base_dir = os.getcwd()

py_proto_dir = os.path.join(base_dir, 'gen', 'py')
sys.path.append(py_proto_dir)

import grpc
from test_pb2 import ResponseRequest
from test_pb2_grpc import TestApiStub

channel = grpc.insecure_channel("localhost:8080")
client = TestApiStub(channel)

request = ResponseRequest(msg="Hello")
print(client.Echo(request))


