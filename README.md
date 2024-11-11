Sample gRPC Server
========

```
brew install grpcurl
```

```
docker compose up
```

```
grpcurl -plaintext -d '{"name":"world"}' localhost:9501 example.Greeter/SayHello
```

health check
```
grpcurl -plaintext localhost:9501 example.Health/Check
```
