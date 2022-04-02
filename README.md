# Setup

1. Install go lang
2. Install make 
3. Install global go deps

```
go get -u google.golang.org/grpc/cmd/protoc-gen-go-grpc
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc

go get -u google.golang.org/grpc/cmd/protoc-gen-go
go install google.golang.org/grpc/cmd/protoc-gen-go
```

4. Generate proto deps run  `make create`

5. In a terminal window go to `server/` 
```
go run server.go
```
6. In another terminal window go to `client/`
```
go run client.go
```

You should client sending a RPC call to sever and printing out the result.

