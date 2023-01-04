# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol_robot_catie_2022.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol_robot_catie_2022.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fprotocol_robot_catie_2022.proto\"A\n\x14MainBoardToBrushless\x12\x1a\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\t.Commands\x12\r\n\x05speed\x18\x02 \x01(\x02\"C\n\x14\x42rushlessToMainBoard\x12\x13\n\x0b\x65rror_count\x18\x01 \x01(\r\x12\x16\n\x0emeasured_speed\x18\x02 \x01(\x02\"\xd0\x01\n\rIAToMainBoard\x12\x10\n\x08robot_id\x18\x01 \x01(\r\x12\x14\n\x0cnormal_speed\x18\x02 \x01(\x02\x12\x18\n\x10tangential_speed\x18\x03 \x01(\x02\x12\x15\n\rangular_speed\x18\x04 \x01(\x02\x12\x13\n\x0bmotor_break\x18\x05 \x01(\x08\x12\x1b\n\nkicker_cmd\x18\x06 \x01(\x0e\x32\x07.Kicker\x12\x12\n\nkick_power\x18\x07 \x01(\x02\x12\x0e\n\x06\x63harge\x18\x08 \x01(\x08\x12\x10\n\x08\x64ribbler\x18\t \x01(\x08\"\x83\x01\n\rMainboardToIA\x12\x10\n\x08robot_id\x18\x01 \x01(\r\x12\x1d\n\x15measured_normal_speed\x18\x02 \x01(\x02\x12!\n\x19measured_tangential_speed\x18\x03 \x01(\x02\x12\x1e\n\x16measured_angular_speed\x18\x04 \x01(\x02*(\n\x08\x43ommands\x12\x08\n\x04STOP\x10\x00\x12\x07\n\x03RUN\x10\x01\x12\t\n\x05\x42REAK\x10\x02*+\n\x06Kicker\x12\x0b\n\x07NO_KICK\x10\x00\x12\t\n\x05KICK1\x10\x01\x12\t\n\x05KICK2\x10\x02\x62\x06proto3'
)

_COMMANDS = _descriptor.EnumDescriptor(
  name='Commands',
  full_name='Commands',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BREAK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=516,
  serialized_end=556,
)
_sym_db.RegisterEnumDescriptor(_COMMANDS)

Commands = enum_type_wrapper.EnumTypeWrapper(_COMMANDS)
_KICKER = _descriptor.EnumDescriptor(
  name='Kicker',
  full_name='Kicker',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_KICK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KICK1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KICK2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=558,
  serialized_end=601,
)
_sym_db.RegisterEnumDescriptor(_KICKER)

Kicker = enum_type_wrapper.EnumTypeWrapper(_KICKER)
STOP = 0
RUN = 1
BREAK = 2
NO_KICK = 0
KICK1 = 1
KICK2 = 2



_MAINBOARDTOBRUSHLESS = _descriptor.Descriptor(
  name='MainBoardToBrushless',
  full_name='MainBoardToBrushless',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='MainBoardToBrushless.command', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='MainBoardToBrushless.speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=100,
)


_BRUSHLESSTOMAINBOARD = _descriptor.Descriptor(
  name='BrushlessToMainBoard',
  full_name='BrushlessToMainBoard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_count', full_name='BrushlessToMainBoard.error_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measured_speed', full_name='BrushlessToMainBoard.measured_speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=102,
  serialized_end=169,
)


_IATOMAINBOARD = _descriptor.Descriptor(
  name='IAToMainBoard',
  full_name='IAToMainBoard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='IAToMainBoard.robot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='normal_speed', full_name='IAToMainBoard.normal_speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tangential_speed', full_name='IAToMainBoard.tangential_speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular_speed', full_name='IAToMainBoard.angular_speed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='motor_break', full_name='IAToMainBoard.motor_break', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kicker_cmd', full_name='IAToMainBoard.kicker_cmd', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kick_power', full_name='IAToMainBoard.kick_power', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='charge', full_name='IAToMainBoard.charge', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dribbler', full_name='IAToMainBoard.dribbler', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=172,
  serialized_end=380,
)


_MAINBOARDTOIA = _descriptor.Descriptor(
  name='MainboardToIA',
  full_name='MainboardToIA',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='MainboardToIA.robot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measured_normal_speed', full_name='MainboardToIA.measured_normal_speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measured_tangential_speed', full_name='MainboardToIA.measured_tangential_speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measured_angular_speed', full_name='MainboardToIA.measured_angular_speed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=383,
  serialized_end=514,
)

_MAINBOARDTOBRUSHLESS.fields_by_name['command'].enum_type = _COMMANDS
_IATOMAINBOARD.fields_by_name['kicker_cmd'].enum_type = _KICKER
DESCRIPTOR.message_types_by_name['MainBoardToBrushless'] = _MAINBOARDTOBRUSHLESS
DESCRIPTOR.message_types_by_name['BrushlessToMainBoard'] = _BRUSHLESSTOMAINBOARD
DESCRIPTOR.message_types_by_name['IAToMainBoard'] = _IATOMAINBOARD
DESCRIPTOR.message_types_by_name['MainboardToIA'] = _MAINBOARDTOIA
DESCRIPTOR.enum_types_by_name['Commands'] = _COMMANDS
DESCRIPTOR.enum_types_by_name['Kicker'] = _KICKER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MainBoardToBrushless = _reflection.GeneratedProtocolMessageType('MainBoardToBrushless', (_message.Message,), {
  'DESCRIPTOR' : _MAINBOARDTOBRUSHLESS,
  '__module__' : 'protocol_robot_catie_2022_pb2'
  # @@protoc_insertion_point(class_scope:MainBoardToBrushless)
  })
_sym_db.RegisterMessage(MainBoardToBrushless)

BrushlessToMainBoard = _reflection.GeneratedProtocolMessageType('BrushlessToMainBoard', (_message.Message,), {
  'DESCRIPTOR' : _BRUSHLESSTOMAINBOARD,
  '__module__' : 'protocol_robot_catie_2022_pb2'
  # @@protoc_insertion_point(class_scope:BrushlessToMainBoard)
  })
_sym_db.RegisterMessage(BrushlessToMainBoard)

IAToMainBoard = _reflection.GeneratedProtocolMessageType('IAToMainBoard', (_message.Message,), {
  'DESCRIPTOR' : _IATOMAINBOARD,
  '__module__' : 'protocol_robot_catie_2022_pb2'
  # @@protoc_insertion_point(class_scope:IAToMainBoard)
  })
_sym_db.RegisterMessage(IAToMainBoard)

MainboardToIA = _reflection.GeneratedProtocolMessageType('MainboardToIA', (_message.Message,), {
  'DESCRIPTOR' : _MAINBOARDTOIA,
  '__module__' : 'protocol_robot_catie_2022_pb2'
  # @@protoc_insertion_point(class_scope:MainboardToIA)
  })
_sym_db.RegisterMessage(MainboardToIA)


# @@protoc_insertion_point(module_scope)