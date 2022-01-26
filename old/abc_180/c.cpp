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

  vector<ll> ans;
  rep(i, (int)sqrt(n)+1){
    if(i==0) continue;
    if(n%i==0){
      ans.push_back(i);
      if(i != n/i){
        ans.push_back(n/i);
      }
    }
  }
  sort(ans.begin(), ans.end());
  for(auto x: ans) cout << x << endl;
  return 0;
}