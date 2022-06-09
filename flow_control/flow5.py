"""
for i in range(5):
    if i == 2:
        break
    else:
        print(i)
print("------------------------------------------------")
for i in range(5):
    if i == 2:
        continue
    else:
        print(i)
print("------------------------------------")
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)

"""
cart = [1999,  399, 499, 650, 800, 450, 299, 199, 99]
for i in cart:
    if i < 500:
        pass
    else:
        print('Product price is Rs:', i, 'Free delivery applicable')
print("------------------------------------------------------")
cart = [1999,  399, 499, 650, 800, 450, 299, 199, 99]
for i in cart:
    if i < 500:
        continue
    else:
        print('Product price is Rs:', i, 'Free delivery applicable')
