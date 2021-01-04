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
  vector<vector<ll>> t(n);
  vector<ll> p(n, 0);
  vector<ll> al(n-1), bl(n-1);
  rep(i,n-1){
    ll a, b;
    cin >> a >> b;
    --a; --b;
    al[i] = a;
    bl[i] = b;
    t[a].push_back(b);
    t[b].push_back(a);
  }
// calc depth
  vector<ll> depth(n, -1);
  // I deifne  i=0 node is root
  ll root = 0;
  depth[root] = 0;
  vector<ll> que = {root};
  while(que.size()){
    ll at = que.back();
    que.pop_back();
    for(ll i : t[at]) if(depth[i] == -1){
      depth[i] = depth[at] + 1;
      que.push_back(i);
    }
  }

  
  int q;
  cin >> q;
  rep(i,q){
    ll tt, e, x;
    cin >> tt >> e >> x;
    --e;
    ll ai = al[e];
    ll bi = bl[e];
    if(tt==2) swap(ai, bi);
    // a is child
    if(depth[ai] > depth[bi]){
      p[ai] += x;
      // cout << "child "<< i << " " << ai << " " << bi << " " << t[ai] << endl;
    // a is par 
    }else if(depth[bi] > depth[ai]){
      p[bi] -= x;
      p[root] += x;
      // cout <<"par  "<< i << " " <<  ai << " " << bi << " " << t[ai] << endl;
    }else{
      // error
      cout << "error " << i; 
      cout << " depth[ai]: " << depth[ai];
      cout << " depth[bi]: " << depth[bi] << endl;
    }
  }

  que = {root};
  while(que.size()){
    ll at = que.back();
    que.pop_back();
    for(ll i : t[at]) if(depth[at] < depth[i]){
      p[i] += p[at];
      que.push_back(i);
    }
  }
  for(ll i : p) cout << i << endl;
  return 0;
}