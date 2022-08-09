package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

func main() {
	// START
	url := "https://httpbin.org/ip"

	resp, err := http.Get(url)
	if err != nil {
		log.Fatalf("error: can't get %q - %s", url, err)
	}
	defer resp.Body.Close()

	dec := json.NewDecoder(resp.Body)
	var reply struct {
		Origin string `json:"origin"`
	}
	if err := dec.Decode(&reply); err != nil {
		log.Fatalf("error: can't decode reply - %s", err)
	}
	fmt.Println(reply.Origin)
	// END
}
