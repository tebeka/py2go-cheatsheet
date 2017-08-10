# Python -> Go Cheatsheet

A cheatsheet for Python programmers who are starting to write Go code.

## Declarations

### Python

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

### Go

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

### Python

```python
with open('song.txt') as fp:
    pass  # Process file
```

### Go

```go
file, err := os.Open("song.txt")
if err != nil {
    return err
}
defer file.Close()
// Process file
```

## Define Function

### Python

```python
def add(a, b):
    """Adds a to b"""
    return a + b
```

### Go

```go
// Add adds a to b
func Add(a, b int) int {
    return a + b
}
```

## Iterate

### Python

```python
for name in names:
    print(name)

for i, name in enumerate(names):
    print('{} at {}'.format(name, i))
```

### Go

```go
for _, name := range names {
       fmt.Println(name)
   }
   for i, name := range names {
       fmt.Printf("%s at %d\n", name, i)
   }
```

## Iterate over Lines

### Python

```python
for line in fp:  # fp is an open file
    print(line)
```

### Go

```go
scanner := bufio.NewScanner(rdr) // file is an io.Reader
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
return scanner.Err()
```


---
Miki Tebeka <miki@353solutions.com>
