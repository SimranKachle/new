

def knapsack(value,weight,capacity):
    n = len(value)-1

    m = [[-1]*(capacity+1) for _ in range(n+1)]

    for w in range(capacity+1):
        m[0][w]=0

    for i in range(1,n+1):
        for w in range(capacity+1):
            if weight[i]>w:
                m[i][w]=m[i-1][w]
            else:
                m[i][w] = max(m[i-1][w-weight[i]]+value[i],m[i-1][w])
    return m[n][capacity]
n = int(input("Enter number of items: "))
value = input("Enter value for {} items ".format(n)).split()
value = [ int(v) for v in value]
value.insert(0,None)

weight = input("Enter weight for {} items ".format(n)).split()
weight = [ int(w) for w in weight]
weight.insert(0,None)

capacity = int(input("Enter the capacity: "))

max = knapsack(value,weight,capacity)
print(max)