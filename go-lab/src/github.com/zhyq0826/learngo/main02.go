package main

import "fmt"
import "unicode/utf8"

func main() {
    s := "asSASA ddd dskldskl dk"
    d := make(map[rune]int)
    for _, v := range(s){
        _, ok := d[v]
        if ok {
            d[v] += 1 
        } else {
            d[v] = 1
        }
    }

    for k, v := range(d){
        fmt.Printf("%s-%d\n", string(k), v)
    }

    b := []byte(s)

    fmt.Printf("%d, runes", utf8.RuneCount(b))
}