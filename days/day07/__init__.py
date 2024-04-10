# solution by gretchen.keppel@gmail.com fka pckeppel@gmail.com
# protect trans kids

# ==========================================================================
import copy

class Problem:
  def __init__(self,dataset):
    self.result1 = None
    self.result2 = None
    self.dataset = dataset


  # ------------------------------------------------------------------------
  def part1(self):
    return(self.result1)


  # ------------------------------------------------------------------------
  def part2(self):
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
  # fpath = "./data.txt"
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
