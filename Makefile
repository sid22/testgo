create:
	protoc --proto_path=proto proto/*.proto --go_out=gen/
	protoc --proto_path=proto proto/*.proto --go-grpc_out=gen/
	protoc --proto_path=proto proto/*.proto --python_out=gen/proto/

clean:
	rm gen/proto/*.go
	rm gen/proto/*.py