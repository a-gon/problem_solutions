def findWords(self, board, words):
    
    vocabulary = {}
    
    for word in words:
        cur = vocabulary
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['end'] = word   # signifies that this is a word
    
    # print(vocabulary)
    def backtracking(row, col, parent):

        next_cells = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        letter = board[row][col]
        cur_node = parent[letter]
        # print(cur_word + letter)
        found_word = cur_node.pop('end', False)   # check if this is a word, if it is - remove it from vocabulary so that there's no duplicates
        if found_word:
            found_words.append(found_word)
        
        board[row][col] = '#'                      # mark as visited
        # explore the neighbor cells: 
        for r, c in next_cells:
            next_r, next_c = row + r, col + c
            if next_r < 0 or next_r >= len(board) or next_c < 0 or next_c >= len(board[0]):
                continue
            if board[next_r][next_c] not in cur_node:
                continue
            backtracking(next_r, next_c, cur_node)

        board[row][col] = letter                 # restore the letter
        
        if not cur_node:
            parent.pop(letter)
        
        
    found_words = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            # for each cell, start a word there 
            if board[r][c] in vocabulary:
                backtracking(r, c, vocabulary)
            
            
    
    return found_words