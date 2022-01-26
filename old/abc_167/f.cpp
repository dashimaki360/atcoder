#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

bool compare(pair<int, int> a, pair<int, int> b) {
    if(a.second == b.second){
        return a.first < b.first;
    }else{
        return a.second > b.second;
    }
}

int main() {
  int n;
  cin >> n;

  // cout l,r incpmplete () nums
  vector<P> ps;
  vector<P> ms;
  rep(i,n){
    string s;
    cin >> s;
    int mi=0, sum=0;
    for(auto x: s){
      if(x=='('){
        sum++;
      } else {
        sum--;
        mi = min(mi, sum);
      }
    }
    if(sum >= 0) ps.emplace_back(mi, sum);
    else ms.emplace_back(mi-sum, -sum);
  }

  // sort r smaller, l bigger;
   sort(ps.rbegin(), ps.rend());
   sort(ms.rbegin(), ms.rend());

  // check ps & rs
  bool NG = false;
  // ps
  ll psum = 0;
  for(auto x: ps){
    if((psum + x.first) < 0) {
      NG = true;
      break;
    }
    psum += x.second;
    // cout << x.first << " " << x.second << endl;
  }
  // ms
  ll msum = 0;
  for(auto x: ms){
    if((msum + x.first) < 0) {
      NG = true;
      break;
    }
    msum += x.second;
    // cout << x.first << " " << x.second << endl;
  }
  // cout << psum << " " << msum << " " << NG << endl;
  if(!NG && psum == msum){
    cout << "Yes" << endl;
    return 0;
  }
  cout << "No" << endl;
  return 0;
}