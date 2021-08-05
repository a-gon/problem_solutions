def compress(self, chars):
    if len(chars) <= 1:
        return len(chars)
    i = 0
    write = 0
    while i < len(chars):
        j = i + 1
        while j < len(chars) and chars[i] == chars[j]:
            j += 1
            
        group_len = j - i
        chars[write] = chars[i]
        write += 1

        if group_len >= 10:
            for num in str(group_len):
                chars[write] = num
                write += 1
        elif group_len > 1:
            chars[write] = str(group_len)
            write += 1
        
        i = j

    return write