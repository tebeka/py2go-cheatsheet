# Python -> Go Cheatsheet

A cheatsheet for Python programmers who are starting to write Go code.

## Declarations

```python
age = 80
name = 'daffy'
loons = ['bugs', 'daffy', 'taz']
ages = {  # Correct for 2017
    'daffy': 80,
    'bugs': 79,
    'taz': 63,
}
```

```go
age := 80
name := "daffy"
loons := []string{"bugs", "daffy", "taz"}
ages := map[string]int{ // Correct for 2017
	"daffy": 80,
	"bugs":  79,
	"taz":   63,
}
```


## Files

```python
with open('song.txt') as fp:
    pass  # Process file

```

```go
file, err := os.Open("song.txt")
if err != nil {
	return err
}
defer file.Close()
// Process file

```


---
Miki Tebeka <miki@353solutions.com>
