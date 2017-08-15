package main

import "fmt"

func main() {
	ages := map[string]int{ // Correct for 2017
		"daffy": 80,
		"bugs":  79,
		"taz":   63,
	}

	// START
	for name := range ages { // Keys
		fmt.Println(name)
	}

	for name, age := range ages { // Keys & values
		fmt.Printf("%s is %d years old\n", name, age)
	}
	// END
}
