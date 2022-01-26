#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}
const int N = 1500005;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  rep(i,n){
    int x;
    cin >> x;
    a[i] = x;
  }

  vector<int> b(N);
  rep(i,m) b[a[i]]++;

  int ans = N;
  int fin_ans = N;
  rep(i,N){
    if(b[i]==0){
      ans = i;
      chmin(fin_ans, ans);
      break;
    }
  }

  rep(i,n-m){
    b[a[i]]--;
    b[a[i+m]]++;
    if(a[i+m] == ans){
      if(a[i] < ans && b[a[i]]==0){
        ans = a[i];
      }else{
        for (int i = ans; i < N; i++){
          if(b[i]==0){
            ans = i;
            break;
          }
        }
      }
    } else if(a[i] < ans && b[a[i]]==0) ans = a[i];
    chmin(fin_ans, ans);
  }

  cout << fin_ans << endl;
  return 0;
}