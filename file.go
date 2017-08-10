package main

import (
	"log"
	"os"
)

func run() error {
	// START
	file, err := os.Open("song.txt")
	if err != nil {
		return err
	}
	defer file.Close()
	// Process file
	// END

	return nil
}

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}
