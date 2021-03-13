#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}
const int N = 1000005;

int main() {
  int n, m, q;
  cin >> n >> m >> q;
  vector<P> a;
  rep(i,n) {
    int w, v;
    cin >> w >> v;
    a.emplace_back(v, w);
  }
  vector<int> b(m);
  rep(i,m) cin >> b[i];
  vector<int> llist, rl;
  rep(i,q){
    int l, r;
    cin >> l >> r;
    l--; r--;
    llist.push_back(l);
    rl.push_back(r);
  }
  sort(a.begin(), a.end(), greater<P>());

  rep(k,q){
    int l = llist[k];
    int r = rl[k];
    vector<int> bb(m);
    vector<int> d(n);
    rep(i,m){
      if((l<=i) && (i<=r)) continue;
      bb[i] = b[i];
    }
    sort(bb.begin(), bb.end());
    ll ans = 0;
    for(int x: bb){
      if(x == 0) continue;
      rep(i,n){
        if(d[i]) continue;
        if(a[i].second <= x){
          d[i] = 1;
          ans += a[i].first;
          break;
        }
      }
    }
    cout << ans << endl;
    // cout << __LINE__ << endl;
  }
  
  return 0;
}