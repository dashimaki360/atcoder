#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int m;
  cin >> m;
  int n = 1<<m;
  // vector<int> a(n/2), b(n/2);
  int max_a=0, max_b=0, max_a_id=0, max_b_id=0;
  rep(i,n/2) {
    int a;
    cin >> a;
    if(max_a < a){
      max_a = a;
      max_a_id = i+1;
    }
  }
  rep(i,n/2) {
    int b;
    cin >> b;
    if(max_b < b){
      max_b = b;
      max_b_id = n/2 + i+1;
    }
  }
  if(max_a > max_b){
    cout << max_b_id << endl;
    // cout << "max_B" << endl;
    return 0;
  }else{
    cout << max_a_id << endl;
    // cout << "max_A" << " " << max_a << " " << max_b << endl;
    return 0;
  }
  return 0;
}