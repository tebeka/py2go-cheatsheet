package main

import "fmt"

func main() {
	names := []string{"bugs", "taz", "tweety"}

	// START
	for _, name := range names {
		fmt.Println(name)
	}

	for i, name := range names {
		fmt.Printf("%s at %d\n", name, i)
	}
	// END
}
