# encoding = 'utf-8'
import json
import sys

sys.path.append("..")
import grpc
from common.rpc.proto import shopsubjectcopyservice_pb2, shopsubjectcopyservice_pb2_grpc

# HOST = 'linkerd.service.consul'
HOST = 'dohko.shop.service.hualala.com'
PORT = '31503'

# HOST = '172.16.32.39'
# PORT = '8888'


def get_response():
    channel = grpc.insecure_channel(HOST + ':' + PORT)
    print channel
    stub = shopsubjectcopyservice_pb2_grpc.ShopSubjectCopyServiceStub(channel)
    print stub
    Header={"traceID": "2134324234"}
    response = stub.shopSubjectCopy(
    shopsubjectcopyservice_pb2.ShopSubjectCopyRequest(header=Header, sourceShopID=2, targetShopID=3, sourceGroupID=4,
                                                      targetGroupID=5))
    print type(response)
    print response.result.message.encode('utf-8')
    # print("received: " + response)

    # CardInfoServiceGrpc.CardInfoServiceFutureStub
    # cardInfoServiceGrpc =
    # (CardInfoServiceGrpc.CardInfoServiceFutureStub)
    # cardInfoClient.getFutureStub(CardInfoServiceGrpc.
    #
    # class );
    # response = cardInfoServiceGrpc.queryCardInfo(request.toGRpcBean()).get();


if __name__ == '__main__':
    get_response()
