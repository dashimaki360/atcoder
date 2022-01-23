#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

int main() {
  int n, m;
  cin >> n >> m;
  vector x(n, vector<bool>(n)), y(n, vector<bool>(n));
  rep(i,m){
    int a, b;
    cin >> a >> b;
    a--; b--;
    x[a][b] = x[b][a] = true;
  }
  rep(i,m){
    int c, d;
    cin >> c >> d;
    c--; d--;
    y[c][d] = y[d][c] = true;
  }

  vector<int> p(n);
  iota(begin(p), end(p), 0);
  do {
    bool ok = true;
    rep(i, n){
      rep(j, n){
        if(x[i][j] != y[p[i]][p[j]]){
          ok = false;
        }
      }
    }
    if(ok == true){
      cout << "Yes" << endl;
      return 0;
    }
  } while(next_permutation(begin(p), end(p)));
  cout << "No" << endl;
}