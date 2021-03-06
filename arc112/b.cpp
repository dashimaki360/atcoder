#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

int main() {
  ll n, cost;
  cin >> n >> cost;
  ll a, b, c, d;
  if(n>0){
    a = min(cost/2+1, n+1);
    b = (cost-1)/2+1;
    c = (cost-2)/2;
    d = min((cost-1)/2, n-1);
  }else if(n<0){
    a = cost/2+1;
    b = min((cost-1)/2+1, -n+1);
    c = (cost-1)/2;
    d = min((cost-2)/2, -n-1);
  } else{
    a = cost/2+1;
    b = 0;
    c = (cost-1)/2;
    d = 0;
  }
  ll ans = a + b + c + d;
  cout << ans << endl;
  return 0;
}