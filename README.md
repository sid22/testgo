# Setup

1. Install go lang
2. Install make 
3. Clone project
4. Install global go deps
5. Create python virtualenv `python3 -m venv venv`
6. Install py deps `pip install -r requirements.txt`

```
go clean -modcache

go get -u google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

go get -u google.golang.org/protobuf/cmd/protoc-gen-go
go install google.golang.org/protobuf/cmd/protoc-gen-go

go get -u google.golang.org/grpc/cmd/protoc-gen-go-grpc
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc
```

7. Generate proto deps run  `make create`

---
**NOTE:**  In case you are getting "protoc-gen-go: program not found or is not executable" error. Add both GOPATH and GOROOT in PATH :
```
export PATH=$PATH:$HOME/go/bin, in order to add the GOPATH and
export PATH=$PATH:/usr/local/go/bin, in order to add GOROOT
```
---

8. In a terminal window go to `server/` 
```
go run server.go
```
9. In another terminal window go to `client/`
```
go run client.go
```
10. For Python client in terminal go to `pyclient/`
```
python client.py
```

You should client sending a RPC call to sever and printing out the result.

