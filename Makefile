create:
	protoc --proto_path=proto proto/*.proto --go_out=gen/
	protoc --proto_path=proto proto/*.proto --go-grpc_out=gen/
	python -m grpc_tools.protoc -I .\proto\ --python_out=gen/py/ --grpc_python_out=gen/py .\proto\test.proto
	
# protoc --proto_path=proto proto/*.proto --python_out=gen/proto/
# protoc --proto_path=proto proto/*.proto --grpc_python_out=gen/proto/

clean:
	rm gen/proto/*.go
	rm gen/py/*.py
