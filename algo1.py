#Oppgave 2a) 
def BMMatch(T, P):
    m = len(P)
    n = len(T)

    i = m-1
    j = m-1

    num_comparisons = 0

    while i <= n-1:
        num_comparisons += 1
        if P[j] == T[i]:
            if j == 0:
                return "Found the pattern starting at position " + str(i) + " after " + str(num_comparisons/m) + \
                       " comparisons per char in P"
            else:
                i -= 1
                j -= 1
        else:
            i = i+m - min(j, 1 + last(T[i], P))
            j = m-1
    return "There is no substring of T matching P"


def KMPFailureFunc(P):
    lmp = [0] * len(P)
    i = 1
    # m can also be viewed as index of first mismatch
    m = 0
    while i < len(P):
        # prefix = suffix till m-1
        if P[i] == P[m]:
            m += 1
            lmp[i] = m
            i += 1
        
        # When there is a mismatch, we will check the index of previous possible prefix
        elif P[i] != P[m] and m != 0:
            # do not increment i here 
            m = lmp[m - 1]
        else:
            # m = 0, we move to the next letter,
            # there was no any prefix found which
            # is equal to the suffix for index i
            lmp[i] = 0
            i += 1

    return lmp


def KMPMatch(T, P):
    lmp = KMPFailureFunc(P)
    i = 0
    j = 0
    n = len(T)
    m = len(P)

    while i < n:
        if P[j] == T[i]:
            if j == m-1:
                return i - m+1
            i += 1
            j += 1
        elif j > 0:
            j = lmp[j-1]

        else:
            i = i+1
    return "Found no pattern"


def last(c, P):
    index = -1
    for pos, char in enumerate(P):
        if c == char:
            index = pos
    return index


#Oppgave 9a) 
def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
   
#Oppgave 9b) 
def dynLcs(X, Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 

    return L[m][n] 


def main(): 
    text = "a pattern matching algorithm"
    pattern = "rithm"
    result = BMMatch(text, pattern)
    print(result)
    text = "a pattern matching algorithm" 
    print("Longest common substring")
    X = "babbabab" 
    Y = "bbabbaaab"
    print(f"LCS in {X} and {Y} is {lcs(X, Y, len(X), len(Y))}")
    print(f"LCS from dynamic for {X} and {Y} is {dynLcs(X, Y)}")
    print("We will now try to find out when the recursive version starts to get too slow")
    print("Trying recursive LCS with 15 char string")
    X="ababcbabababbab"
    Y="abdfabbabdbadba"
    print(f"LCS in {X} and {Y} is {lcs(X, Y, len(X), len(Y))}")
    X="ababcbabababbabuwyet"
    Y="abdfabbabdbadbalopmh"
    print("Trying dynamic LCS with 20 char string")
    print(f"LCS from dynamic for {X} and {Y} is {dynLcs(X, Y)}") 
    print("Trying recursive LCS with 20 char string")
    print(f"LCS in {X} and {Y} is {lcs(X, Y, len(X), len(Y))}")
    
    
    
if __name__ == '__main__':
    main()
    
    

