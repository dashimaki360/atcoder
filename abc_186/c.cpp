#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int m, p;

int check(int n){
  m = n;
  do {
    if(m%10==7) return 0;
    m /= 10;
  } while (m);

  p = n;
  do {
    if(p%8==7) return 0;
    p /= 8;
  } while (p);
  return 1;
}

int main() {
  int n;
  cin >> n;

  int sum =0;

  for (int i = 1; i <= n; i++)
  {
    sum +=check(i);
  }

  cout << sum << endl;
  return 0;
}