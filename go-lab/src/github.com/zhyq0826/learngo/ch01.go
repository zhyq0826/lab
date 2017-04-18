package main

import "fmt"

func main() {
    const s = 10
    fmt.Printf("%d\n", s)

    array := []int{1, 2, 3, 4, 5, 6}
    for _, item := range array {
        fmt.Printf("%d", item)
    }

    sr := "abcedf"
    c := []rune(sr)
    for _, i := range c {
        fmt.Printf("%c", i)
    }
}
