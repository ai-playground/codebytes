
# Problem 1
# Generate All Possible Expressions That Evaluate To The Given Target Value

def generate_all_expressions(s, target):
    all_expression = list(range(2*len(s)))
    cur_expression = list(range(2*len(s)))
    generate_all_expressions_recur(s,0,cur_expression,0,all_expression,target)
    return all_expression

def generate_all_expressions_recur(s,i,cur_expression,j,target,all_expression):
    
    if i == len(s):
        if evaluate_expression(cur_expression) == target:
            all_expression.append(cur_expression)
            #print("".join(out[:j]))
        return
    
    cur_expression[j] = s[i]
    
    cur_expression[j+1] = "c"
    #new_target = target - int(s[i])*(10**(len(s)-i))
    generate_all_expressions_recur(s,i+1,cur_expression,j+2,target,all_expression)
    
    cur_expression[j+1] = "*"
    #new_target = target/int(s[i])
    generate_all_expressions_recur(s,i+1,cur_expression,j+2,target,all_expression)
    
    cur_expression[j+1] = "+"
    #new_target = target - int(s[i])
    generate_all_expressions_recur(s,i+1,cur_expression,j+2,target,all_expression)
    return 


def evaluate_expression(cur_expression):
    s = cur_expression.copy()
    n = len(s)
    
    for i in range(n):
        if i == "c":
            s[i-1] = int(s[i-1])*10 + int(s[i+1])
            s[i:] = s[i+2:]
            
    for i in range(n):
        if i == "*":
            s[i-1] = int(s[i-1])*int(s[i+1])
            s[i:] = s[i+2:]
            
    for i in range(n):
        if i == "+":
            s[i-1] = int(s[i-1])+int(s[i+1])
            s[i:] = s[i+2:]
            
    return int(s[0])