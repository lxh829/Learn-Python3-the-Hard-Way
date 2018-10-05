def function_1(A):
    print("function_1")
def function_2(B):
    print(B(3))
    print("function_2")


@function_1
@function_2
def function_name(n):
    print("Hello World ,i am function_name")
    return n+5
