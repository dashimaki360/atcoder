#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
using mint = modint1000000007;

int main() {
  mint a = 123455667770;
  mint ans = a*a;
  cout << ans.val() << endl;
  return 0;
}