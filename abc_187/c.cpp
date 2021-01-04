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
  vector<string> s(n);
  rep(i,n) cin >> s[i];
  // remove same string
  sort(s.begin(), s.end());
  rep(i, n-1){
    if(s[i] == s[i+1]){
      s[i] = "";
    }
  }

  rep(i,n){
    if(s[i][0]=='!') s[i].erase(0,1);
  }
  sort(s.begin(), s.end());
  rep(i, n-1){
    if(s[i].empty()) continue;
    if(s[i] == s[i+1]){
      cout << s[i] << endl; 
      return 0;
    }
  }
  cout << "satisfiable" << endl; 
  // cout << "satisfiable" << endl; 
  return 0;
}