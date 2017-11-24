package main

import "fmt"

// START
type Cat struct {
	name string
}

func NewCat(name string) *Cat {
	return &Cat{name: name}
}

func (c *Cat) Greet(other string) {
	fmt.Printf("Meow %s, I'm %s\n", other, c.name)
}

// END

func main() {
	// START
	c := NewCat("Grumpy")
	c.Greet("Grafield")
	// END
}
