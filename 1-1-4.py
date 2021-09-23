# task4
def max_weight(capasity, weight):
    d = [[True] + [False] * capasity]
    for i in range(len(weight)):
        d.append(d[-1][:])
        for best_weight in range(weight[i], capasity + 1):
            d[-1][best_weight] = d[-2][best_weight] or d[-2][best_weight - weight[i]]
        d = d[-1:]

    for best_weight in range(capasity, -1, -1):
        if d[-1][best_weight]:
            return best_weight


capasity = int(input("Enter a bag capasity: "))
weights = input("Enter weights: ")

weights = list(set(weights.split()))
for i in range(0, len(weights)):
    weights[i] = int(weights[i])

print(max_weight(capasity, weights))
