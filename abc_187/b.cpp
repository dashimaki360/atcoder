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
  vector<float> x(n), y(n);
  rep(i,n) cin >> x[i] >> y[i];

  int ans = 0;
  rep(i,n) rep(j,i){
    if(i==j) continue;
    float a = (y[i]-y[j])/(x[i]-x[j]);
    if(-1<=a && a<=1){
      ans++;
    }
  }
  cout << ans << endl;
  return 0;
}