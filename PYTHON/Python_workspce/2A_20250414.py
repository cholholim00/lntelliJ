def test1():
    for i in range(10):
        try:
            print(10/i)
        except ZeroDivisionError:
            print("Not divisible by 0")
        
# test1()

def test2():
    for i in range(10):
        try:
            print(10/i)
        except ZeroDivisionError as e:
            print(e)

# test2()

def test3():
    while True:
        value = input("숫자[종료:quit]: ")
        if value.upper() == "quit":
            break
        for digit in value:
            if not digit in "0123456789":
                raise ValueError("숫자를 넣어야지!!!")
            print(f"정수값: {int(value)}")

# test3()
def test4():
    try:
        while True:
            value = input("숫자[종료:quit]: ")
            if value.upper() == "quit":
                break
            for digit in value:
                if not digit in "0123456789":
                    raise ValueError("숫자를 넣어야지!!!")
            print(f"정수값: {int(value)}")
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)

test4()

