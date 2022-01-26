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

  if( n%3==0 ){
    cout << 0 << endl;
    return 0;
  }

  vector<int> a;
  do {
    a.push_back(n%10);
    n /= 10;
  } while (n!=0);

  if(a.size() == 1){
    cout << -1 << endl;
    return 0;
  }

  for(auto x : a){
    if( (accumulate(a.begin(), a.end(),0) - x)%3==0 ){
      cout << 1 << endl;
      return 0;
    }
  }

  if(a.size() < 3){
    cout << -1 << endl;
    return 0;
  }

  cout << 2 << endl;
  return 0;
}