class LazySegmentTree():
    def __init__(self, init, unitX, unitA, f, g, h):
        self.f = f # (X, X) -> X
        self.g = g # (X, A, size) -> X
        self.h = h # (A, A) -> A
        self.unitX = unitX
        self.unitA = unitA
        self.f = f
        if type(init) == int:
            self.n = init
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
            self.size = [1] * (self.n * 2)
        else:
            self.n = len(init)
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            self.size = [0] * self.n + [1] * len(init) + [0] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
    
        for i in range(self.n - 1, 0, -1):
            self.size[i] = self.size[i*2] + self.size[i*2|1]
        
        self.A = [unitA] * (self.n * 2)
        
    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def calc(self, i):
        return self.g(self.X[i], self.A[i], self.size[i])
    
    def calc_above(self, i):
        i >>= 1
        while i:
            self.X[i] = self.f(self.calc(i*2), self.calc(i*2|1))
            i >>= 1
    
    def propagate(self, i):
        self.X[i] = self.g(self.X[i], self.A[i], self.size[i])
        self.A[i*2] = self.h(self.A[i*2], self.A[i])
        self.A[i*2|1] = self.h(self.A[i*2|1], self.A[i])
        self.A[i] = self.unitA
        
    def propagate_above(self, i):
        H = i.bit_length()
        for h in range(H, 0, -1):
            self.propagate(i >> h)
    
    def propagate_all(self):
        for i in range(1, self.n):
            self.propagate(i)
    
    def getrange(self, l, r):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        
        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.calc(l))
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.calc(r), ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
    def getvalue(self, i):
        i += self.n
        self.propagate_above(i)
        return self.calc(i)
    
    def operate_range(self, l, r, a):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        while l < r:
            if l & 1:
                self.A[l] = self.h(self.A[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.h(self.A[r], a)
            l >>= 1
            r >>= 1
        
        self.calc_above(l0)
        self.calc_above(r0)
    
    # Find r s.t. calc(l, ..., r-1) = True and calc(l, ..., r) = False
    def max_right(self, l, z):
        if l >= self.n: return self.n
        l += self.n
        s = self.unitX
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.calc(l))):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.calc(l))):
                        s = self.f(s, self.calc(l))
                        l += 1
                return l - self.n
            s = self.f(s, self.calc(l))
            l += 1
            if l & -l == l: break
        return self.n
    
    # Find l s.t. calc(l, ..., r-1) = True and calc(l-1, ..., r-1) = False
    def min_left(self, r, z):
        if r <= 0: return 0
        r += self.n
        s = self.unitX
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.calc(r), s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.calc(r), s)):
                        s = self.f(self.calc(r), s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.calc(r), s)
            if r & -r == r: break
        return 0

# P = 998244353
# f = lambda x, y: (x + y) % P
# g = lambda x, a, s: (a[0] * x + a[1] * s) % P
# h = lambda a, b: (a[0] * b[0] % P, (a[1] * b[0] + b[1]) % P)
# unitX = 0
# unitA = (1, 0)
# N, Q = map(int, input().split())
# A = [int(a) for a in input().split()]
# st = LazySegmentTree(A, unitX, unitA, f, g, h)

# for _ in range(Q):
#     q = [int(a) for a in input().split()]
#     if q[0] == 0:
#         l, r, b, c = q[1:]
#         st.operate_range(l, r, (b, c))
#     else:
#         l, r = q[1:]
#         print(st.getrange(l, r))
