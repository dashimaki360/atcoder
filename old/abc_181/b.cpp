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
  ll a, b;
  ll sum=0;
  rep(i,n){
    cin >> a >> b;
    sum += ((a+b)*(b-a+1))/2;
  }
  cout << sum << endl;
  return 0;
}