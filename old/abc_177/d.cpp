#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

struct UnionFind {
  vector<int> par;
  UnionFind(int n=0): par(n,-1) {}
  int find(int x) {
    if(par[x] < 0) return x;
    return par[x] = find(par[x]);
  }
  bool unite(int x, int y){
    x = find(x); y = find(y);
    if(x==y) return false;
    if(par[x] > par[y]) swap(x,y);
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  bool same(int x, int y) {return find(x) == find(y);}
  int size(int x) {return -par[find(x)];}
};

int main() {
  int n, m;
  cin >> n >> m;
  UnionFind t(n);
  rep(i,m){
    int a, b;
    cin >> a >> b;
    t.unite(a, b);
  }
  vector<int> sum(n);
  rep(i,n){
    sum[t.find(i)] += 1;
  }
  int ans = 0;
  rep(i,n){
    ans = max(ans, sum[i]);
  }
  cout << ans << endl;
  // rep(i,n) cout << sum[i] << endl;

  return 0;
}