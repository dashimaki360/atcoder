#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n;
  cin >> n;
  n = n*2;
  ll ans = 0;
  ll l=sqrt(n);
  rep(i,l+1){
    if(i == 0) continue;
    if(n%i==0){
      if(i&1) ans++;
      if((n/i)&1) ans++;
    }
  }
  ans *= 2;
  cout << ans << endl;
  return 0;
}