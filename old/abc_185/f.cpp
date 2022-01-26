#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int op(int x, int y){return x^y;}
int e() {return 0;}

int main() {
  int n, q;
  cin >> n >> q;
  segtree<int, op, e> t(n);
  rep(i,n) {
    int a;
    cin >> a;
    t.set(i,a);
  }
  rep(i,q){
    int type, x, y;
    cin >> type >> x >> y;
    --x;
    if(type == 1){
      t.set(x, t.get(x)^y);
    }
    else{
      cout << t.prod(x, y) << endl;
    }
  }

  return 0;
}