#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)


struct UnionFind {
  vector<int> par;
  UnionFind(int n=0): par(n,-1) {}
  int find(int x) {
    if(par[x] < 0) return x;
    return par[x] = find(par[x]);
  }
  bool unite(int x, int y){
    x = find(x); y = find(y);
    if(x==y) return false;
    if(par[x] > par[y]) swap(x,y);
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  bool same(int x, int y) {return find(x) == find(y);}
  int size(int x) {return -par[find(x)];}
};