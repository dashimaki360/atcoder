#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, x;
  cin >> n >> x;
  vector<int> v(n), p(n);
  int sum = 0;
  rep(i,n) cin >> v[i] >> p[i];
  rep(i,n){
    sum += v[i]*p[i];
    if(sum > x*100){
      cout << i+1 << endl;
      return 0;
    }
  } 
  cout << -1 << endl;
  return 0;
}