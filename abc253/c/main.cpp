#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)

int main() {
  map<int, int> ma;  // 名前→成績
  int q;
  cin >> q;
  int a,x,c;
  rep(i,q){
    cin >> a;
    if(a == 1){
      cin >> x;
      ma[x] += 1;
    }
    else if(a == 2)
    {
      cin >> x;
      cin >> c;
      if (ma[x] > c){
        ma[x] -= c;
      } else{
        ma.erase(x);
      }
    }
    else
    {
    int minv = ma.begin()->first;
    int maxv = ma.rbegin()->first;
    cout << maxv - minv << endl;
    }
  }
}