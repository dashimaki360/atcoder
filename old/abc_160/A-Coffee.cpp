#include <iostream>
#include <string>
using namespace std;

int main()
{
    string x;
    // 整数の入力
    cin>>x;

    if(x[2] == x[3] && x[4] == x[5]){
        printf("Yes\n");
        return 0;
    }else{
        printf("No\n");
        return 0;
    }
}