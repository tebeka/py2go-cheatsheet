package main

import "fmt"

func main() {
	// START
	ages := map[string]int{ // Correct for 2017
		"daffy": 80,
		"bugs":  79,
		"taz":   63,
	}
	ages["elmer"] = 80

	fmt.Println(ages["bugs"]) // 79

	_, ok := ages["daffy"]
	fmt.Println(ok) // true

	delete(ages, "taz")

	for name := range ages { // Keys
		fmt.Println(name)
	}

	for name, age := range ages { // Keys & values
		fmt.Printf("%s is %d years old\n", name, age)
	}
	// END
}
