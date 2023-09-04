# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/integration/integration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,chirpstack-api/integration/integration.proto\x12\x0bintegration\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd5\x02\n\nDeviceInfo\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x13\n\x0btenant_name\x18\x02 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x03 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x04 \x01(\t\x12\x19\n\x11\x64\x65vice_profile_id\x18\x05 \x01(\t\x12\x1b\n\x13\x64\x65vice_profile_name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x07 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x08 \x01(\t\x12\x31\n\x14\x64\x65vice_class_enabled\x18\n \x01(\x0e\x32\x13.common.DeviceClass\x12/\n\x04tags\x18\t \x03(\x0b\x32!.integration.DeviceInfo.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"s\n\x11UplinkRelayRxInfo\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\n\n\x02\x64r\x18\x03 \x01(\r\x12\x0b\n\x03snr\x18\x04 \x01(\x05\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x13\n\x0bwor_channel\x18\x06 \x01(\r\"\x90\x03\n\x0bUplinkEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x10\n\x08\x64\x65v_addr\x18\x04 \x01(\t\x12\x0b\n\x03\x61\x64r\x18\x05 \x01(\x08\x12\n\n\x02\x64r\x18\x06 \x01(\r\x12\r\n\x05\x66_cnt\x18\x07 \x01(\r\x12\x0e\n\x06\x66_port\x18\x08 \x01(\r\x12\x11\n\tconfirmed\x18\t \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\n \x01(\x0c\x12\'\n\x06object\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12!\n\x07rx_info\x18\x0c \x03(\x0b\x32\x10.gw.UplinkRxInfo\x12!\n\x07tx_info\x18\r \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12\x35\n\rrelay_rx_info\x18\x0e \x01(\x0b\x32\x1e.integration.UplinkRelayRxInfo\"\xc6\x01\n\tJoinEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x10\n\x08\x64\x65v_addr\x18\x04 \x01(\t\x12\x35\n\rrelay_rx_info\x18\x05 \x01(\x0b\x32\x1e.integration.UplinkRelayRxInfo\"\xbd\x01\n\x08\x41\x63kEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x15\n\rqueue_item_id\x18\x04 \x01(\t\x12\x14\n\x0c\x61\x63knowledged\x18\x05 \x01(\x08\x12\x12\n\nf_cnt_down\x18\x06 \x01(\r\"\xdd\x01\n\nTxAckEvent\x12\x13\n\x0b\x64ownlink_id\x18\x01 \x01(\r\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x15\n\rqueue_item_id\x18\x04 \x01(\t\x12\x12\n\nf_cnt_down\x18\x05 \x01(\r\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12#\n\x07tx_info\x18\x07 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\"\xa6\x02\n\x08LogEvent\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x02 \x01(\x0b\x32\x17.integration.DeviceInfo\x12$\n\x05level\x18\x03 \x01(\x0e\x32\x15.integration.LogLevel\x12\"\n\x04\x63ode\x18\x04 \x01(\x0e\x32\x14.integration.LogCode\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x33\n\x07\x63ontext\x18\x06 \x03(\x0b\x32\".integration.LogEvent.ContextEntry\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe8\x01\n\x0bStatusEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x0e\n\x06margin\x18\x05 \x01(\x05\x12\x1d\n\x15\x65xternal_power_source\x18\x06 \x01(\x08\x12!\n\x19\x62\x61ttery_level_unavailable\x18\x07 \x01(\x08\x12\x15\n\rbattery_level\x18\x08 \x01(\x02\"\xa5\x01\n\rLocationEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\"\n\x08location\x18\x04 \x01(\x0b\x32\x10.common.Location\"\xdb\x01\n\x10IntegrationEvent\x12\x18\n\x10\x64\x65\x64uplication_id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x0b\x64\x65vice_info\x18\x03 \x01(\x0b\x32\x17.integration.DeviceInfo\x12\x18\n\x10integration_name\x18\x04 \x01(\t\x12\x12\n\nevent_type\x18\x05 \x01(\t\x12\'\n\x06object\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x88\x01\n\x0f\x44ownlinkCommand\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x02 \x01(\t\x12\x11\n\tconfirmed\x18\x03 \x01(\x08\x12\x0e\n\x06\x66_port\x18\x04 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\'\n\x06object\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct*,\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02*\xda\x01\n\x07LogCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x19\n\x15\x44OWNLINK_PAYLOAD_SIZE\x10\x01\x12\x10\n\x0cUPLINK_CODEC\x10\x02\x12\x12\n\x0e\x44OWNLINK_CODEC\x10\x03\x12\x08\n\x04OTAA\x10\x04\x12\x16\n\x12UPLINK_F_CNT_RESET\x10\x05\x12\x0e\n\nUPLINK_MIC\x10\x06\x12\x1f\n\x1bUPLINK_F_CNT_RETRANSMISSION\x10\x07\x12\x14\n\x10\x44OWNLINK_GATEWAY\x10\x08\x12\x18\n\x14RELAY_NEW_END_DEVICE\x10\tB\x81\x01\n\x1dio.chirpstack.api.integrationB\x10IntegrationProtoP\x01Z3github.com/brocaar/chirpstack/api/go/v4/integration\xaa\x02\x16\x43hirpstack.Integrationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.integration.integration_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035io.chirpstack.api.integrationB\020IntegrationProtoP\001Z3github.com/brocaar/chirpstack/api/go/v4/integration\252\002\026Chirpstack.Integration'
  _DEVICEINFO_TAGSENTRY._options = None
  _DEVICEINFO_TAGSENTRY._serialized_options = b'8\001'
  _LOGEVENT_CONTEXTENTRY._options = None
  _LOGEVENT_CONTEXTENTRY._serialized_options = b'8\001'
  _globals['_LOGLEVEL']._serialized_start=2730
  _globals['_LOGLEVEL']._serialized_end=2774
  _globals['_LOGCODE']._serialized_start=2777
  _globals['_LOGCODE']._serialized_end=2995
  _globals['_DEVICEINFO']._serialized_start=189
  _globals['_DEVICEINFO']._serialized_end=530
  _globals['_DEVICEINFO_TAGSENTRY']._serialized_start=487
  _globals['_DEVICEINFO_TAGSENTRY']._serialized_end=530
  _globals['_UPLINKRELAYRXINFO']._serialized_start=532
  _globals['_UPLINKRELAYRXINFO']._serialized_end=647
  _globals['_UPLINKEVENT']._serialized_start=650
  _globals['_UPLINKEVENT']._serialized_end=1050
  _globals['_JOINEVENT']._serialized_start=1053
  _globals['_JOINEVENT']._serialized_end=1251
  _globals['_ACKEVENT']._serialized_start=1254
  _globals['_ACKEVENT']._serialized_end=1443
  _globals['_TXACKEVENT']._serialized_start=1446
  _globals['_TXACKEVENT']._serialized_end=1667
  _globals['_LOGEVENT']._serialized_start=1670
  _globals['_LOGEVENT']._serialized_end=1964
  _globals['_LOGEVENT_CONTEXTENTRY']._serialized_start=1918
  _globals['_LOGEVENT_CONTEXTENTRY']._serialized_end=1964
  _globals['_STATUSEVENT']._serialized_start=1967
  _globals['_STATUSEVENT']._serialized_end=2199
  _globals['_LOCATIONEVENT']._serialized_start=2202
  _globals['_LOCATIONEVENT']._serialized_end=2367
  _globals['_INTEGRATIONEVENT']._serialized_start=2370
  _globals['_INTEGRATIONEVENT']._serialized_end=2589
  _globals['_DOWNLINKCOMMAND']._serialized_start=2592
  _globals['_DOWNLINKCOMMAND']._serialized_end=2728
# @@protoc_insertion_point(module_scope)
