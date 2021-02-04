# Nicholas Colonna

def arithmetic_arranger(problems, solve=False):
    """ Returns a string that vertically formats arithmetic problems given as a string, solving if specified

        Keyword arguments: 
        problems -- list of strings containing addition and subtraction problems
        solve -- boolean specifying whether to solve the problems (default: False)

    """

    if len(problems) > 5:     # Five is the max number of problems allowed
        return "Error: Too many problems."   
    
    my_probs = [] 
    widths = []    # Keeps track of length of number with most characters in each problem for formatting
    for problem in problems:
        cur_prob = problem.split(" ")
        if cur_prob[1] != "+" and cur_prob[1] != "-":
            return "Error: Operator must be '+' or '-'."  
        elif not cur_prob[0].isdigit() or not cur_prob[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif len(cur_prob[0]) > 4 or len(cur_prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
        my_probs.append(cur_prob)
        widths.append(max(len(cur_prob[0]), len(cur_prob[2]))+2)
 

    arranged_problems = ""
    # Build first line of our problems (first number)
    for i, prob in enumerate(my_probs):
        arranged_problems += (widths[i] - len(prob[0])) * " " + prob[0]
        if (i + 1) != len(my_probs):
            arranged_problems += 4 * " "
        else:
            arranged_problems += "\n"   # no spacing needed for last problem, start new line
    
    # Build second line of our problems (operator and second number)
    for i, prob in enumerate(my_probs):
        arranged_problems += prob[1] + " " + (widths[i] - 2 - len(prob[2])) * " " + prob[2]
        if (i + 1) != len(my_probs):
            arranged_problems += 4 * " "
        else:
            arranged_problems += "\n"   # no spacing needed for last problem, start new line
    
    # Build dashes to separate solutions
    for i in range(len(my_probs)):
        arranged_problems += widths[i] * "-"
        if (i + 1) != len(my_probs):
            arranged_problems += 4 * " "
      
    # Build final line if needed (solution)
    if solve == True:
        arranged_problems += "\n"
        for i, prob in enumerate(my_probs):
            if prob[1] == '+':
                solution = int(prob[0]) + int(prob[2])
            else:
                solution = int(prob[0]) - int(prob[2])

            arranged_problems += (widths[i] - len(str(solution))) * " " + str(solution)
            if (i + 1) != len(my_probs):
                arranged_problems += 4*" "

    return arranged_problems