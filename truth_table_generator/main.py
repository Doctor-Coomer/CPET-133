import truthtable;

def f(a:bool, b:bool) -> bool:
    return (a and b);

truthtable.print_truth_table(f);
