package main

import (
	"fmt"
	"time"
)

func add(a, b int) {
	fmt.Println(a + b)
}

func main() {
	// START
	go add(1, 2)
	// END

	time.Sleep(time.Millisecond)
}
