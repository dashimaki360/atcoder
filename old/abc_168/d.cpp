#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n, m;
  cin >> n >> m;
  vector<vector<ll>> t(n);
  rep(i,m){
    ll a, b;
    cin >> a >> b;
    --a; --b;
    t[a].push_back(b);
    t[b].push_back(a);
  }

// calc depth
  vector<ll> depth(n, -1);
  vector<ll> ans(n, -1);

  // I deifne  i=0 node is root
  ll root = 0;
  depth[root] = 0;
  queue<ll> que;
  que.push(root);
  while(que.size()){
    ll at = que.front();
    que.pop();
    for(ll i : t[at]){
      // if(depth[i] == -1 || depth[i] > depth[at]+1){
      if(depth[i] == -1){
        depth[i] = depth[at] + 1;
        ans[i] = at+1;
        que.push(i);
      }
    }
  }
    cout << "Yes" << endl;
  rep(i,n){
    if(i==0) continue;
    cout << ans[i] << endl;
  }
  return 0;
}