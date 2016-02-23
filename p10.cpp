#include <iostream>

bool is_prime(int n)
{
    if (n < 1) return false;
    if (n <= 3 ) return true;
    if ((n%2 == 0) || (n%3 == 0)) return false;
    int i = 5;
    while (i*i <= n) {
        if ((n%i == 0) || (n%(i+2) == 0)) return false;
        i += 6;
    }
    return true;
}

int main()
{
    int sum = 2;
    for (int i = 3; i < 2000000; i += 2) {
        if (is_prime(i)) sum += 1;
    }
    std::cout << sum << std::endl;
}
