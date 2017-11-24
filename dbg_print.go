package main

import (
	"fmt"
)

type Actor struct {
	Name string
	Age  int
}

func main() {
	// START
	daffy := Actor{
		Name: "Daffy",
		Age:  80,
	}
	fmt.Printf("%#v\n", daffy)
	// END
}
