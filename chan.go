package main

import "fmt"

func main() {
	// START
	ch := make(chan int)
	// END

	go func() {
		// START
		// Send message from a goroutine
		// (this will block is there no one reading)
		ch <- 353
		// END
	}()

	// START
	// Read message in a goroutine
	// (this will block is nothing in channel)
	val := <-ch
	// END

	fmt.Println(val)
}
