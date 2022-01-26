#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

const int N = 1000000007;
int main() {
  ll n;
  cin >> n;
  ll a=1;
  ll b=1;
  ll c=1;
  rep(i,n) a = (a*10)%N;
  rep(i,n) b = (b*9)%N;
  rep(i,n) c = (c*8)%N;
  ll ans = ((a-2*b+c)%N+N)%N;
  cout << ans << endl;
  return 0;
}