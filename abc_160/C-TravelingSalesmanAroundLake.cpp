#include <iostream>
#include <string>
using namespace std;

int main()
{
    int k, n;
    cin>>k;
    cin>>n;

    int l, i=0, a[n];
    while(cin>>l){
        a[i] = l;
        cout << a[i];
        i++;
    }
    return 0;
}