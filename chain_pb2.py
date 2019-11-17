# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chain.proto',
  package='adb',
  syntax='proto3',
  serialized_options=_b('\n\024edu.sjsu.cs249.chainP\001'),
  serialized_pb=_b('\n\x0b\x63hain.proto\x12\x03\x61\x64\x62\"N\n\x16HeadStateUpdateRequest\x12\x0b\n\x03src\x18\x01 \x01(\x04\x12\x0b\n\x03xid\x18\x02 \x01(\x04\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x05\"x\n\x16TailStateUpdateRequest\x12\x0b\n\x03src\x18\x01 \x01(\x04\x12\x0b\n\x03xid\x18\x02 \x01(\x04\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x05\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\x12\x0c\n\x04\x63xid\x18\x07 \x01(\x05\"\x12\n\x10LatestXidRequest\",\n\x11LatestXidResponse\x12\n\n\x02rc\x18\x01 \x01(\r\x12\x0b\n\x03xid\x18\x02 \x01(\x04\"\xcb\x01\n\x18HeadStateTransferRequest\x12\x0b\n\x03src\x18\x01 \x01(\x04\x12\x10\n\x08stateXid\x18\x02 \x01(\x04\x12\x37\n\x05state\x18\x03 \x03(\x0b\x32(.adb.HeadStateTransferRequest.StateEntry\x12)\n\x04sent\x18\x04 \x03(\x0b\x32\x1b.adb.HeadStateUpdateRequest\x1a,\n\nStateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xcb\x01\n\x18TailStateTransferRequest\x12\x0b\n\x03src\x18\x01 \x01(\x04\x12\x10\n\x08stateXid\x18\x02 \x01(\x04\x12\x37\n\x05state\x18\x03 \x03(\x0b\x32(.adb.TailStateTransferRequest.StateEntry\x12)\n\x04sent\x18\x04 \x03(\x0b\x32\x1b.adb.TailStateUpdateRequest\x1a,\n\nStateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x1b\n\rChainResponse\x12\n\n\x02rc\x18\x01 \x01(\r\"2\n\x10IncrementRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tincrValue\x18\x02 \x01(\x05\"\x1c\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"`\n\x14TailIncrementRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tincrValue\x18\x02 \x01(\x05\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x0c\n\x04\x63xid\x18\x05 \x01(\x05\"J\n\x11TailDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0c\n\x04\x63xid\x18\x04 \x01(\x05\"\x1a\n\x0cHeadResponse\x12\n\n\x02rc\x18\x01 \x01(\r\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"(\n\x0bGetResponse\x12\n\n\x02rc\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x05\"\"\n\x13XidProcessedRequest\x12\x0b\n\x03xid\x18\x01 \x01(\x04\"$\n\x14\x43xidProcessedRequest\x12\x0c\n\x04\x63xid\x18\x01 \x01(\x05\x32\xac\x03\n\x10HeadChainReplica\x12\x45\n\x12proposeStateUpdate\x12\x1b.adb.HeadStateUpdateRequest\x1a\x12.adb.ChainResponse\x12=\n\x0cgetLatestXid\x12\x15.adb.LatestXidRequest\x1a\x16.adb.LatestXidResponse\x12\x42\n\rstateTransfer\x12\x1d.adb.HeadStateTransferRequest\x1a\x12.adb.ChainResponse\x12\x35\n\tincrement\x12\x15.adb.IncrementRequest\x1a\x11.adb.HeadResponse\x12/\n\x06\x64\x65lete\x12\x12.adb.DeleteRequest\x1a\x11.adb.HeadResponse\x12(\n\x03get\x12\x0f.adb.GetRequest\x1a\x10.adb.GetResponse\x12<\n\x0cxidProcessed\x12\x18.adb.XidProcessedRequest\x1a\x12.adb.ChainResponse2\xf6\x02\n\x10TailChainReplica\x12\x45\n\x12proposeStateUpdate\x12\x1b.adb.TailStateUpdateRequest\x1a\x12.adb.ChainResponse\x12=\n\x0cgetLatestXid\x12\x15.adb.LatestXidRequest\x1a\x16.adb.LatestXidResponse\x12\x42\n\rstateTransfer\x12\x1d.adb.TailStateTransferRequest\x1a\x12.adb.ChainResponse\x12\x39\n\tincrement\x12\x19.adb.TailIncrementRequest\x1a\x11.adb.HeadResponse\x12\x33\n\x06\x64\x65lete\x12\x16.adb.TailDeleteRequest\x1a\x11.adb.HeadResponse\x12(\n\x03get\x12\x0f.adb.GetRequest\x1a\x10.adb.GetResponse2L\n\nTailClient\x12>\n\rcxidProcessed\x12\x19.adb.CxidProcessedRequest\x1a\x12.adb.ChainResponseB\x18\n\x14\x65\x64u.sjsu.cs249.chainP\x01\x62\x06proto3')
)




_HEADSTATEUPDATEREQUEST = _descriptor.Descriptor(
  name='HeadStateUpdateRequest',
  full_name='adb.HeadStateUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='adb.HeadStateUpdateRequest.src', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xid', full_name='adb.HeadStateUpdateRequest.xid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.HeadStateUpdateRequest.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='adb.HeadStateUpdateRequest.value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=98,
)


_TAILSTATEUPDATEREQUEST = _descriptor.Descriptor(
  name='TailStateUpdateRequest',
  full_name='adb.TailStateUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='adb.TailStateUpdateRequest.src', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xid', full_name='adb.TailStateUpdateRequest.xid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.TailStateUpdateRequest.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='adb.TailStateUpdateRequest.value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='adb.TailStateUpdateRequest.host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='adb.TailStateUpdateRequest.port', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cxid', full_name='adb.TailStateUpdateRequest.cxid', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=220,
)


_LATESTXIDREQUEST = _descriptor.Descriptor(
  name='LatestXidRequest',
  full_name='adb.LatestXidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=240,
)


_LATESTXIDRESPONSE = _descriptor.Descriptor(
  name='LatestXidResponse',
  full_name='adb.LatestXidResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='adb.LatestXidResponse.rc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xid', full_name='adb.LatestXidResponse.xid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=286,
)


_HEADSTATETRANSFERREQUEST_STATEENTRY = _descriptor.Descriptor(
  name='StateEntry',
  full_name='adb.HeadStateTransferRequest.StateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.HeadStateTransferRequest.StateEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='adb.HeadStateTransferRequest.StateEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=492,
)

_HEADSTATETRANSFERREQUEST = _descriptor.Descriptor(
  name='HeadStateTransferRequest',
  full_name='adb.HeadStateTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='adb.HeadStateTransferRequest.src', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stateXid', full_name='adb.HeadStateTransferRequest.stateXid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='adb.HeadStateTransferRequest.state', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent', full_name='adb.HeadStateTransferRequest.sent', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HEADSTATETRANSFERREQUEST_STATEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=492,
)


_TAILSTATETRANSFERREQUEST_STATEENTRY = _descriptor.Descriptor(
  name='StateEntry',
  full_name='adb.TailStateTransferRequest.StateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.TailStateTransferRequest.StateEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='adb.TailStateTransferRequest.StateEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=492,
)

_TAILSTATETRANSFERREQUEST = _descriptor.Descriptor(
  name='TailStateTransferRequest',
  full_name='adb.TailStateTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='adb.TailStateTransferRequest.src', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stateXid', full_name='adb.TailStateTransferRequest.stateXid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='adb.TailStateTransferRequest.state', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent', full_name='adb.TailStateTransferRequest.sent', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TAILSTATETRANSFERREQUEST_STATEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=698,
)


_CHAINRESPONSE = _descriptor.Descriptor(
  name='ChainResponse',
  full_name='adb.ChainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='adb.ChainResponse.rc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=727,
)


_INCREMENTREQUEST = _descriptor.Descriptor(
  name='IncrementRequest',
  full_name='adb.IncrementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.IncrementRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incrValue', full_name='adb.IncrementRequest.incrValue', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=779,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='adb.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.DeleteRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=781,
  serialized_end=809,
)


_TAILINCREMENTREQUEST = _descriptor.Descriptor(
  name='TailIncrementRequest',
  full_name='adb.TailIncrementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.TailIncrementRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incrValue', full_name='adb.TailIncrementRequest.incrValue', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='adb.TailIncrementRequest.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='adb.TailIncrementRequest.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cxid', full_name='adb.TailIncrementRequest.cxid', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=811,
  serialized_end=907,
)


_TAILDELETEREQUEST = _descriptor.Descriptor(
  name='TailDeleteRequest',
  full_name='adb.TailDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.TailDeleteRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='adb.TailDeleteRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='adb.TailDeleteRequest.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cxid', full_name='adb.TailDeleteRequest.cxid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=909,
  serialized_end=983,
)


_HEADRESPONSE = _descriptor.Descriptor(
  name='HeadResponse',
  full_name='adb.HeadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='adb.HeadResponse.rc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1011,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='adb.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adb.GetRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1038,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='adb.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rc', full_name='adb.GetResponse.rc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='adb.GetResponse.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1080,
)


_XIDPROCESSEDREQUEST = _descriptor.Descriptor(
  name='XidProcessedRequest',
  full_name='adb.XidProcessedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xid', full_name='adb.XidProcessedRequest.xid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1082,
  serialized_end=1116,
)


_CXIDPROCESSEDREQUEST = _descriptor.Descriptor(
  name='CxidProcessedRequest',
  full_name='adb.CxidProcessedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cxid', full_name='adb.CxidProcessedRequest.cxid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1118,
  serialized_end=1154,
)

_HEADSTATETRANSFERREQUEST_STATEENTRY.containing_type = _HEADSTATETRANSFERREQUEST
_HEADSTATETRANSFERREQUEST.fields_by_name['state'].message_type = _HEADSTATETRANSFERREQUEST_STATEENTRY
_HEADSTATETRANSFERREQUEST.fields_by_name['sent'].message_type = _HEADSTATEUPDATEREQUEST
_TAILSTATETRANSFERREQUEST_STATEENTRY.containing_type = _TAILSTATETRANSFERREQUEST
_TAILSTATETRANSFERREQUEST.fields_by_name['state'].message_type = _TAILSTATETRANSFERREQUEST_STATEENTRY
_TAILSTATETRANSFERREQUEST.fields_by_name['sent'].message_type = _TAILSTATEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['HeadStateUpdateRequest'] = _HEADSTATEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['TailStateUpdateRequest'] = _TAILSTATEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['LatestXidRequest'] = _LATESTXIDREQUEST
DESCRIPTOR.message_types_by_name['LatestXidResponse'] = _LATESTXIDRESPONSE
DESCRIPTOR.message_types_by_name['HeadStateTransferRequest'] = _HEADSTATETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['TailStateTransferRequest'] = _TAILSTATETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['ChainResponse'] = _CHAINRESPONSE
DESCRIPTOR.message_types_by_name['IncrementRequest'] = _INCREMENTREQUEST
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['TailIncrementRequest'] = _TAILINCREMENTREQUEST
DESCRIPTOR.message_types_by_name['TailDeleteRequest'] = _TAILDELETEREQUEST
DESCRIPTOR.message_types_by_name['HeadResponse'] = _HEADRESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['XidProcessedRequest'] = _XIDPROCESSEDREQUEST
DESCRIPTOR.message_types_by_name['CxidProcessedRequest'] = _CXIDPROCESSEDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeadStateUpdateRequest = _reflection.GeneratedProtocolMessageType('HeadStateUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEADSTATEUPDATEREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.HeadStateUpdateRequest)
  })
_sym_db.RegisterMessage(HeadStateUpdateRequest)

TailStateUpdateRequest = _reflection.GeneratedProtocolMessageType('TailStateUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAILSTATEUPDATEREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.TailStateUpdateRequest)
  })
_sym_db.RegisterMessage(TailStateUpdateRequest)

LatestXidRequest = _reflection.GeneratedProtocolMessageType('LatestXidRequest', (_message.Message,), {
  'DESCRIPTOR' : _LATESTXIDREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.LatestXidRequest)
  })
_sym_db.RegisterMessage(LatestXidRequest)

LatestXidResponse = _reflection.GeneratedProtocolMessageType('LatestXidResponse', (_message.Message,), {
  'DESCRIPTOR' : _LATESTXIDRESPONSE,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.LatestXidResponse)
  })
_sym_db.RegisterMessage(LatestXidResponse)

HeadStateTransferRequest = _reflection.GeneratedProtocolMessageType('HeadStateTransferRequest', (_message.Message,), {

  'StateEntry' : _reflection.GeneratedProtocolMessageType('StateEntry', (_message.Message,), {
    'DESCRIPTOR' : _HEADSTATETRANSFERREQUEST_STATEENTRY,
    '__module__' : 'chain_pb2'
    # @@protoc_insertion_point(class_scope:adb.HeadStateTransferRequest.StateEntry)
    })
  ,
  'DESCRIPTOR' : _HEADSTATETRANSFERREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.HeadStateTransferRequest)
  })
_sym_db.RegisterMessage(HeadStateTransferRequest)
_sym_db.RegisterMessage(HeadStateTransferRequest.StateEntry)

TailStateTransferRequest = _reflection.GeneratedProtocolMessageType('TailStateTransferRequest', (_message.Message,), {

  'StateEntry' : _reflection.GeneratedProtocolMessageType('StateEntry', (_message.Message,), {
    'DESCRIPTOR' : _TAILSTATETRANSFERREQUEST_STATEENTRY,
    '__module__' : 'chain_pb2'
    # @@protoc_insertion_point(class_scope:adb.TailStateTransferRequest.StateEntry)
    })
  ,
  'DESCRIPTOR' : _TAILSTATETRANSFERREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.TailStateTransferRequest)
  })
_sym_db.RegisterMessage(TailStateTransferRequest)
_sym_db.RegisterMessage(TailStateTransferRequest.StateEntry)

ChainResponse = _reflection.GeneratedProtocolMessageType('ChainResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHAINRESPONSE,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.ChainResponse)
  })
_sym_db.RegisterMessage(ChainResponse)

IncrementRequest = _reflection.GeneratedProtocolMessageType('IncrementRequest', (_message.Message,), {
  'DESCRIPTOR' : _INCREMENTREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.IncrementRequest)
  })
_sym_db.RegisterMessage(IncrementRequest)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

TailIncrementRequest = _reflection.GeneratedProtocolMessageType('TailIncrementRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAILINCREMENTREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.TailIncrementRequest)
  })
_sym_db.RegisterMessage(TailIncrementRequest)

TailDeleteRequest = _reflection.GeneratedProtocolMessageType('TailDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAILDELETEREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.TailDeleteRequest)
  })
_sym_db.RegisterMessage(TailDeleteRequest)

HeadResponse = _reflection.GeneratedProtocolMessageType('HeadResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEADRESPONSE,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.HeadResponse)
  })
_sym_db.RegisterMessage(HeadResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

XidProcessedRequest = _reflection.GeneratedProtocolMessageType('XidProcessedRequest', (_message.Message,), {
  'DESCRIPTOR' : _XIDPROCESSEDREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.XidProcessedRequest)
  })
_sym_db.RegisterMessage(XidProcessedRequest)

CxidProcessedRequest = _reflection.GeneratedProtocolMessageType('CxidProcessedRequest', (_message.Message,), {
  'DESCRIPTOR' : _CXIDPROCESSEDREQUEST,
  '__module__' : 'chain_pb2'
  # @@protoc_insertion_point(class_scope:adb.CxidProcessedRequest)
  })
_sym_db.RegisterMessage(CxidProcessedRequest)


DESCRIPTOR._options = None
_HEADSTATETRANSFERREQUEST_STATEENTRY._options = None
_TAILSTATETRANSFERREQUEST_STATEENTRY._options = None

_HEADCHAINREPLICA = _descriptor.ServiceDescriptor(
  name='HeadChainReplica',
  full_name='adb.HeadChainReplica',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1157,
  serialized_end=1585,
  methods=[
  _descriptor.MethodDescriptor(
    name='proposeStateUpdate',
    full_name='adb.HeadChainReplica.proposeStateUpdate',
    index=0,
    containing_service=None,
    input_type=_HEADSTATEUPDATEREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getLatestXid',
    full_name='adb.HeadChainReplica.getLatestXid',
    index=1,
    containing_service=None,
    input_type=_LATESTXIDREQUEST,
    output_type=_LATESTXIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stateTransfer',
    full_name='adb.HeadChainReplica.stateTransfer',
    index=2,
    containing_service=None,
    input_type=_HEADSTATETRANSFERREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='increment',
    full_name='adb.HeadChainReplica.increment',
    index=3,
    containing_service=None,
    input_type=_INCREMENTREQUEST,
    output_type=_HEADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='adb.HeadChainReplica.delete',
    index=4,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_HEADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='adb.HeadChainReplica.get',
    index=5,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='xidProcessed',
    full_name='adb.HeadChainReplica.xidProcessed',
    index=6,
    containing_service=None,
    input_type=_XIDPROCESSEDREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEADCHAINREPLICA)

DESCRIPTOR.services_by_name['HeadChainReplica'] = _HEADCHAINREPLICA


_TAILCHAINREPLICA = _descriptor.ServiceDescriptor(
  name='TailChainReplica',
  full_name='adb.TailChainReplica',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1588,
  serialized_end=1962,
  methods=[
  _descriptor.MethodDescriptor(
    name='proposeStateUpdate',
    full_name='adb.TailChainReplica.proposeStateUpdate',
    index=0,
    containing_service=None,
    input_type=_TAILSTATEUPDATEREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getLatestXid',
    full_name='adb.TailChainReplica.getLatestXid',
    index=1,
    containing_service=None,
    input_type=_LATESTXIDREQUEST,
    output_type=_LATESTXIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stateTransfer',
    full_name='adb.TailChainReplica.stateTransfer',
    index=2,
    containing_service=None,
    input_type=_TAILSTATETRANSFERREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='increment',
    full_name='adb.TailChainReplica.increment',
    index=3,
    containing_service=None,
    input_type=_TAILINCREMENTREQUEST,
    output_type=_HEADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='adb.TailChainReplica.delete',
    index=4,
    containing_service=None,
    input_type=_TAILDELETEREQUEST,
    output_type=_HEADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='adb.TailChainReplica.get',
    index=5,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TAILCHAINREPLICA)

DESCRIPTOR.services_by_name['TailChainReplica'] = _TAILCHAINREPLICA


_TAILCLIENT = _descriptor.ServiceDescriptor(
  name='TailClient',
  full_name='adb.TailClient',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=1964,
  serialized_end=2040,
  methods=[
  _descriptor.MethodDescriptor(
    name='cxidProcessed',
    full_name='adb.TailClient.cxidProcessed',
    index=0,
    containing_service=None,
    input_type=_CXIDPROCESSEDREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TAILCLIENT)

DESCRIPTOR.services_by_name['TailClient'] = _TAILCLIENT

# @@protoc_insertion_point(module_scope)
