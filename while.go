package main

import "fmt"

func main() {
	// START
	a, b := 1, 1
	for b < 10_000 {
		a, b = b, a+b
	}
	// END
	fmt.Println(a)
}
