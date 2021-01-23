#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, m;
  cin >> n >> m;
  int c;
  if(n&1){
    c = (n+1)/2;
  }else{
    c = n/2;
  }
  rep(i,m){
    int a, b;
    if(i&1){
      a = c - (i+1)/2;
      b = c + (i+1)/2;
    }else{
      a = i/2+1;
      b = n-i/2;
    }
    cout << a << " " << b << endl;
  }
  return 0;
}