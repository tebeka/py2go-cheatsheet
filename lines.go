package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

func processLines(rdr io.Reader) error {
	// START
	scanner := bufio.NewScanner(rdr) // file is an io.Reader
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	return scanner.Err()
	// END
}

func main() {
	file, err := os.Open("song.txt")
	if err != nil {
		log.Fatal(err)
	}
	if err = processLines(file); err != nil {
		log.Fatal(err)
	}
}
