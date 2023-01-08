# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    self.dataset = dataset
    self.result1 = None
    self.result2 = None
    self.rank = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def part1(self):
    sum = 0
    for row in self.dataset:
      l = int(len(row)/2)
      p1 = set(list(row[:l]))
      p2 = set(list(row[l:]))
      r = [x for x in p1 if x in p2]
      x = self.rank.find(r[0])+1
      sum += x
    
    self.result1 = sum
    return(sum)

  # ------------------------------------------------------------------------
  def part2(self):
    # store groups of records
    group = []

    # track the overall total
    sum = 0

    for row in self.dataset:
      group.append(row)

      # The list must be processed in groups of 3. If we don't have three records yet, then escape to the next cycle.
      if len(group) < 3:
        continue

      # store each of the 3 records for shorthand.
      g1 = set(list(group[0]))
      g2 = set(list(group[1]))
      g3 = set(list(group[2]))

      # find the single unique element across all three lists and look up the value
      r = [x for x in g1 if x in [y for y in g2 if y in g3]]
      x = self.rank.find(r[0])+1

      # add the value to the sum, then reset the loop.
      sum += x
      print(r, g1, g2, g3)
      group = []

    # set the class result to the sum, and return the value.
    self.result2 = sum
    return(sum)    

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

# protect trans kids
