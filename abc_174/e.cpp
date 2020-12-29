#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i,n) cin >> a[i];

  int ir = 0;
  int il = 1e9;
  while((il-ir) > 1){
    int x = (il+ir)/2;
    int tot = 0;
    rep(i,n){
      tot += (a[i]-1)/x;
    }
    // cout << tot << ", " << il << ", " << ir << endl;
    if(tot > k){
      ir = x;
    }else{
      il = x;
    }
  }
  cout << il << endl;
  return 0;
}