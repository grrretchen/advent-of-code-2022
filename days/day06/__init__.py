# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
import copy

class Problem:
  def __init__(self,dataset):
    self.result1 = None
    self.result2 = None
    self.dataset = dataset


  # ------------------------------------------------------------------------
  def findStart(self, gap=4):
    # the start of a payload is marked by [gap] number of unique characters.
    pos = gap
    for row in self.dataset:
      while pos < len(row):
        # use "set" to create a pure list of unique characters.
        this = set(row[pos-gap:pos])
        if len(this) > gap-1:
          return pos
        pos +=1 

    return False


  # ------------------------------------------------------------------------
  def part1(self):
    self.result1 = self.findStart(4)

    return(self.result1)


  # ------------------------------------------------------------------------
  def part2(self):
    self.result2 = self.findStart(14)

    return(self.result2)


# --------------------------------------------------------------------------
# pull the dataset from a file 
def fetch(fpath):
  dataset = []
  
  with open(fpath, "r") as infile:
    dataset = [line.strip("\n\r") for line in infile.readlines()]
        
  return dataset


# --------------------------------------------------------------------------  
# solve the problems.
def solve(dataset):
  p = Problem(dataset)

  p.part1()
  p.part2()

  return (p.result1, p.result2)  


# --------------------------------------------------------------------------
# do the main 
def main():
  fpath = "./sample.txt" # this is the sample dataset.
  fpath = "./data.txt"
  dataset = fetch(fpath)
  
  r1,r2 = solve(dataset)

  result = {
    "Part 1" : r1,
    "Part 2" : r2
  }

  return result


# ==========================================================================
if __name__ == "__main__" :
  result = main()
  print(result)

# protect trans kids
