from collections.abc import Callable;

import inspect;
import string;


def bin_pad(i, length):
    binary_str:str = bin(i).replace('0b', '');
    
    while len(binary_str) != length:
        binary_str = '0' + binary_str;
    
    return binary_str;


def print_truth_table(f:Callable):
    N_ARGS=len(inspect.signature(f).parameters);
    ARGS  =list(inspect.signature(f).parameters);
    NAME  =f.__name__;
    
    for _ in range(N_ARGS+1):
        print("___", end='');
    #print("_");
    print();
    for ARG in ARGS:
        print(ARG,end=' | ');
    print(NAME);
    for _ in range(N_ARGS+1):
        print("---", end='');
    #print("-");
    print();

    for i in range(2**N_ARGS):
        args:dict = dict([ (ARGS[idx],bool(int(v))) for idx,v in enumerate(list(bin_pad(i, N_ARGS))) ]);

        for i,(k,v) in enumerate(args.items()):
            print(int(v), end=' | ');
        print(int(f(**args)));

def print_k_map():
    """
    for _ in range(N_ARGS):
        print("-",end='');
    print();
    """
    
    
#print_truth_table();
#print_k_map();
