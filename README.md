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

health check
```
grpcurl -v -plaintext -proto service.proto localhost:9501 example.Health/Check
```
