#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
using namespace std;

int main()
{
    int N,t,x,y;
    int t_=0, x_=0, y_=0;
    int t_d, x_d, y_d;
    int d_sum;
    // 整数の入力
    scanf("%d", &N);

    // スペース区切りの整数の入力
    for (int i = 0; i < N; i++)
    {
        scanf("%d %d %d",&t,&x,&y);

        t_d = t - t_;
        x_d = abs(x - x_);
        y_d = abs(y - y_);

        d_sum = x_d + y_d;

        if(t_d < d_sum || (t_d - d_sum) % 2 == 1) {
            printf("No\n");
            return 0;
        }

        t_ = t;
        x_ = x;
        y_ = y;
    }
    
    printf("Yes\n");
    return 0;
}