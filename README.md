Sample gRPC Server
========

```
brew install grpcurl
```

```
docker compose up
```

```
grpcurl -plaintext -proto service.proto -d '{"name":"world"}' localhost:9501 example.Greeter/SayHello
```
