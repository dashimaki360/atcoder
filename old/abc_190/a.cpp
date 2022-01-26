#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  string ans;
  if(a==b){
    if(c==0) ans = "Aoki";
    else ans = "Takahashi";
  }
  if(a > b) ans = "Takahashi";
  if(a < b) ans = "Aoki";
  cout << ans << endl;
  return 0;
}