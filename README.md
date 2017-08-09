# Python -> Go Cheatsheet

A cheatsheet for Python programmers who are starting to write Go code.


## Open File

### Python

```python
with open('/path/to/file') as fp:
    pass # Do something with open file
```
### Go

```go
import "os"

file, err := os.Open("/path/to/file")
if err != nil {
    return err
}
defer file.Close()
```


---
Miki Tebeka <miki@353solutions.com>
