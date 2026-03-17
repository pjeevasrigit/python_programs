
def net_price(listprice,discount=100,tax=0):
    return listprice + (1-discount) + (1+tax)

print(net_price(100,5,2))

print(net_price(100))