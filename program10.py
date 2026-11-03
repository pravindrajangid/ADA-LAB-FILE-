def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Finds the length of the longest common subsequence between two strings.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """

    m, n = len(text1), len(text2)

    # Initialize a 2D DP array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # If characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def minDistance(word1: str, word2: str) -> int:
    """
    Calculates the minimum edit distance (insert, delete, or replace)
    required to convert word1 into word2.

    Args:
        word1 (str): The source string.
        word2 (str): The target string.

    Returns:
        int: The minimum number of edit operations.
    """

    m, n = len(word1), len(word2)

    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Populate the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Replace, delete, or insert
                dp[i][j] = min(
                    dp[i - 1][j - 1],  # Replace
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1]       # Insert
                ) + 1

    return dp[m][n]


# Example Usage
if __name__ == "__main__":

    # Longest Common Subsequence Example
    s1, s2 = "programming", "gaming"

    print(f"Longest Common Subsequence of '{s1}' and '{s2}': {longestCommonSubsequence(s1, s2)}")

    # Edit Distance Example
    w1, w2 = "intention", "execution"

    print(f"Minimum Edit Distance between '{w1}' and '{w2}': {minDistance(w1, w2)}")
