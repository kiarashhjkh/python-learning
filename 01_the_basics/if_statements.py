final_price = int(input())

if final_price >= 5000:
    final_price = final_price - (0.2) * final_price
elif final_price >= 2000:
    final_price = final_price - (0.1) * final_price
else :
    final_price = final_price

print(final_price)