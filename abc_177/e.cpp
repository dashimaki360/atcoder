#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int N = 1000005;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  vector<int> b(N);
  rep(i,n) {
    int x;
    cin >> x;
    a[i] = x;
    b[x] += 1;
  }
  bool is_parwise = true;
  for(int i=2; i<N; ++i){
    int sum = 0;
    for(int j=i; j<N; j+=i){
      sum += b[j];
    }
    if(sum > 1) {
      is_parwise = false;
      break;
    }
  }
  if(is_parwise){
    cout << "pairwise coprime" << endl;
    return 0;
  }

  int g = 0;
  rep(i,n) g = gcd(g,a[i]);
  if(g == 1) {
    cout << "setwise coprime" << endl;
    return 0;
  }else{
    cout << "not coprime" << endl;
    return 0;
  }
  return 0;
}