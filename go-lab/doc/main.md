## main 01

- 函数内数组的初始化和使用
- for 循环，goto 循环, array 循环


## main 02

- 双引号包裹的字符是字符串
- rune 是 int32 的别名，遍历字符串得到的是 rune 类型
- slice 是一个指向 array 的指针，如果 slice 的容量不够了，调用 append 容量不够的情况下回返回一个新的 slice，因此 append 会改变 slice 