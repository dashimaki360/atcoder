#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
static const double pi = 3.141592653589793;

int main() {
  double a, b, h, m;
  cin >> a >> b >> h >> m;
  double hth = pi*2*(h*60 + m)/(60*12);
  double mth = pi*2*m/60;
  double th = abs(hth - mth);
  double ans = a*a + b*b - cos(th)*2*a*b;
  // printf("%f %f %f \n", hth, mth, th);
  printf("%0.19f\n", sqrt(ans));
  return 0;
}