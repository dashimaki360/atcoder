#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n, x, m;
  cin >> n >> x >> m;
  vector<ll> f(m, -1);
  vector<ll> a;
  int len = 0;
  ll tot = 0;
  while(f[x] == -1){
    a.push_back(x);
    f[x] = len;
    len ++;
    tot += x;
    x = (x*x)%m;
  }
  int c = len - f[x];
  ll s = 0;
  for(int i=f[x]; i<len; i++) s+=a[i];
  ll ans = 0;
  if(n <= len){
    rep(i,n) ans += a[i];
  }else{
    ans += tot;
    n -= len;
    ans += s*(n/c);
    n %= c;
    rep(i, n) ans += a[f[x]+i];
  }
  cout << ans << endl;
  return 0;
}
