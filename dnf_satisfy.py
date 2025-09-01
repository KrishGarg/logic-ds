from data_structures import Literal

def satisfy_block(lits: list[Literal]):
    for i in range(len(lits)):
        for j in range(i+1, len(lits)):
            if (lits[i].getNegation() == lits[j]):
                return False
            
    return True


def satisfy_formula(formula: str):
    formula = formula.replace(" ", "")
    Cs = formula.split("|")

    for C in Cs: # m
        C = C.replace("(", "")
        C = C.replace(")", "")

        lits = [Literal(l) for l in C.split("&")]
        if (satisfy_block(lits)): # k^2
            return True
        else:
            continue # redundant but good for understanding
    
    return False

def tester():
    formula = input("Enter formula: \n");
    if satisfy_formula(formula):
        print("It is satisfiable")
    else:
        print("It is unsatisfiable")

def rules():
    print("Rules to follow: \n")
    print("- Use proper DNF notation.")
    print("- No brackets for negating an atomic proposition.")
    print("- Use bracket to contain single string of conjunctions. No brackets at the ends needed.")
    print("- Literal statements can be any continuous string of letters, adding ~ before is considered negation.")
    print("- '&' for conjunction, '|' for disjunction, '~' for negation")
    print("- Example for satisfiable: (p & ~q) | (p & r & ~p) | (p & ~s)")
    print("- Example for unsatisfiable: (p & ~q & ~p) | (p & r & ~p) | (p & ~s & ~r & s)")
