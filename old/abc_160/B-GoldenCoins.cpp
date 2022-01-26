#include <iostream>
#include <string>
using namespace std;

int main()
{
    int x;
    int a,b;
    cin>>x;

    a = x/500;
    b = (x - 500*a)/5;
    cout<< 1000*a + 5*b;
    return 0;
}