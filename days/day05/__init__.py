# trans rights are human rights
#
# solution by gretchen.ostara@gmail.com fka pckeppel@gmail.com

# ==========================================================================
class Problem:
  def __init__(self,dataset):
    self.stacks = []
    self.commands = []
    self.restacked = []
    self.result1 = None
    self.result2 = None

    self.dataset = self.parse(dataset)

  # ------------------------------------------------------------------------
  def parse(self, dataset):    
    stacks = []
    commands = []
    last = 0
    for row in dataset:
      # "[Z] [C] [B]"
      if "[" in row:
        stacks.append(row)
      # "move 3 from 1 to 2"
      elif "move" in row:
        commands.append(row)
      # " 1   2   3 ""   
      elif "".join(row.split()).isdigit():
        last = int(row.split()[-1])

    # parse the stacks into a list:
    # "[['Z', 'N'], ['M', 'C', 'D'], ['P']]"
    self.stacks = [[]]*last
    for row in stacks:
      w = 4 # field width
      p = 0 # position in row
      i = 0 # index of stack

      # step across each row, by a fixed value, then reset.
      while p < len(row):
        # strip out each character, and skip if it's an empty value.
        val = row[p:p+w].strip("[] ")
        if val:
          self.stacks[i] = [val] + self.stacks[i]
        i += 1
        p += w    

    for row in self.stacks:
      print(row)

    # parse the "move" commands:
    # "[1,2,1]" (count, src, dst)
    for row in commands:
      cmd = row.split()
      self.commands.append([int(cmd[1]),int(cmd[3]),int(cmd[5])])

    for row in self.commands:
      print(row)

    self.restacked = self.stacks.copy()
    return


  # ------------------------------------------------------------------------
  def move(self):
    # move elements 1-by-1 from source to destination.
    for cmd in self.commands:
      for i in range(0,cmd[0]):
        self.restacked[cmd[2]-1].append(self.restacked[cmd[1]-1].pop())
    
    for row in self.restacked:
      print(row)
 

  # ------------------------------------------------------------------------
  def part1(self):
    self.move()
    result = "".join([i[-1] for i in self.restacked])

    self.result1 = result
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
