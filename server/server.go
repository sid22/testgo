package main

import (
	"context"
	"log"
	"net"

	pb "github.com/sid22/testgo/gen/proto"

	"google.golang.org/grpc"
)

type testApiServer struct {
	pb.UnimplementedTestApiServer
}

func (s *testApiServer) Echo(ctx context.Context, in *pb.ResponseRequest) (*pb.ResponseRequest, error) {
	log.Printf("Echo: %v", in.GetMsg())
	return in, nil
}

func main() {
	listen, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		log.Fatal(err)
	}
	log.Print("listening on port 8080")
	grpcServer := grpc.NewServer()
	pb.RegisterTestApiServer(grpcServer, &testApiServer{})

	err = grpcServer.Serve(listen)
	if err != nil {
		log.Fatal(err)
	}
}
