def floodFill(image, sr, sc, newColor):
    if not image:
        return image

    neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def helper(sr, sc, curColor):
        if image[sr][sc] == newColor or image[sr][sc] != curColor:
            return
    
        for r, c in neighbors:
            new_r, new_c = sr + r, sc + c
            if not (0 <= new_r < len(image) and 0 <= new_c < len(image[0])):
                continue
            image[sr][sc] = newColor
            helper(new_r, new_c, curColor)

    curColor = image[sr][sc]
    helper(sr, sc, curColor)
        
    return image