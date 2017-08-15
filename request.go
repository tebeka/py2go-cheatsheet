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
	reply := make(map[string]interface{})
	if err := dec.Decode(&reply); err != nil {
		log.Fatalf("error: can't decode reply - %s", err)
	}
	fmt.Println(reply["origin"])
	// END
}
