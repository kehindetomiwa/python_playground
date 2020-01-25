import os

def disk_usage(path):
    '''
     input: path to the directory
     output: cummulative disk space used by the
             directory and the child entry
    '''
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total

disk_usage('/Users/kehindetomiwa/Documents/DS_Materials/code/python')
