# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # The objective is to evaluate an integer expression using reverse polish notation.
    # Firstly, I should create a stack to organise both the numbers and operators. 
    # Through the stack I will loop through the list from left to right for each token.
    # If the token is a number it will be appended into the stack, and if it is an operator,
    # it will be popped in between the last two numbers in the stack.
    # Once all the tokens have been evaluated, the values are retured to the stack and the
    # expression can be solved.
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    operators = {"+", "-", "*", "/"}
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
            continue
       
        b = stack.pop()
        a = stack.pop()
        
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]




def decode_string(s):
    # Outline:
    # The goal is to decode a string with the rule k[encoded]. To start I will
    # create a stack to store the initial strings with the k[encoded] rule. 
    # Then I will loop through each character in the string. If the character is a number,
    # it will be added as repeated count. Then wherever there is a opening bracket, I will append 
    # the current string and the repeated number count into the stack.
    # When there is a closing bracket, the previous string and repeat count will be popped
    # and then combined into the current string.
    # For all other cases, I will add the character to the current string.
    # Lastly, the decoded string is returned.
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_num = 0
    current_string = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count
        else:
            current_string += char

    return current_string


def daily_temperatures(temps):
    # Outline:
    #  To begin I will create a list with 0's inside a stack.
    # Then loop through the the given temperatures in their indexes and track how many days taken to get
    # a warmer temperature. If the current temperature is warmer than the last day in the stack, 
    # the index will be popped. Next I calculate how many days have passed and store it in the previous
    # day index. This is repeated while there are previous days needing a warmer temperature.
    # Lastly, the current index is pushed onto the stack and the list is returned.
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    
    result = [0] * len(temps)
    stack = []
    for i in range(len(temps)):
        while stack and temps [i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day
        stack.append(i)
    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   Firstly, I will create a check when the grid is empty which returns 0 by default.
    # Then, I will make a set of stored co-ordinates and a counter for the number of islands
    # After I will loop through each row and column in the grid. If there is a 1 that hasn't
    # been found, it will be added to the queue. Next a while loop is ran through the
    # queue to check all 4 directions. If the value in the grid is connected it will be added
    # to the queue. Then once all rows and columns are checked the total island count is returned.
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                island_count += 1
                stack = [(r, c)]
                visited.add((r, c))
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                            stack.append((nr, nc))
                            visited.add((nr, nc))
    return island_count

    


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
    print(eval_rpn(["3", "4", "+"])) # 7
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) # 22

    print(decode_string("3[a]2[bc]")) # "aaabcbc"
    print(decode_string("3[a2[c]]")) # "accaccacc"
    print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"
    print(decode_string("abc")) # "abc"

    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60])) # [1, 1, 1, 0]
    print(daily_temperatures([30, 60, 90])) # [1, 1, 0]
    print(daily_temperatures([50])) # [0]

    
    print(num_islands(["11110", "11010", "11000", "00000"])) # 1
    print(num_islands(["11000", "11000", "00100", "00011"])) # 3
    print(num_islands(["000"])) # 0
    print(num_islands(["1"])) # 1
    print(num_islands([])) # 0




if __name__ == "__main__":
    main()
