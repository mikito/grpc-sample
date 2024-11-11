Sample gRPC Server
========

...
brew install grpcurl
...


'''
grpcurl -plaintext -proto service.proto -d '{"name":"world"}' localhost:9501 example.Greeter/SayHello
...
