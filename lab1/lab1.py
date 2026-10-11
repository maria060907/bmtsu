import sys
import math

def get_coef(name, index):

    if len(sys.argv) > index + 1:
        try:
            return float(sys.argv[index + 1])
        except ValueError:
            print(f"Некорректное значение коэффициента {name} в командной строке. Введите его вручную.")

    while True:
        s = input(f"Введите коэффициент {name}: ").strip().replace(',', '.')
        try:
            return float(s)
        except ValueError:
            print(f"Ошибка: '{s}' не число. Повторите ввод.")


def get_roots(A, B, C):

    roots = []

    if A == 0:
        if B == 0:
            if C == 0:
                return "infinite"
            return []
        t = -C / B
        if t > 0:
            roots += ([math.sqrt(t), -math.sqrt(t)])
        elif t == 0:
            roots.append(0.0)
        return roots

    D = B * B - 4 * A * C

    if D < 0:
        return roots

    if D == 0:
        t = -B / (2 * A)
        if t > 0:
            roots += ([math.sqrt(t), -math.sqrt(t)])
        elif t == 0:
            roots.append(0.0)
        return roots

    sqrtD = math.sqrt(D)
    t1 = (-B + sqrtD) / (2 * A)
    t2 = (-B - sqrtD) / (2 * A)

    for t in (t1, t2):
        if t > 0:
            r = math.sqrt(t)
            roots += ([r, -r])
        elif t == 0:
            roots.append(0.0)

    return roots

def format_equation(A, B, C):

    parts = []

    if A != 0:
        if A == 1:
            parts.append("x⁴")
        elif A == -1:
            parts.append("−x⁴")
        else:
            parts.append(f"{A:g}x⁴")

    if B != 0:
        if B < 0:
            sign = "−"
        else:
            sign = "+"

        b = abs(B)
        if not parts:
            if b == 1:
                if B > 0:
                    parts.append("x²" )
                else:
                    parts.append("−x²")
            else:
                if B < 0:
                    parts.append(f"{'-'}{b:g}x²")
                else:
                    parts.append(f"{''}{b:g}x²")
        else:
            if b == 1:
                parts.append(f" {sign} x²")
            else:
                parts.append(f" {sign} {b:g}x²")

    if C != 0 or not parts:
        if C < 0:
            sign = "−"
        else:
            sign = "+"
        c = abs(C)
        if not parts:
            if C < 0:
                parts.append(f"{'-'}{c:g}")
            else:
                parts.append(f"{''}{c:g}")
        else:
            parts.append(f" {sign} {c:g}")

    return " ".join(parts) + " = 0"

def main():
    print("РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ")

    A = get_coef("A", 0)
    B = get_coef("B", 1)
    C = get_coef("C", 2)

    print(f"\nВведенное уравнение: {format_equation(A, B, C)}")

    result = get_roots(A, B, C)

    if result == "infinite":
        print("Уравнение имеет бесконечно много решений (x может быть любым).")
    elif not result:
        print("Действительных корней нет.")
    else:
        true_roots = sorted(set(round(r, 10) for r in result))
        print("Действительные корни есть:")
        for r in true_roots:
            print(f"  x = {r}")

if __name__ == "__main__":
    main()
