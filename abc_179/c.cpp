#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;


int main() {
  vector<int> hoge(n);
  sort(hoge.begin(), hoge.end())

  int n;
  cin >> n;
  int ans = 0;
  rep(a, n){
    if(a==0) continue;
    ans += (n-1)/a;
  }
  cout << ans << endl;
  return 0;
}