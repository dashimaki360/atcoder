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
  int me=0, you=0;
  ll ans=0;
  rep(i,n){
    cin >> me;
    if(me < you){
      ans += you - me;
    }else{
      you = me;
    }
  }
  cout << ans << endl;
  return 0;
}