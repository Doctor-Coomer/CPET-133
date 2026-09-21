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

    SEPERATOR=' | ';

    
    args_str:str = "";

    for ARG in ARGS:
        args_str += (ARG + SEPERATOR);
    args_str += NAME;
    
    
    for _ in range(len(args_str)):
        print("_", end='');
    print();

    print(args_str);
    
    for _ in range(len(args_str)):
        print("-", end='');
    print();

    for i in range(2**N_ARGS):
        args:dict = dict([ (ARGS[idx],bool(int(v))) for idx,v in enumerate(list(bin_pad(i, N_ARGS))) ]);

        for i,(k,v) in enumerate(args.items()):
            print(int(v), end=SEPERATOR);
        print(int(f(**args)));

def print_k_map():
    """
    for _ in range(N_ARGS):
        print("-",end='');
    print();
    """
    ...;
    
#print_truth_table();
#print_k_map();
