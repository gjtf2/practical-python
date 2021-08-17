Height = 100
lossHeight = 3/5
ballHeight = Height

# print(ballHeight)
for i in range(1, 11, 1):
    ballHeight = ballHeight * lossHeight
    print(i, round(ballHeight, 4))

