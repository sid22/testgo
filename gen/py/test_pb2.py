# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\x04main\"\x1e\n\x0fResponseRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t2A\n\x07TestApi\x12\x36\n\x04\x45\x63ho\x12\x15.main.ResponseRequest\x1a\x15.main.ResponseRequest\"\x00\x42\tZ\x07./protob\x06proto3')



_RESPONSEREQUEST = DESCRIPTOR.message_types_by_name['ResponseRequest']
ResponseRequest = _reflection.GeneratedProtocolMessageType('ResponseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:main.ResponseRequest)
  })
_sym_db.RegisterMessage(ResponseRequest)

_TESTAPI = DESCRIPTOR.services_by_name['TestApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007./proto'
  _RESPONSEREQUEST._serialized_start=20
  _RESPONSEREQUEST._serialized_end=50
  _TESTAPI._serialized_start=52
  _TESTAPI._serialized_end=117
# @@protoc_insertion_point(module_scope)