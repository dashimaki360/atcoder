#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

// memo = [False]*n
vector<int> memo(1001001,0);
// x_list = [[X[i]] for i in range(n)]
vector<vector<int>> x_list(1001001);
// tree = [[] for _ in range(n)]
vector<vector<int>> tree(1001001);

// def set_x_list(n):
//     global x_list
//     memo[n] = True
//     for t in tree[n]:
//         if memo[t]:
//             continue
//         x_list[n].extend(set_x_list(t))
//     return x_list[n]
vector<int> set_x_list(int n){
  memo[n] = 1;
  rep(i,n){
    if (memo[tree[n][i]]) continue;
    x_list[n] += set_x_list(tree[n][i]);
  }
  
}

int main() {
  // n,q = LI()
  int n,q;
  cin >> n >> q;
  // X = LI()
  vector<int> X(n);
  rep(i,n) cin >> X[i];
  // AB = [LI() for _ in range(n-1)]
  vector<int> A(n-1), B(n-1);
  rep(i,n-1){
    int a,b;
    cin >> a >> b;
    A[i] == --a;
    B[i] == --b;
  }
  // VK = [LI() for _ in range(q)]
  vector<int> V(q), K(q);
  rep(i,q){
    int v,k;
    cin >> v >> k;
    V[i] == --v;
    K[i] == --k;
  }

  rep(i,n) x_list[i].push_back(X[i]);

  // for a, b in AB:
  //     tree[a-1].append(b-1)
  //     tree[b-1].append(a-1)
  rep(i,n-1){
    tree[A[i]].push_back(B[i]);
    tree[B[i]].push_back(A[i]);
  }


  // set_x_list(0)
  // for i in range(n):
  //     x_list[i].sort(reverse=True)
  // for v, k in VK:
  //     print(x_list[v-1][k-1])

  return 0;
}