#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

const int N = 200005;

int main() {
  ll n, q;
  cin >> n >> q;
  vector<int> a(n), b(n);
  vector<multiset<int>> s(N);
  multiset<int> maxs;
  
  auto getMax = [&](int i) {
    if(s[i].size() == 0) return -1;
    return *s[i].rbegin();
  };
  auto addYouchien = [&](int i) {
    int x = getMax(i);
    if(x == -1) return;
    maxs.insert(x);
  };
  auto delYouchien = [&](int i) {
    int x = getMax(i);
    if(x == -1) return;
    maxs.erase(maxs.find(x));
  };
  auto addEnji = [&](int i, int x){
    delYouchien(i);
    s[i].insert(x);
    addYouchien(i);
  };
  auto delEnji = [&](int i, int x){
    delYouchien(i);
    s[i].erase(s[i].find(x));
    addYouchien(i);
  };

  rep(i,n){
    cin >> a[i] >> b[i];
    addEnji(b[i], a[i]);
  }
  rep(i,q){
    int c, d;
    cin >> c >> d;
    --c;
    delEnji(b[c], a[c]);
    b[c] = d;
    addEnji(b[c], a[c]);
    int ans = *maxs.begin();
    cout << ans << endl;
  }
  return 0;
}