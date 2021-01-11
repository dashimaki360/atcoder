#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
using mint = modint998244353; 
const int mod = 998244353; 

struct combination {
  vector<mint> fact, ifact;
  combination(int n):fact(n+1),ifact(n+1) {
    assert(n < mod);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i-1]*i;
    ifact[n] = fact[n].inv();
    for (int i = n; i >= 1; --i) ifact[i-1] = ifact[i]*i;
  }
  mint operator()(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n]*ifact[k]*ifact[n-k];
  }
};

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  combination comb(n);

  mint ans = 0;
  rep(i, k+1){
    mint tmp = m-1;
    tmp = tmp.pow(n-i-1);
    tmp *= m;
    tmp *= comb(n-1, i);
    ans += tmp;
    // cout << tmp.val() << endl;
  }
  cout << ans.val() << endl;
  return 0;
}