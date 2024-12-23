sweet = input()
numberSweets = int(input())
day = int(input())
price = 0

if sweet == "Cake":
    if day <= 15:
        price = 24.00 * numberSweets
    else:
        price = 28.70 * numberSweets
elif sweet == "Souffle":
    if day <= 15:
        price = 6.66 * numberSweets
    else:
        price = 9.80 * numberSweets
elif sweet == "Baklava":
    if day <= 15:
        price = 12.60 * numberSweets
    else:
        price = 16.98 * numberSweets

if day <= 22:
    if 100 <= price <= 200:
        price *= 0.85
    elif price > 200:
        price *= 0.75
if day <= 15:
    price *= 0.90

print(f'{price:.2f}')