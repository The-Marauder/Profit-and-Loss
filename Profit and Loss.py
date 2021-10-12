saleprice = int(input("Enter the price of the sale."))
productprice = int(input("Enter the price of the product."))
if saleprice>productprice :
    profit = saleprice - productprice
    Ppercent = profit/productprice*100
    print(f'The profit from this purchase was {profit} and the % gained is {Ppercent}')
elif saleprice == productprice :
    print("There was no profit or loss from this purchase.")
elif saleprice<productprice :
    loss = productprice-saleprice
    Lpercent = loss/productprice*100
    print(f'The loss from this purchase was {loss} and the % lost is {Lpercent}')