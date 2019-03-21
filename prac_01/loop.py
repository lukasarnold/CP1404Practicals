for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 101, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

number_stars = int(input("Enter a number for how many stars: "))
for i in range(number_stars):
    print("*", end=' ')
print()

for i in range(number_stars + 1):
    stars = i * "*"
    print(stars)
