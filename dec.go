package main

import "fmt"

func main() {

	// START
	age := 80
	name := "daffy"
	weight := 62.3
	loons := []string{"bugs", "daffy", "taz"}
	ages := map[string]int{ // Correct for 2017
		"daffy": 80,
		"bugs":  79,
		"taz":   63,
	}
	// END

	fmt.Println(age, name, weight, loons, ages)
}
