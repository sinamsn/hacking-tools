import argparse

parser = argparse.ArgumentParser(description="A tool for removing 'www.' from first of found subdomains")
parser.add_argument('-i', action="store", dest="filename",required=True,default="inp.txt")
parser.add_argument('-o', action="store", dest="output",required=True,default="out.txt")
given_args = parser.parse_args()
filename, output = given_args.filename, given_args.output


with open(filename,"r") as file:
    with open(output,"w") as file2:
        for line in file.readlines():
            print(line)
            if line.startswith("www."):
                file2.write(line[4:])
            else:
                file2.write(line)
                print(line)