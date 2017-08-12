package main

import "fmt"

func main() {
	// START
	// Largest Fibonacci under 10,000
	a, b := 1, 1
	for b < 10000 {
		a, b = b, a+b
	}
	fmt.Println(a)
	// END
}
