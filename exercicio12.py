qtd_anos = 0
pop_a = 80000
pop_b = 200000

while True:
    pop_a += pop_a * 0.03
    pop_b += pop_b * 0.015
    qtd_anos += 1
    if pop_a > pop_b:
        break

print(pop_a)
print(pop_b)
print(qtd_anos)