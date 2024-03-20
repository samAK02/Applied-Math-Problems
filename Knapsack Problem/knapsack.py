N = int(input("Please enter the number of items to take: "))
L = float(input("Please enter your space limit: "))

U=[]
P = []
R=[]

for i in range(int(N)):
    A = float(input("Please enter the utility of the item on a scale of 1 to 10: "))
    U.append(A)
    B = float(input("Please enter the weight of the item : "))
    P.append(B)

R = [u / p for u, p in zip(U, P)]

max_index = R.index(max(R))

limitReached = False
print("selected items: \n")

total_utility = 0
total_weight = 0

for i in range(int(N)):
    if total_weight + P[i] <= L:
        total_utility += U[i]
        total_weight += P[i]
        print('Item', i+1, ': Utility =', U[i], ', Weight =', P[i])
    else:
        limitReached = True
        break

print("Total Utility: ",total_utility)
print("Total Weight: ", total_weight)

if total_weight < L:
    print("There is still place left, but no other item can be taken.")
if limitReached :
    print("The maximum capacity has been reached.")
else:
    print("Space limit not reached, all items have been taken.")



