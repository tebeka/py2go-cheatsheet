package main

import (
	"fmt"
	"sort"
)

// START

// ByLen implements sort.Interface
type ByLen []string

func (a ByLen) Len() int           { return len(a) }
func (a ByLen) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByLen) Less(i, j int) bool { return len(a[i]) < len(a[j]) }

// END

func main() {

	// START
	names := []string{"taz", "bugs", "daffy"}

	// Lexicographical order
	sort.Strings(names)
	// Reverse lexicographical order
	sort.Sort(sort.Reverse(sort.StringSlice(names)))
	// Sort by length
	sort.Sort(ByLen(names))
	// END

	fmt.Println(names)
}
