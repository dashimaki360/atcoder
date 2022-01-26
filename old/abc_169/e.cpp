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
  vector<int> a(n), b(n);
  rep(i,n) cin >> a[i] >> b[i];
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  int mida, midb;
  if(n&1){
    midb = b[(n-1)/2];
    mida = a[(n-1)/2];
  }else{
    midb = b[n/2-1] + b[n/2];
    mida = a[n/2-1] + a[n/2];
  }
  int ans;
  ans = midb - mida + 1;
  cout << ans << endl;
  return 0;
}