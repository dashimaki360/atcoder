#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
using mint = modint1000000007;
const int mod = 1000000007;

int main() {
  int n;
  cin >> n;
  int zero = 0;
  map<pair<ll,ll>, pair<int, int>> mp;
  
  // devided group
  rep(i,n){
    ll x, y;
    cin >> x >> y;
    if(x==0 && y==0){
      zero++;
      continue;
    }
    ll g = gcd(x, y);
    x /= g;
    y /= g;
    if(y < 0) x = -x, y = -y;
    if(y == 0 && x <0) x = -x, y = -y;
    bool rot90 = (x <= 0); 
    if (rot90) {
      swap(x, y);
      y = -y;
      // ll tmp = x;
      // x = y; y = -tmp;
    }
    if(rot90) mp[{x,y}].first++;
    else mp[{x,y}].second++;
  }
    
  // cout up
  mint ans = 1;
  for(auto p : mp) {
    auto[s, t] = p.second;
    // int s = p.second.first;
    // int t = p.second.second;
    mint now = 1;
    now += mint(2).pow(s) - 1;
    now += mint(2).pow(t) - 1;
    ans *= now;
  }
  ans -= 1;
  ans += zero;
  cout << ans.val() << endl;
  return 0;
}