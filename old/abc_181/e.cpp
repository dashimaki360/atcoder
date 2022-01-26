#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> h(n), w(m);
  rep(i,n) cin >> h[i];
  rep(i,m) cin >> w[i];

  sort(h.begin(), h.end());
  sort(w.begin(), w.end());

  vector<int> fsum(n/2+1, 0);
  vector<int> bsum(n/2+1, 0);
  for(int i = 0; i+1 < n; i+=2) fsum[i/2+1] = fsum[i/2] + h[i+1] - h[i];
  for(int i = n-2; i > 0; i-=2) bsum[i/2] = bsum[i/2+1] + h[i+1] - h[i];

  int ans = 1001001001;
  int minw;
  int xxx = 0;
  for(int i = 0; i < n; i+=2){
    minw = 1001001001;
    for (int j = xxx; j < m; ++j){
      xxx = j;
      minw = min(minw, abs(h[i]-w[j]));
      if(w[j] > h[i]) break;
    }
    ans = min(ans, fsum[i/2] + bsum[i/2] + minw);
  }
  // for (int ww : w) {
  //   int x = lower_bound(h.begin(), h.end(), ww) - h.begin();
  //   if (x & 1)
  //     x ^= 1;
  //   ans = min(ans, fsum[x / 2] + bsum[x / 2] + abs(h[x] - ww));
  // }
  cout << ans << endl;
  return 0;
}