import heapq

def min_cost(cable_lengths):
    # Перетворюємо список в купу
    heapq.heapify(cable_lengths)

    total_cost = 0
    
    while len(cable_lengths) > 1:
        # Беремо два найменші кабелі
        min1 = heapq.heappop(cable_lengths)
        min2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх і додаємо витрати до загальних
        cables_cost = min1 + min2
        total_cost += cables_cost
        
        # Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, cables_cost)
    
    return total_cost

# Приклад використання:
cable_lengths = [10, 24, 3, 12]
print("Мінімальна сума витрат на об'єднання кабелів:", min_cost(cable_lengths))
