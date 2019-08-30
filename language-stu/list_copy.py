ltest = [1, 2, 3]
l1 = ltest
l1[0] = 100
print(ltest)

l2 = ltest[:]
l2[0] = 1
print(ltest)
