#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int N = 1000005;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  vector<int> b(N);
  rep(i,n){
    int x;
    cin >> x;
    a[i] = x;
    b[x]++;
  }
  sort(a.begin(), a.end());
  int befor = -1;
  for(auto x: a){
    if(x == befor) continue;
    int y = x + x;
    while(y < N){
      b[y] = 0;
      y += x;
    }
    befor = x;
  }
  int ans = 0;
  rep(i,N){
    if(b[i]==1) ans++;
  }
  cout << ans << endl;
  return 0;
}