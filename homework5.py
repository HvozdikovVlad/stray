
def divider(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        print("You can't")
        return 0
    except TypeError:
        print("You can't")
        return 0
    except ValueError:
        print("You can't")
        return 0
data = {10: 2, 2: 5, "123": 4, 18: 0, 69: 15, 8 : 4}
result= []
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)