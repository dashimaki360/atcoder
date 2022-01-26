#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> a(n);
  rep(i,n) cin >> a[i];


  // 一番近い自分より右側の同じ数字のインデックスをペアにして記録する
  vector<int> pi(n+1, -1); // 一番近い数字を一時的に記憶しておく
  vector<vector<int>> ps(n); // ペアを記録するベクター
  rep(i,n) {
    int l = pi[a[i]];
    if(l != -1) ps[l].push_back(i);
    pi[a[i]] = i;
  }

  // クエリ先読み
  vector<vector<P>> qs(n);
  rep(qi, q){
    int l, r;
    cin >> l >> r;
    --l; --r;
    qs[l].emplace_back(r, qi);
  }

  // 重複した数字の数を数えるためにlが大きい順に捜査していく
  // 愚直にクエリを順番に処理していくと間に合わない。lを大きい方から捜査していく。
  vector<int> ans(q);
  fenwick_tree<int> d(n); // logN で数えるためにBIT(fenwick_tree)を使う. ACL
  for (int x = n-1; x>=0; --x) {
    for(int y: ps[x]) d.add(y,1); //該当する区間をBITに追加
    // クエリのr以下にある区間を数える(BITを使って高速に)
    for(P query : qs[x]) { 
      int r = query.first, i = query.second;
      ans[i] = (r-x+1) - d.sum(0, r+1); // 答えをクエリ順に格納 r以下の区間の合計をBITのSUMで計算
    }
  }
  // 答えを出力
  rep(i,q) cout << ans[i] << endl;
  return 0;
}