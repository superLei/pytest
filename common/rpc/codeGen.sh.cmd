#安装grpc基础依赖
pip install grpcio
#安装 ProtoBuf 相关的 python 依赖库：
pip install protobuf
#安装grpc工具集
pip install grpcio-tools
#升成grpc端依赖
python -m grpc.tools.protoc -I=. --python_out=. --grpc_python_out=. shopsubjectcopyservice.proto
