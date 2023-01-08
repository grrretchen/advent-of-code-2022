# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    self.dataset = dataset
    self.result1 = None
    self.result2 = None

  # ------------------------------------------------------------------------
  def part1(self):
    overlap = 0
    for row in self.dataset:
      # the dataset is formatted like "2-4,5-7", with each group representing a range of numbers.

      group = []
      for g in [g.split("-") for g in row.split(",")]:
        group.append([int(e) for e in g])

      # after splitting the row, then compare the second digits.
      group.sort()
      if group[0][0] == group[1][0]:
        overlap +=1
      elif group[0][0] < group[1][0]:
        if group[0][1] >= group[1][1]:
          overlap += 1
      else:
        print("%s\t%s\t%s"%(group[0],group[1],group[0][1] >= group[1][1]))

    self.result1 = overlap
    print(overlap)
    pass

  # ------------------------------------------------------------------------
  def part2(self):
    pass

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

# protect trans kids
