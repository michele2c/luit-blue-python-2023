
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

print(split_and_join("this is a string"))