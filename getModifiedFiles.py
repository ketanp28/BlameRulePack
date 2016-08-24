import os

def getFiles(commitId,repoDir):
    parent = commitId+'^'
    modifiedFiles = []

    os.chdir(repoDir)

    cmdFileList = "git diff "+parent+" "+commitId+" --numstat"
    output = os.popen(cmdFileList).read()

    for line in output.splitlines():
        parts = line.split()
        added = int(parts[0])
        deleted = int(parts[1])
        fileName =parts[2]

        if(deleted>0):
            modifiedFiles.append(fileName)

    return modifiedFiles

def test():
    os.system('ls')

if __name__ == "__main__":
    commitId = "153d6ea8fcc"
    repoDir = "/Users/ketanpatil/Desktop/bugattribution/fdinet"

    filelist = getFiles(commitId,repoDir)
    print(filelist)

