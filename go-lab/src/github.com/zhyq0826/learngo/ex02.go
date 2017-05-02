package main

import "fmt"

func main() {
	sl := make([]float64, 10)
	sl[1] = 10
	sl[2] = 12
	sl[5] = 19
	s2 := append(sl, 10)
	fmt.Printf("%f\n", ave(s2))
	var a1, a2 int
	b1, b2 := 0, 0
	a1, a2 = sortNumber(10, 7)
	b1, b2 = sortNumber(10, 7)
	print(a1, " ", a2)
	print(b1, " ", b2)
}

func ave(s []float64) float64 {
	var sum float64
	for i := 0; i < len(s); i++ {
		sum += s[i]
	}
	return sum
}

func sortNumber(a1 int, a2 int) (r, s int) {
	if a1-a2 >= 0 {
		return a1, a2
	} else {
		return a2, a1
	}
}
