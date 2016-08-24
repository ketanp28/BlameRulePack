import os


def modifiedFileContent(filename,commitId,repoDir):
    parent = commitId + '^'
    data = []

    os.chdir(repoDir)

    cmdDiffData = "git show "+commitId+" -U9999"
    output = os.popen(cmdDiffData).read() + "diff --git a/"

    start = "+++ b/"+filename
    end = "diff --git a/"

    flag = False;
    for line in output.splitlines():
        if(line == start):
            flag = True;
            continue
        if(line.startswith(end) and flag):
            break
        if(flag):
            data.append(line)

    fileContent = '\n'.join(data)

    i = fileContent.index('\n')
    fileContent = fileContent[i+1:]

    fo = open(filename + ".txt", 'w+')
    fo.write(fileContent)

    fo.close()


if __name__ == "__main__":
    commitId = "153d6ea8fcc"
    repoDir = "/Users/ketanpatil/Desktop/bugattribution/fdinet"
    filename = "fdinet-core/src/main/java/fdinet/core/web/URLProcessor.java"

    modifiedFileContent(filename,commitId,repoDir)



