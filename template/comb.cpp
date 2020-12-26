ll comb[2000][2000];
void combInit(int s){
  rep(i,s) rep(j,s) {
    if(j==0) comb[i][j] = 1;
    else comb[i][j] = 0;
  }
  for(int i=1; i<s; i++){
    for(int j=1; j<=i; j++){
      comb[i][j] = (comb[i-1][j-1] + comb[i-1][j])%N;
    }
  }
}