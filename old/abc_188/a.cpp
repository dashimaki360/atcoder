#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int x, y;
  cin >> x >> y;
  if(abs(x-y) < 3 ){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
  return 0;
}