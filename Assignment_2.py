# Assignment 2 refactor

# Environment variable)
import os
import re
# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)
#helper function to group file read and write; encourage reuse, reduce, recycle :D
def updateVersionNumber(source_path:str, pattern:str, repl:str) -> None:
    os.chmod(source_path, 0o755) #should be octal number. Sets file permission.
    # Owner -  7 (Read, Write, Execute)
    # Group -  5 (Read, Execute)
    # Others - 5 (Read, Execute)
    #safer to use [with] keyword
    #there is no real need to create another directory for this? Just read and write in place
    #read lines into variable
    file_data:list = None
    with open(source_path, 'r') as fin:
        file_data = fin.readlines()
    for i in range(len(file_data)):
        if re.match(pattern, file_data[i]) != None:
            file_data[i] = re.sub(pattern, repl, file_data[i])
            break #only one line needs to be changed
    #write back
    with open(source_path, 'w') as fout:
        fout.writelines(file_data)
#original code had a lot of repetition. Cut it down by storing strings in variables
def updateSconstruct(version_number) -> None:
    #"Update the build number in the SConstruct file"
    source_path:str = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")
    pattern:str = "point\=[\d]+"
    repl:str = "point=" + version_number
    try:
        updateVersionNumber(source_path, pattern, repl)
    except:
        pass #possible error handling here

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def updateVersion(version_number) -> None:
    #"Update the build number in the VERSION file"
    source_path:str = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")
    pattern:str = "ADLMSDK_VERSION_POINT=[\d]+"
    repl:str = "ADLMSDK_VERSION_POINT=" + version_number
    try:
        updateVersionNumber(source_path, pattern, repl)
    except:
        pass #possible error handling here

def main():
    #grab version number first
    version_number = os.environ["BuildNum"]
    #added argument to make it more flexible
    updateSconstruct(version_number)
    updateVersion(version_number)
main()