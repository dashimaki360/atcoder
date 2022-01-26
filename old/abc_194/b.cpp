#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

int main() {
  int n;
  cin >> n;
  vector<P> a, b;
  rep(i,n){
    int x, y;
    cin >> x >> y;
    a.emplace_back(x, i);
    b.emplace_back(y, i);
  }
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  if(a[0].second != b[0].second){
    cout << max(a[0].first , b[0].first) << endl;
    return 0;
  }
  int ans = 1001001001;
  chmin(ans, max(a[1].first, b[0].first));
  chmin(ans, max(a[0].first , b[1].first));
  chmin(ans, (a[0].first + b[0].first));
  cout << ans << endl;
  return 0;
}