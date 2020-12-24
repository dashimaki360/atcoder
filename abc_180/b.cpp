#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  cout << fixed << setprecision(15);

  int n;
  cin >> n;
  vector<long> x(n);
  rep(i,n) cin >> x[i];

  long mdis=0;
  long udis=0;
  long cdis=0;
  rep(i,n) mdis += abs(x[i]);
  cout << mdis << endl;

  rep(i,n) udis += x[i]*x[i];
  // printf("%.15f\n", udis);
  cout << sqrt(udis) << endl;

  rep(i,n) cdis = max(cdis, abs(x[i]));
  cout << cdis << endl;

  return 0;
}