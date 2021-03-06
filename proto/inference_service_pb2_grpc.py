# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import inference_service_pb2 as proto_dot_inference__service__pb2


class InferenceServiceStub(object):
  """TODO(tommadams): Investigate enabling arenas with:
  option cc_enable_arenas = true;

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/minigo.InferenceService/GetConfig',
        request_serializer=proto_dot_inference__service__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.GetConfigResponse.FromString,
        )
    self.GetFeatures = channel.unary_unary(
        '/minigo.InferenceService/GetFeatures',
        request_serializer=proto_dot_inference__service__pb2.GetFeaturesRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.GetFeaturesResponse.FromString,
        )
    self.PutOutputs = channel.unary_unary(
        '/minigo.InferenceService/PutOutputs',
        request_serializer=proto_dot_inference__service__pb2.PutOutputsRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.PutOutputsResponse.FromString,
        )


class InferenceServiceServicer(object):
  """TODO(tommadams): Investigate enabling arenas with:
  option cc_enable_arenas = true;

  """

  def GetConfig(self, request, context):
    """Called by the inference worker to get the server's configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeatures(self, request, context):
    """Called by the inference worker to fetch the next batch of features to
    run. The returned batch is of fixed size, GetConfigResponse.batch_size.
    If there aren't enough inference requests pending to fill a batch, the
    batch is padded with zeros.
    The response is tagged with a batch ID. The same batch ID should be set
    in the PutOutputResquest that sends the inference output back to the
    server,
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutOutputs(self, request, context):
    """Called by the inference worker to write back the inference outputs.
    The batch ID in the PutOutputRequest must match the ID from the previous
    call to GetFeaturesRequest.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=proto_dot_inference__service__pb2.GetConfigRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.GetConfigResponse.SerializeToString,
      ),
      'GetFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatures,
          request_deserializer=proto_dot_inference__service__pb2.GetFeaturesRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.GetFeaturesResponse.SerializeToString,
      ),
      'PutOutputs': grpc.unary_unary_rpc_method_handler(
          servicer.PutOutputs,
          request_deserializer=proto_dot_inference__service__pb2.PutOutputsRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.PutOutputsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'minigo.InferenceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
