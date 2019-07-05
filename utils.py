

"""
Given two list of words X, Y. Return the longest common child

Solution: DP
If last characters of both sequences match (or X[m-1] == Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )

Reference: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
"""

def longest_common_child(X, Y):
    # find the length of the strings
    m, n = len(X), len(Y)

    # declaring the array for storing the dp values
    lcc_length = [[None for _ in range(n+1)] for _ in range(m + 1)]
    lcc_content = [[None for _ in range(n+1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcc_length[i][j] = 0
                lcc_content[i][j] = ''

            elif X[i - 1] == Y[j - 1]:
                lcc_length[i][j] = lcc_length[i-1][j-1] + 1
                lcc_content[i][j] = lcc_content[i-1][j-1] + '|' + X[i - 1]

            elif lcc_length[i - 1][j] > lcc_length[i][j - 1]:
                lcc_length[i][j] = lcc_length[i-1][j]
                lcc_content[i][j] = lcc_content[i-1][j]

            else: #lcc_length[i - 1][j] < lcc_length[i][j - 1]:
                lcc_length[i][j] = lcc_length[i][j-1]
                lcc_content[i][j] = lcc_content[i][j-1]

    lcc_content_ = lcc_content[m][n][1:].split('|')
    return lcc_content_

def marking_error(lcc_content, typing_content):
    error_content = list()
    run_id = 0
    for id in range(len(typing_content)):
        if typing_content[id] == lcc_content[run_id]:
            error_content.append(typing_content[id])
            run_id += 1
            if run_id == len(lcc_content):
                for rest_word in typing_content[id+1:]:
                    error_content.append(rest_word.upper())
                break
        else:
            error_content.append(typing_content[id].upper())

    return error_content

def write_error_to_file(error_content, error_file):
    for error_content_id in range(len(error_content)):
        error_file.write(error_content[error_content_id] + ' ')
        if error_content_id % 15 == 14:
            error_file.write('\n')

    error_file.write('\n\n')