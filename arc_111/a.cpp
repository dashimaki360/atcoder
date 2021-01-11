#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
#include <atcoder/all>
using namespace atcoder;
using mint = modint;

int main() {
  ll n, m;
  cin >> n >> m;
  mint::set_mod(m*m);
  mint p = 10;
  p = p.pow(n);
  cout << (p.val()/m)%m << endl;
}