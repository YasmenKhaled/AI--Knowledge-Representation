from utils import *
from logic2 import *


""""
  hates(x,y), hates(y,x) ==> enemies(x, y)
  the correct :
  
  enemies(x, y) ==> hates(x, y) ^ hates(y, x)
  
"""
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates1 = Symbol(f"hates({x}, {y})")
hates2 = Symbol(f"hates({y}, {x})")
knowledge_for_question1 = And(Implication(enemies, And(hates1, hates2)))
# print(knowledge_for_question1.formula())

#-----------------------------
"""
        p(X) ==> (q(X) ==> r(X)).
        the correct:
        p(x) ==> (q(x) ^ r(x))
     
"""

p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge_for_question2 = And(Implication(p , And(q, r)))
# print(knowledge_for_question2.formula())
