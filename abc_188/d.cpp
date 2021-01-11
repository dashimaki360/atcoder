#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n, C;
  cin >> n >> C;
  vector<pair<ll,ll>> sum;
  rep(i,n){
    int a, b, c;
    cin >> a >> b >> c;
    --a; --b;
    sum.emplace_back(a,c);
    sum.emplace_back(b+1,-c);
  }
  sort(sum.begin(), sum.end());

  ll ans = 0;
  ll now = 0;
  ll tot = 0;
  rep(i, 1000000005){
    while(sum[now].first == i){
      tot += sum[now].second;
      ++now;
    }
    if(tot > C){
      ans += C;
    }else{
      ans += tot;
    }
  }
  cout << ans << endl;
  return 0;
}