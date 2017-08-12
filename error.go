package main

import "fmt"

// START
func div(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("b can't be 0")
	}
	return a / b, nil
}

// END

func main() {
	// START
	val, err := div(1, 0)
	if err != nil {
		fmt.Printf("error: %s\n", err)
	}
	// END
	fmt.Println(val) // Must use val somehow
}
