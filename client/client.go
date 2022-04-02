package main

import (
	"context"
	"log"

	commons "github.com/sid22/testgo/commons"
	pb "github.com/sid22/testgo/gen/proto"

	"google.golang.org/grpc"
)

func main() {
	commons.TestDummyHello()
	conn, err := grpc.Dial("localhost:8080", grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	client := pb.NewTestApiClient(conn)
	resp, err := client.Echo(ctx, &pb.ResponseRequest{Msg: "hello"})
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("resp: %v", resp)
}
