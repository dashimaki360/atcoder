#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  string S;
  cin >> S;
  if(S[0] == S[1] && S[1] == S[2]){
  cout << "Won" << endl;

  } else{
  cout << "Lost" << endl;
  }
  return 0;
}