package main

import "fmt"

func main() {
	// START
	names := []string{"bugs", "taz", "tweety"}

	fmt.Println(names[0]) // bugs
	names = append(names, "elmer")

	fmt.Println(len(names)) // 4
	fmt.Println(names[2:])  // [tweety elmer]

	for _, name := range names {
		fmt.Println(name)
	}

	for i, name := range names {
		fmt.Printf("%s at %d\n", name, i)
	}
	// END
}
