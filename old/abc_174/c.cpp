#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int k;
  cin >> k;
  int x = 0;
  int ans = -1;
  rep(i,k){
    x = (x*10 + 7)%k;
    if(x==0){
      ans = i+1;
      break;
    }
  }
  cout << ans << endl;
  return 0;
}