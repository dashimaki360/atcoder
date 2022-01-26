#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

const ll INF = 1e18;
const int MAX_V = 50;
const int MAX_S = 50*50+5;
struct Edge {
  int to, a, b;
  Edge(int to, int a, int b): to(to),a(a),b(b) {}
};

struct Data {
  int v, s;
  ll x;
  Data(int v, int s, ll x):v(v), s(s), x(x) {}
  bool operator<(const Data& a) const {
    return x > a.x;
  }
};

vector<Edge> g[MAX_V];
ll dp[MAX_V][MAX_S+5];

int main() {
  int n, m, s;
  cin >> n >> m >> s;
  rep(i,m){
    int u, v, a, b;
    cin >> u >> v >> a >> b;
    --u; --v;
    g[u].emplace_back(v, a, b);
    g[v].emplace_back(u, a, b);
  }
  vector<int> rate(n), time(n);
  rep(i,n) cin >> rate[i] >> time[i];

  rep(i,MAX_V) rep(j, MAX_S+5) dp[i][j] = INF;
  s = min(s, MAX_S);
  priority_queue<Data> q;
  auto push = [&](int v, int s, ll x) {
    if(s < 0) return;
    if(dp[v][s] <= x) return;
    dp[v][s] = x;
    q.emplace(v,s,x);
  };
  push(0,s,0);
  while(!q.empty()){
    Data hoge = q.top();
    q.pop();
    int v = hoge.v, s = hoge.s;
    ll x = hoge.x;
    if(dp[v][s] != x) continue;
    //change coin
    {
      int ns = min(s+rate[v], MAX_S);
      push(v, ns, x+time[v]);
    }
    // move
    for(Edge e: g[v]) {
      push(e.to, s-e.a, x+e.b);
    }
  }
  for (int i = 1; i < n; ++i){
    ll ans = INF;
    rep(j,MAX_S+5) {
      ans = min(ans, dp[i][j]);
    }
    cout << ans << endl;
  }
  return 0;
}