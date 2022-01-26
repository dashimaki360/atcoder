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
  vector<int> a(n);
  rep(i,n) cin >> a[i];

  int tot=0;
  int max_tot=0;
  int max_i=0;
  for(int i=2; i <= *max_element(a.begin(), a.end()); ++i){
    tot = 0;
    rep(j,n){
      if(a[j] % i == 0) tot++;
    }
    max_tot = max(max_tot, tot);
    if(max_tot == tot) max_i = i;
  }
  cout << max_i << endl;
  return 0;
}