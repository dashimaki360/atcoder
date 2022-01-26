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
  string name = "";
  while(1){
    n--;
    name += ('a' + n%26);
    n /= 26;
    if(n==0) break;
  }
  reverse(name.begin(), name.end());
  cout << name << endl;
  return 0;
}