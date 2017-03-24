package main
import "fmt"

func main() {
    fmt.Printf("for loop")
    for i := 0; i < 10; i++ {
        fmt.Printf("%d\n",i)
    }
    fmt.Printf("goto loop \n")
    gotoloop()
    fmt.Printf("array loop \n")
    arr := [...]int{1,2,3,4,}
    for _, v := range(arr){
        fmt.Printf("%d\n", v)
    }

    switch 0 {
        case 0:
            fmt.Printf("case 0")
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