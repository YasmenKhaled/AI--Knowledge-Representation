from utils import *
from logic2 import *

#  read(maria, logic programming book) ==> by(peter lucas)
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_for_question1 = And(Implication(read, by))


#-----------------------------------------------------------

# is_girl(x) ==> like(x, shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_for_question2 = And(Implication(is_girl, like))


#-----------------------------------------------------------

# ? likes( x , shopping)
who = Symbol("?")
knowledge_for_question3  = And(who ,like)

#-----------------------------------------------------------

# city( x ,big , crowdy) ==> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_for_question4 = And(Implication(city, hates))



