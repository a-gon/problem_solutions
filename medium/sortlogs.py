def reorderLogFiles(logs):
    if not logs:
        return []
    digLogs = []
    letLogs = []
    for log in logs:
        idf, content = log.split(' ', 1)
        if content[0].isalpha():
            letLogs.append(log)
        else:
            digLogs.append(log)
            
    letLogs.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
    
    return letLogs + digLogs