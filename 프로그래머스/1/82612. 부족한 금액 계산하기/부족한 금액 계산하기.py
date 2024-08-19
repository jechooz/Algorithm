def solution(price, money, count):
    resultprice=0
    
    for i in range(1,count+1):
        resultprice+=price*i

    if money - resultprice> 0:
        print(resultprice)
        return 0
    else:
        return -(money-resultprice)