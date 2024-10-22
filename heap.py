import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)

        cost = first_cable + second_cable
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")