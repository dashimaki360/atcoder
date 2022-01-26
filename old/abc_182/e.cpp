#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

const int N = 1505;
const int di[] = {-1,0,1,0};
const int dj[] = {0,-1,0,1};

bool wall[N][N];
bool light[N][N];
bool ok[N][N];

bool visited[N][N];
bool memo[N][N];

int h,w,n,m;

bool f(int v, int i, int j){
  if(i < 0 || j < 0 || i >= h || j>=w) return false;
  if(wall[i][j]) return false;
  if(light[i][j]) return true;
  if(visited[i][j]) return memo[i][j];
  visited[i][j] = true;
  return memo[i][j] = f(v, i+di[v], j+dj[v]);
}

int main() {
  cin >> h >> w >> n >> m;
  rep(i, n){
    int r, c;
    cin >> r >> c;
    --r; --c;
    light[r][c] = true;
  } 
  rep(i, m){
    int r, c;
    cin >> r >> c;
    --r; --c;
    wall[r][c] = true;
  } 
  
  rep(v, 4){
    rep(i,h) rep(j,w) visited[i][j] = false;
    rep(i,h) rep(j,w) if(f(v,i,j)) ok[i][j] = true;
  }

  int ans=0;
  rep(i,h) rep(j,w) if(ok[i][j]) ++ans;
  cout << ans << endl;
  return 0;
}