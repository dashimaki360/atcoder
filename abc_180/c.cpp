#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n;
  cin >> n;

  rep(i, (int)sqrt(n)+1){
    if(i==0) continue;
    if(n%i==0) cout << i << endl;
  }
    cout << n << endl;
  return 0;
}