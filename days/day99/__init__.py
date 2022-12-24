# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    self.data = dataset

  def part1(self):
    return "Hello"

  def part2(self):
    return "World"



# --------------------------------------------------------------------------
# pull the dataset from a file 
def fetch(fpath):
  dataset = []
  
  with open(fpath, "r") as infile:
    for line in infile:
      dataset.append([int(i) for i in line.strip()])
        
  return dataset


# --------------------------------------------------------------------------  
# solve the problems.
def solve(dataset):
  p = Problem(dataset)

  result1 = p.part1()
  result2 = p.part2()

  return (result1, result2)  


# --------------------------------------------------------------------------
# do the main 
def main():
  # fpath = "./sample.txt" # this is the sample dataset.
  fpath = "./data.txt"
  dataset = fetch(fpath)
  
  r1,r2 = solve(dataset)

  return (r1, r2)


# ==========================================================================
if __name__ == "__main__" :
  result = main()
  print(f"Part 1:  {result[0]}\r\nPart 2:  {result[1]}")

# protect trans kids
