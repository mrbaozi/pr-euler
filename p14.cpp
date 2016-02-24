#include <iostream>

/* long collatz(long n) */
/* { */
/*     return n&1 ? (3*n + 1) : n/2; */
/* } */

int main()
{
    long num, len = 0;

    for (long n = 1; n <= 1000000; n++)
    {
        long i = 1;
        long tmp = n;

        while (1 != tmp)
        {
            tmp = (tmp & 1) ? (3*tmp + 1) : (tmp/2);
            /* tmp = collatz(tmp); */
            ++i;
        }

        if (i > len)
        {
            len = i;
            num = n;
        }
    }

    std::cout << "number: " << num << std::endl;
    std::cout << "collatz len: " << len << std::endl;
}
