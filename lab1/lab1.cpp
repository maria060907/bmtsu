#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <windows.h>

bool isNumber(const std::string& s) {
    if (s.empty()) {
        return false;
    }

    int dotCount = 0;
    int start = 0;

    if (s[0] == '-') {
        if (s.length() == 1) {
            return false;
        }
        start = 1;
    }

    for (size_t i = start; i < s.length(); ++i) {
        if (s[i] == '.' || s[i] == ',') {
            dotCount++;
            if (dotCount > 1) {
                return false;
            }
        }
        else if (!std::isdigit(s[i])) {
            return false;
        }
    }

    return true;
}

class BiquadraticSolver {
private:
    double A, B, C;

public:
    BiquadraticSolver(double a, double b, double c) : A(a), B(b), C(c) {}

    bool infiniteRoots() const {
        return (A == 0 && B == 0 && C == 0);
    }

    std::vector<double> solve() const {
        std::vector<double> roots;

        if (infiniteRoots()) {
            return roots;
        }

        if (A == 0) {
            if (B != 0) {
                double t = -C / B;
                addRoots(t, roots);
            }
            return roots;
        }

        double D = B * B - 4 * A * C;
        if (D < 0) {
            return roots;
        }

        if (D == 0) {
            double t = -B / (2 * A);
            addRoots(t, roots);
        } else {
            double sqrtD = std::sqrt(D);
            double t1 = (-B + sqrtD) / (2 * A);
            double t2 = (-B - sqrtD) / (2 * A);

            addRoots(t1, roots);
            addRoots(t2, roots);
        }

        std::sort(roots.begin(), roots.end());

        std::vector<double> uniqueRoots;
        for (double r : roots) {
            if (uniqueRoots.empty() || std::abs(r - uniqueRoots.back()) > 1e-9) {
                if (std::abs(r) < 1e-9){
                    r = 0.0;
                }
                uniqueRoots.push_back(r);
            }
        }
        return uniqueRoots;
    }

    void formatEquation() const {
        std::cout << "Введенное уравнение: ";
        bool first = true;

        if (A != 0) {
            if (A == 1) {
                std::cout << "x⁴";
            }
            else if (A == -1) {
                std::cout << "-x⁴";
            }
            else {
                std::cout << A << "x⁴";
            }
            first = false;
        }

        if (B != 0) {
            if (!first) {
                if (B > 0) {
                    std::cout << " + ";
                }
                else {
                    std::cout << " - ";
                }
                double b_abs = std::abs(B);
                if (b_abs == 1) {
                    std::cout << "x²";
                }
                else {
                    std::cout << b_abs << "x²";
                }
            } else {
                if (B == 1) {
                    std::cout << "x²";
                }
                else if (B == -1) {
                    std::cout << "-x²";
                }
                else {
                    std::cout << B << "x²";
                }
            }
            first = false;
        }

        if (C != 0 || first) {
            if (!first) {
                if (C > 0) {
                    std::cout << " + ";
                }
                else {
                    std::cout << " - ";
                }
                std::cout << std::abs(C);
            } else {
                std::cout << C;
            }
        }

        std::cout << " = 0\n";
    }

private:
    void addRoots(double t, std::vector<double>& roots) const {
        if (t > 0) {
            double r = std::sqrt(t);
            roots.push_back(r);
            roots.push_back(-r);
        } else if (t == 0) {
            roots.push_back(0.0);
        }
    }
};

static double getCoef(const std::string& name) {
        std::string input;
        while (true) {
            std::cout << "Введите коэффициент " << name << ": ";
            std::cin >> input;


            if (isNumber(input)) {
                std::replace(input.begin(), input.end(), ',', '.');
                return std::stod(input);
            }

            std::cout << "Ошибка: '" << input << "' не число. Повторите ввод.\n";
        }
    }

int main(int argc, char* argv[]) {

    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);


    std::cout << "РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ\n\n";

    double A = getCoef("A");
    double B = getCoef("B");
    double C = getCoef("C");

    BiquadraticSolver solver(A, B, C);

    std::cout << "\n";
    solver.formatEquation();

    if (solver.infiniteRoots()) {
        std::cout << "Уравнение имеет бесконечно много решений (x может быть любым).\n";
    } else {
        std::vector<double> roots = solver.solve();
        if (roots.empty()) {
            std::cout << "Действительных корней нет.\n";
        } else {
            std::cout << "Действительные корни есть:\n";
            for (double r : roots) {
                std::cout << "  x = " << r << "\n";
            }
        }
    }

    return 0;
}
