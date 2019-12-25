import os
import sys
from Parser import CompilationEngine

def jackanalyzer_run(inputFileDir, outPutFileDir):
    jackfilenames = [f for f in os.listdir(
        inputFileDir) if f.endswith(".jack")]

    for jackfilename in jackfilenames:
        print(jackfilename)
        inputfilepath = os.path.join(inputFileDir, jackfilename)
        outputfilepath = os.path.join(
            outPutFileDir, jackfilename.split(".")[0]+".xml")
        
        jackcompiler = CompilationEngine(inputfilepath, outputfilepath)

        jackcompiler.compile()
        jackcompiler.writer.close()

        print("Write: " + outputfilepath)
    print("All files wrote!")

def main():
    inputfiledir = sys.argv[1]
    outputfiledir = sys.argv[2]
    jackanalyzer_run(inputfiledir, outputfiledir)

if __name__ == "__main__":
    main()