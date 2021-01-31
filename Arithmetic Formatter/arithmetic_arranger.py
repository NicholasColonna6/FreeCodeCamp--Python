import re

def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
      return "Error: Too many problems."
    
    my_probs = []
    widths = []
    for problem in problems:
      next_prob = re.findall('\\S+', problem)

      if next_prob[1] != "+" and next_prob[1] != "-":
        return "Error: Operator must be '+' or '-'."
      if not next_prob[0].isdigit() or not next_prob[2].isdigit():
        return "Error: Numbers must only contain digits."
      if len(next_prob[0]) > 4 or len(next_prob[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    
      my_probs.append(next_prob)
      widths.append(max(len(next_prob[0])+2, len(next_prob[2])+2))
 
    arranged_problems = ""
    #adds first number in problems
    for i, prob in enumerate(my_probs):
      arranged_problems += (widths[i] - len(prob[0]))*" " + prob[0]
      if i+1 != len(my_probs):
        arranged_problems += 4*" "
      else:
        arranged_problems += "\n"
    
    #adds operator and second number in problems
    for i, prob in enumerate(my_probs):
      arranged_problems += prob[1] + " " + (widths[i] - 2 - len(prob[2]))*" " + prob[2]
      if i+1 != len(my_probs):
        arranged_problems += 4*" "
      else:
        arranged_problems += "\n"
    
    #adds dashes under problem
    for i in range(len(my_probs)):
      arranged_problems += widths[i] * "-"
      if i+1 != len(my_probs):
        arranged_problems += 4*" "
      
    #adds solution if requested
    if solve == True:
      arranged_problems += "\n"
      for i, prob in enumerate(my_probs):
        if prob[1] == '+':
          solution = int(prob[0]) + int(prob[2])
        else:
          solution = int(prob[0]) - int(prob[2])

        arranged_problems += (widths[i] - len(str(solution)))*" " + str(solution)
        if i+1 != len(my_probs):
          arranged_problems += 4*" "

    return arranged_problems