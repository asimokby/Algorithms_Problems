    def countingValleys(n, s):
      count_valleys = 0
      last_step = 0 
      next_step = 0
      for step in s: 
          if step == "U":
              last_step = next_step
              next_step += 1 
          elif step == "D":
              last_step = next_step
              next_step -= 1

          if last_step == 0 and next_step == -1:
              count_valleys += 1
      return count_valleys
    
    n = input()
    s = input()
    print(countingValleys(n, s))
