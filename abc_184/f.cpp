#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, t;
  cin >> n >> t;
  vector<ll> a1, a2;
  rep(i,n) {
    int x;
    cin >> x;
    a1.push_back(x);
    swap(a1, a2);
  }
  vector<ll> a1sum(1<<a1.size());
  vector<ll> a2sum(1<<a2.size());
  rep(i,a1sum.size()){
    rep(j, a1.size())if(i>>j&1) a1sum[i] += a1[j];
  }
  rep(i,a2sum.size()){
    rep(j, a2.size())if(i>>j&1) a2sum[i] += a2[j];
  }
  sort(a1sum.begin(), a1sum.end());
  sort(a2sum.begin(), a2sum.end());

  ll ans = 0;
  for(auto a1i: a1sum){ 
    if(a1i > t) continue;
    ll a2i = upper_bound(a2sum.begin(), a2sum.end(), t-a1i) - a2sum.begin();
    ans = max(ans, a1i + a2sum[a2i-1]);
  }
  cout << ans << endl;
  return 0;
}