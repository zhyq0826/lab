function fun1( ... )
    print(...)
end

print(fun1('a','b','c'))

function fun2(a, b)
    return a+b
end

print(fun2(2,3))


function fun3()
    return 1, 2
end

a, b = fun3()

print(a, b)