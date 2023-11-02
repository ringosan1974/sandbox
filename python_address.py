hoge = 64
foo = "a".encode("ascii")
a = [0, 1, 2, 3]
print(f"hoge: {hoge}, {id(hoge)}")
print(f"foo: {foo}, {id(foo)}")
print(f"a: {a}, {id(a)}")
for i in a:
    print(f"elem: {i}, {id(i)}")