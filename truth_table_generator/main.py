import truthtable;

def f(a:bool, b:bool, c:bool) -> bool:
    return (a and b) or (not c);

truthtable.print_truth_table(f);
