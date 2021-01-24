#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

struct A
{
  vector<vector<int>> a;
  vector<ll> b;
  A(const vector<vector<int>>& _a = {{1,0},{0,1}},
    const vector<ll>& _b = {0,0}): a(_a), b(_b) {} 
  A operator*(const A& x) const {
    A res({{0,0},{0,0}});
    rep(i,2)rep(j,2)rep(k,2){
      res.a[i][j] += x.a[i][k]*a[k][j];
    }
    res.b = A(x.a)*b;
    rep(i,2){
      res.b[i] += x.b[i];
    }
    return res;
  }
  vector<ll> operator*(const vector<ll>& x) const {
    vector<ll> res = b;
    rep(i,2)rep(j,2) res[i] += a[i][j]*x[j];
    return res;
  }
};


int main() {
  int n;
  cin >> n;
  vector<vector<ll>> p(n, vector<ll>(2));
  rep(i,n) cin >> p[i][0] >> p[i][1];
  int m;
  cin >> m;
  vector<A> d(1);
  rep(i,m){
    int op;
    cin >> op;
    A x;
    int r;
    switch (op)
    {
    case 1:
      x = A({{0,1},{-1,0}});
      break;
    case 2:
      x = A({{0,-1},{1,0}});
      break;
    case 3:
      cin >> r;
      x = A({{-1,0},{0,1}}, {2*r,0});
      break;
    case 4:
      cin >> r;
      x = A({{1,0},{0,-1}}, {0, 2*r});
      break;
    }
    d.emplace_back(d.back()*x);
  }

  int q;
  cin >> q;
  rep(i,q){
    int a, b;
    cin >> a >> b;
    --b;
    vector<ll> ans = d[a]*p[b];
    printf("%lld %lld\n", ans[0], ans[1]);
  }
  return 0;
}