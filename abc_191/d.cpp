#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

ll isq(ll x) {
    ll ok = 0, ng = x;
    while (ng - ok > 1) {
        ll mid = (ng + ok) >> 1;
        if (1LL * mid * mid <= x) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    return ok;
}

int main() {
  long double dx, dy, dr;
  cin >> dx >> dy >> dr;
  const ll N = 10000;
  ll x = round(dx*10000.);
  ll y = round(dy*10000.);
  ll r = round(dr*10000.);
  ll ans = 0;

  for(ll i=((x-r+N-1)/N)*N; i<=x+r; i += N){
    if(r*r-(i-x)*(i-x) < 0) continue;
    ll t = isq(r*r - (i-x)*(i-x));
    ll j = (-t + y + N-1)/N;
    ll jj = (t + y)/N;
    ans += jj - j + 1;
    //  cout << i << " "<<j << " " << jj<< " " << jj-j+1 << endl;;
    // cout << i << " " << jj-j+1 << endl;;

  }
  cout << ans << endl;

  return 0;
}