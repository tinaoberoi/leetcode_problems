"""
code to print longest common subsequence
"""
def helper(text1, m, text2, n, dp):
    if m == 0 or n==0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    if text1[m-1] == text2[n-1]:
        dp[m][n] = 1 + helper(text1, m-1, text2, n-1, dp)
        return dp[m][n]
    dp[m][n] = max(helper(text1, m-1, text2, n, dp), helper(text1, m, text2, n-1, dp))
    return dp[m][n]

def lcs(text1, text2):
    m = len(text1)
    n = len(text2)

    if ( m == 0 or n == 0):
        return 0
    dp = [[-1 for j in range(n+1)] for i in range (m+1)] 
    lcs_len = helper(text1, m, text2, n, dp)
    lcs_str = ""
    i, j = m, n

    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs_str+=text1[i-1]
            i = i-1
            j = j-1
        elif dp[i-1][j] > dp[i][j-1]:
            i = i-1
        else:
            j = j-1
    return lcs_str[::-1]

x = lcs("abcde", "ace")
print(x)
