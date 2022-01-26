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
  sort(a.begin(), a.end(), greater<int>());
  ll sum = 0;
  ll cnt = 1;
  rep(i,n){
    if(i==0){
      sum += a[0];
      cnt++;
      if(cnt==n) break;
    }else{
      sum += a[i];
      cnt++;
      if(cnt==n) break;

      sum += a[i];
      cnt++;
      if(cnt==n) break;
    }
  }
  cout << sum << endl;


  
  return 0;
}