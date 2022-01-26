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
  vector<int> a, b;
  rep(i,n){
    int x,y;
    cin >> x >> y;
    a.push_back(x-y);
    b.push_back(x+y);
  }
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  cout << max(a.back()-a[0], b.back()-b[0]) << endl;
  return 0;
}