#include <iostream>

long divisor(long n)
{
    long div = 2;
    while (n > 1) {
        if (0 == (n % div)) {
            n /= div;
            div--;
        }
        div++;
    }
    return div;
}

int main()
{
    std::cout << divisor(600851475143) << std::endl;
    return 0;
}
