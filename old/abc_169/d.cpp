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
  // 素因数分解
  vector<P> res;
  rep(i, 1000005){
    int ex = 0;
    if(i == 0) continue;
    if(i == 1) continue;
    while(n % i == 0){
      ++ex;
      n /= i;
    }
    res.push_back({i, ex});
  }
  if(n>1) res.push_back({n,1});

  ll ans=0;
  for(auto p : res){
    ll ex = p.second;
    ll i = 1;
    while(ex >= (i*(i+1))/2){
      ans++;
      i++;
    }
  }
  cout << ans << endl;
  return 0;
}