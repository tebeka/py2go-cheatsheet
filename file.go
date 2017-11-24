package main

import (
	"bufio"
	"fmt"
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

	// Iterate over lines
	scanner := bufio.NewScanner(file) // file is an io.Reader
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	return scanner.Err()
	// END
}

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}
