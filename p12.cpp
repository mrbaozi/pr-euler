#include <iostream>
#include <cmath>

int divisors(int n)
{
    int ndiv = 0;
    int root = (int) sqrt(n);
    
    for (int i = 1; i <= root; ++i) {
        if (0 == n%i) {
            ndiv += 2;
        }
    }

    if (root*root == n) {
        ndiv -= 1;
    }

    return ndiv;
}

int main()
{
    int number = 0;
    int i = 1;
    while (divisors(number) < 500) {
        number += i;
        i += 1;
    }

    std::cout << number << std::endl;
}
