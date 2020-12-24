#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  string s;
  cin >> s;

  if(s.size()==1){
    if(s=="8") cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
  }
  if(s.size()==2){
    if(s=="16"|| s=="61"||
       s=="24"|| s=="42"||
       s=="32"|| s=="23"|| 
       s=="48"|| s=="84"||
       s=="56"|| s=="65"||
       s=="64"|| s=="46"||
       s=="72"|| s=="27"||
       s=="88"|| s=="88"||
       s=="96"|| s=="69"
    ) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
  }
  // if(stoll(s)%1000 == 0){
  //   cout << "Yes" << endl;
  //   return 0;
  // }
  vector<int> eit = {112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992};
  for(auto x : eit){
    string xs = to_string(x);
    if(xs[0]=='0'||xs[1]=='0'||xs[2]=='0') continue;
    string ss = s;
    bool ok[3] = {};

// 0
    for (int i = 0; i < ss.size(); i++){
      if(ss[i] == xs[0]){
        ok[0] = true;
        ss.erase(i,1);
        break;
      }
    }
    if(ok[0]==false) continue;
// 1
    for (int i = 0; i < ss.size(); i++){
      if(ss[i] == xs[1]){
        ok[1] = true;
        ss.erase(i,1);
        break;
      }
    }
    if(ok[1]==false) continue;
// 2
    for (int i = 0; i < ss.size(); i++){
      if(ss[i] == xs[2]){
        ok[2] = true;
        ss.erase(i,1);
        break;
      }
    }
    if(ok[2]==false) continue;
// answer
    cout << "Yes" << endl;
    return 0;
  }

  cout << "No" << endl;
  return 0;
}
