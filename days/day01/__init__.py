# solution by gretchen.keppel@gmail.com fka pckeppel@gmail.com
# protect trans kids

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    # groups of numbers are separated by a blank record
    self.data = dataset
    self.totals = [0]
    self.result1 = None
    self.result2 = None

  # find the largest total across all groups of numbers
  def part1(self):
    for each in self.data:
      if each.isdigit():
        self.totals[-1] += int(each)
      else:
        self.totals.append(0)

    self.result1 = max(self.totals)

  def part2(self):
    self.totals.sort(reverse=True)
    self.result2 = sum(self.totals[0:3])



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
