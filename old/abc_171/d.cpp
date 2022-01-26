#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int N = 100005;


int main() {
  int n;
  cin >> n;
  vector<int> A(N);
  rep(i,n){
    int a;
    cin >> a;
    A[a]++;
  }
  ll sum = 0;
  rep(i,N){
    sum += i * A[i];
  }

  int q;
  cin >> q;
  rep(i,q){
    int b, c;
    cin >> b >> c;
    sum += A[b] * (c-b);
    A[c] += A[b];
    A[b] = 0;
    cout << sum << endl;
  }
  return 0;
}