#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const ll N = 1000000007;
using mint = modint1000000007;

int main() {
  int n, k, kk;
  cin >> n >> k;
  kk = k;
  priority_queue<ll> a, z;
  priority_queue<ll, vector<ll>, greater<ll> > b;
  vector<ll> ab(n);
  rep(i,n){
    ll c;
    cin >> c;
    if(c > 0) a.push(c);
    if(c < 0) b.push(c);
    if(c == 0) z.push(c);
    ab[i] = abs(c);
  }
  mint sum = 1;
  bool ok = true;
  if(a.empty() && k%2==1) ok = false;
  if(n==k && b.size()%2==1) ok = false;
  // ans < 0
  if(!ok){
    sort(ab.begin(), ab.end());
    sum = 1;
    rep(i, kk){
      sum *= ab[i];
    }
    sum *= -1;
    cout << sum.val() << endl;
    return 0;
  }
  // ans >= 0
  while(k > 0){
    if(k%2 == 1){
      if(!a.empty()) {
        sum *= a.top();
        a.pop();
        k--;
      }else if(!z.empty()){
        sum *= z.top();
        z.pop();
        k--;
      }else {
        sum *= b.top();
        b.pop();
        k--;
      }
    }else{
      if(a.size()>=2 && b.size()>=2){
        ll tmpa, tmpb;
        tmpa = a.top();
        a.pop();
        tmpb = b.top();
        b.pop();

        if(tmpa*a.top() > tmpb*b.top()){
          sum *= tmpa;
          k--;
          sum *= a.top();
          a.pop(); k--;
          b.push(tmpb);
        }else{
          sum *= tmpb;
          k--;
          sum *= b.top();
          b.pop(); k--;
          a.push(tmpa);
        }
      }else if(a.size()>=2){
        sum *= a.top();
        a.pop(); k--;
        sum *= a.top();
        a.pop(); k--;
      }else if(b.size()>=2){
        sum *= b.top();
        b.pop(); k--;
        sum *= b.top();
        b.pop(); k--;
      }else if(z.empty()){
        sum *= a.top();
        a.pop(); k--;
        sum *= b.top();
        b.pop(); k--;
      }else{
        sum *= z.top();
        z.pop(); k--;
        break;
      }
    }
  }
  cout << sum.val() << endl;
  return 0;
}