ex=input('Expression: ')
x, y, z = ex.split()
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
}

def eval_binary_expr(x, y, z):
    x, z = float(x), float(z)
    return ops[y](x,z)
print (eval_binary_expr(x, y, z))