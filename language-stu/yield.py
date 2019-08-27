def test_func():
    print('start_func')
    for i in range(10):
        msg = yield i
        print("print in func-->" + str(i) + "-->" + str(msg))


y_func = test_func()
print('print out func-->' + str(next(y_func)))
print('print out func-->' + str(next(y_func)))
print("---------------")
y_func.send('aaa')
y_func.send('bbb')

print(type(y_func))
