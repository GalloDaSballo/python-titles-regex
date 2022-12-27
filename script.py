import re

def main():
  f = open("data", "r")
  data = f.read()
  regex = "(###\s.{1,})"
  found = re.findall(regex, data)

  for s in found:
    print("")
    print(s)
    print("")