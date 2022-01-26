#include <bits/stdc++.h>
using namespace std;
//#include <atcoder/all>
//using namespace atcoder;
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
#define rep(i,n) for (ll i = 0; i < (n); ++i)
// using ll = long long;
using ll = cpp_int;
using P = pair<int,int>;


int main() {
  ll x, k, d;
  ll ii = (long long)(1e15);
  ll ji = (long long)(1e10);
  ll ki = (long long)(1e9);
    // cin >> x >> k >> d;
    x = ii; k = ji; d = ki;
    x = abs(x);
  cout << k*d << endl;
    if(k*d > x){
      ll s = k - x/d;
      k = x/d + s%2;
    } 
    ll ans1 = abs(x - k*d);

    x = ii; k = ji; d = ki;
    x = abs(x);
    ll t = min(k, x/d);
    k -= t;
    x -= t*d;
    ll ans2 = 0;
    if(k%2 == 0){
      ans2 = x;
    }else{
      ans2 = d-x;
    }
    if(ans1 != ans2){
      printf("%d %d %d\n", ii, ji, ki);
    }
  return 0;
}