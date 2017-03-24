package main
import "fmt"

func main() {
    fmt.Printf("for loop")
    for i := 0; i < 10; i++ {
        fmt.Printf("%d\n",i)
    }
    fmt.Printf("goto loop")
    gotoloop()
    fmt.Printf("array loop")
    arr := [...]int{1,2,3,4}
    for i := 0; i < len(arr); i++ {
        fmt.Printf("%d\n", arr[i])
    }
}

func gotoloop() {
    i := 0
    Here:
        fmt.Printf("%d\n", i)
        i++
        if i < 10 {
            goto Here
        }
}