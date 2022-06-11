
def comb(n, r, mod):
    # mod素数のときつかえる
    # 素数でないときは拡張ユークリッドの互除法で逆元もとめること
    if n < 0 or r < 0 or r > n: return 0
    nu = 1
    de = 1
    for i in range(r):
        nu = nu * (n-i) % mod
        de = de * (i+1) % mod
    return nu * pow(de,mod-2,mod) % mod

def nHk(n,k,mod):
    return comb(n+k-1, k, mod)