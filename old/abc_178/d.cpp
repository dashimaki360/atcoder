#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const ll N = 1000000007;

ll combination(ll n, ll r) {
  if ( r * 2 > n ) r = n - r;
  unsigned long long dividend = 1;
  for ( ll i = 1; i <= r; ++i ) {
    dividend *= (n-i+1);
    dividend /= i;
  }
  return (ll)dividend%N;
}

ll comb[2000][2000];
void combInit(int s){
  rep(i,s) rep(j,s) {
    if(j==0) comb[i][j] = 1;
    else comb[i][j] = 0;
  }
  for(int i=1; i<s; i++){
    for(int j=1; j<=i; j++){
      comb[i][j] = (comb[i-1][j-1] + comb[i-1][j])%N;
    }
  }
}


int main() {
  ll s;
  ll tot = 0;
  cin >> s;
  combInit(s);
  for(int i=3; i <= s; i+=3){
    ll a = s-i;
    ll bar = i/3 - 1; 
    // cout << a << ", " << bar << ", " << comb[a+bar][bar] << endl;
    tot += comb[a+bar][bar]; // bar C (a+bar)
    tot %= N;
  }
  cout << tot << endl;
  return 0;
}