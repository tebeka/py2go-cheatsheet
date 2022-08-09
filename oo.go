package main

import "fmt"

// START
type Cat struct {
	Name string
}

func NewCat(name string) *Cat {
	return &Cat{Name: name}
}

func (c *Cat) Greet(other string) {
	fmt.Printf("Meow %s, I'm %s\n", other, c.Name)
}

// END

func main() {
	// START
	c := NewCat("Grumpy")
	c.Greet("Grafield")
	// END
}
