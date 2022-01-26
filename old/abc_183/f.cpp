#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

struct UnionFind {
  vector<int> par;
  vector<map<int, int>> mp;
  UnionFind(int n=0): par(n,-1), mp(n) {}
  int find(int x) {
    if(par[x] < 0) return x;
    return par[x] = find(par[x]);
  }
  bool unite(int x, int y){
    x = find(x); y = find(y);
    if(x==y) return false;
    if(par[x] > par[y]) swap(x,y);
    // x > y
    for(auto p : mp[y]) {
      mp[x][p.first] += p.second;
    }
    mp[y] = map<int,int>();
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  bool same(int x, int y) {return find(x) == find(y);}
  int size(int x) {return -par[find(x)];}
};

int main() {
  int n ,q;
  cin >> n >> q;
  UnionFind t(n);
  rep(i,n) {
    int c;
    cin >> c;
    t.mp[i][c] = 1;
  }

  rep(i,q){
    int type, a,b,x, y;
    cin >> type ;
    if(type==1){
      cin >> a >> b;
      --a; --b;
      t.unite(a,b);
    }else{
      cin >> x >> y;
      --x;
      x = t.find(x);
      int ans = t.mp[x][y];
      cout << ans << endl;
    }
  }
  return 0;
}