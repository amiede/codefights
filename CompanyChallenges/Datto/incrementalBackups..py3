# https://app.codesignal.com/company-challenges/datto/NWoHovD8M48E9Diwr
def incrementalBackups(lastBackupTime, changes):
    
    backups = []

    for i in range(len(changes)):
        print(changes[i][0])
        if changes[i][0] > lastBackupTime:
           if changes[i][1] not in backups:
            backups.append(changes[i][1])
    
    return sorted(backups)