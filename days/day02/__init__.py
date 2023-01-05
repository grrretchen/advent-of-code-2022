# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    # comparisons of two values
    self.data = dataset
    self.clean = []
    self.map1 = [[0,0,0],[2,1,3],[3,2,1],[1,3,2]]

    self.result1 = None
    self.result2 = None
 
  def convert1(self):
    set1 = [1, 2, 3]
    set2 = ["A","B","C","X","Y","Z"]

    for row in self.data:
      a = row.split(" ")
      self.clean.append([set1[set2.index(a[0])%3], set1[set2.index(a[1])%3]])

  # plain map based on ABC,XYZ mapping to RPS (rock-paper-scissors)
  def part1(self):
    self.convert1()
    scoring = [[0,0,0],[2,1,3],[3,2,1],[1,3,2]]
    scores = []
    for e in self.clean:
      scores.append(
        [
          e[0] + scoring[e[0]].index(e[1])*3,
          e[1] + scoring[e[1]].index(e[0])*3
        ]
      )

    self.result1 = {
      "Opponent" : sum([e[0] for e in scores]),
      "Player" : sum([e[1] for e in scores])
    }

    pass

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
