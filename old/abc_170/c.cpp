#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int x, n;
  cin >> x >> n;
  vector<int> p(102);
  if(n==0){
    cout << x << endl;
    return 0;
  }
  rep(i,n) {
    int a;
    cin >> a;
    p[a] = 1;
  }

  int ans = 0;
  int minx = 1000;
  for(int i=101; i>=0; i--) {
    if(p[i]) continue;
    if(minx >= abs(x-i)){
      minx = abs(x-i);
      ans = i;
    }
  }
  cout << ans << endl;
  return 0;
}