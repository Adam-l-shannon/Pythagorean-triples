def triplet(nth):
    m = 2
    ans = {}
    for i in range(nth):
        for n in range(1,m):
            if len(ans) == nth:
                return ans
            if GCD(m,n) == 1 and (m%2!=0 ^ n%2!=0):
                a = (m**2)-(n**2)
                b = 2*m*n
                c = (m**2)+(n**2)
                ans[str(n)+","+str(m)] = [a,b,c]
        m+=1
    return ans
    
def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x 

# function triplet generates primitive pythagorean triples which have a,b,c all coprime to eachother
