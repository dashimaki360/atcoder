#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int h, w;
  cin >> h >> w;

  int sum = 0;
  int min_a = 105;
  int a;
  rep(i, h*w){
    cin >> a;
    min_a = min(min_a, a);
    sum += a;
  }

  cout << sum - min_a*h*w << endl;

  return 0;
}