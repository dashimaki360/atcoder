#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n;
  cin >> n;
  vector<int> s(200005);
  ll ans = 0;
  rep(i, n){
    int a;
    cin >> a;
    if((i+a) < s.size()) s[i+a]++;
    if(s.size()>(i-a) && (i-a)>=0) ans += s[i-a];
  }
  cout << ans << endl;
  return 0;
}