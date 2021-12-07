from logic2 import *


#  Carrots color is orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(
    Implication(carrots, orange)
)

#---------------------------------------------------

# in English : 
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))

#---------------------------------------------------

# in English : 
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)

#---------------------------------------------------

# in English : 
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)

#---------------------------------------------------

# in English : 
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)

#---------------------------------------------------

# in English : 
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))

