# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xk = yk = zk = [0,1]
for x in xk:
    for y in yk:
        for z in zk:
            if not(x or y or z) != (not(x) and not(y) and not(z)):
                print("False")
                break
            elif x == y == z == 1: print("True")