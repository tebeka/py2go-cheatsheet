package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// START
	// Largest Fibonacci under 10,000
	a, b := 1, 1
	for b < 10000 {
		a, b = b, a+b
	}
	// END

	// START
	answer := ""
	var err error
	rdr := bufio.NewReader(os.Stdin)
	for {
		fmt.Printf("are you sure? [yes/no] ")
		answer, err = rdr.ReadString('\n')
		if err != nil {
			break
		}
		answer = strings.TrimSpace(answer)
		if answer != "yes" && answer != "no" {
			fmt.Println("error: Unknown answer")
			continue
		}
		break
	}
	// Do something with answer
	// END
	fmt.Println(a)
}
