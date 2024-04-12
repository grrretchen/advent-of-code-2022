# Advent of Code 2022 - Day 04
# https://adventofcode.com/2022/day/4
#
# solution by gretchen.keppel@gmail.com
# protect trans kids

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    self.dataset = dataset
    self._scrub(self.dataset)
    self.result1 = None
    self.result2 = None


  # ------------------------------------------------------------------------
  def _scrub(self,dataset):
    result = []
    for row in dataset:
      # the dataset is formatted like "2-4,5-7", with each group representing a range of numbers.

      group = []
      for g in [g.split("-") for g in row.split(",")]:
        group.append([int(e) for e in g])

      # after splitting the row, sort so that the first record is always <=.
      group.sort()

      # store to the result.
      result.append(group)

    self.dataset = result


  # ------------------------------------------------------------------------
  def part1(self):
    overlap = 0
    # find cases where one dataset is completely self-contained.
    for row in self.dataset:
      if row[0][0] == row[1][0]:
        overlap +=1
      elif row[0][0] < row[1][0]:
        if row[0][1] >= row[1][1]:
          overlap += 1

    self.result1 = overlap
    return(self.result1)


  # ------------------------------------------------------------------------
  def part2(self):
    overlap = 0
    # find cases where one dataset is only partially contained.
    for row in self.dataset:
      if row[0][0] == row[1][0]:
        overlap += 1
      elif row[0][0] <= row[1][0]:
        if row[0][1] >= row[1][0]:
          overlap += 1
    
    self.result2 = overlap
    return(self.result2)


# --------------------------------------------------------------------------
# pull the dataset from a file 
def fetch(fpath):
  dataset = []
  
  with open(fpath, "r") as infile:
    dataset = [line.strip(" \n\r") for line in infile.readlines()]
        
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
