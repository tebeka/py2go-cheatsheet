package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
)

// START

// We can also use anonymous struct
type Loon struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

// END

func jsons() error {
	// START
	var data = []byte(`{
		"name": "bugs",
		"age": 79
	}`)

	loon := Loon{}
	if err := json.Unmarshal(data, &loon); err != nil {
		return err
	}

	enc := json.NewEncoder(os.Stdout)
	if err := enc.Encode(loon); err != nil {
		return err
	}
	// END
	fmt.Printf("%#v\n", loon)
	return nil
}

func main() {
	if err := jsons(); err != nil {
		log.Fatal(err)
	}
}
