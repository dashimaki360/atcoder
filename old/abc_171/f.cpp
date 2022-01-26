#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
using mint = modint1000000007;
const int mod = 1000000007;

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
  int k;
  cin >> k;
  string s;
  cin >> s;
  ll n = s.size();
  combination comb(n+k);
  mint ans = 0;
  rep(i,k+1){
    mint tmp = 1;
    tmp *= mint(25).pow(i);
    tmp *= mint(26).pow(k-i);
    tmp *= comb(n+i-1, n-1);
    ans += tmp;
  }
  cout << ans.val() << endl;


  return 0;
}