#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll x, k, d;
  cin >> x >> k >> d;
  x = abs(x);

  if(k*d > x){
    ll s = k - x/d;
    k = x/d + s%2;
  } 
  cout << abs(x - k*d) << endl;

  // ll t = min(k, x/d);
  // k -= t;
  // x -= t*d;
  // if(k%2 == 0){
  //   cout << x << endl;
  // }else{
  //   cout << d-x << endl;
  // }
  return 0;
}