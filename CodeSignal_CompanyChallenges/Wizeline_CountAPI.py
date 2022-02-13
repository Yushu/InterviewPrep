from collections import OrderedDict

def folderCount(folder, x, level):
    if folder not in x:
        x[folder] = OrderedDict()
        x[folder]['count'] = 1
        x[folder]['level'] = level
    else:
        x[folder]['count'] += 1
        
def groupFolders(folders, lst):
    for f, data in folders:
        lst.append(data['level'] * '--' + f + ' (' + str(data['count']) + ')')
        del data['count']
        del data['level']
        if data is not None:
            groupFolders(data.items(), lst)
        
def solution(calls):
    od = OrderedDict()
    temp = []
    for call in calls:
        file = call.split('/')
        subdir = od
        for i, val in enumerate(file):
            if i == 0:
                continue
            folderCount(file[i], subdir, i)
            subdir = subdir[file[i]]
    groupFolders(od.items(), temp)
    return temp