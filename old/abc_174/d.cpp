#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int solv(){
  int n;
  cin >> n;
  string s;
  cin >> s;
  int ir = 0;
  int il = n-1;
  int ans = 0;

  while(1){
    if(s[ir] == 'W'){
      while(1){
        if(s[il] == 'R'){
          ans++;
          s[ir] = 'R'; s[il] = 'W';
          // cout << ir << ", " << il << endl;
          break;
        }
        il--;
        if(ir==il) return ans;
      }
    }
    ir++;
    if(ir==il) return ans;
  }

}

int main() {
  cout << solv() << endl;
  return 0;
}