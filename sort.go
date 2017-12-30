package main

import (
	"fmt"
	"sort"
)

func main() {

	// START
	names := []string{"bugs", "taz", "daffy"}

	// Lexicographical order
	sort.Strings(names)

	// Reverse lexicographical order
	sort.Sort(sort.Reverse(sort.StringSlice(names)))

	// Sort by length
	sort.Slice(names, func(i, j int) bool {
		return len(names[i]) < len(names[j])
	})
	// END

	fmt.Println(names)
}
