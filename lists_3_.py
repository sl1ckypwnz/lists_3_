m = int(input("Максимальная масса,которую может выдержать одна лодка - "))
n = int(input("Количество рыбаков - "))
a =[]
for _ in range(n):
    a.append(int(input("Вес рыболова - ")))
    
print("Минимальное количество лодок:", (2 * min(a) <= m) + len([x for x in a if x + min(a) > m]))


