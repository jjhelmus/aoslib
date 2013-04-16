#! /usr/bin/env python


def make_func_stub(line):
    command, comment = line.split('!')
   
    if '(' not in command:
        return

    sub_start = command.index('subroutine')
    brace_start = command.index('(')
    brace_end = command.index(')')

    routine = command[sub_start+10:brace_start].strip()
    args = command[brace_start+1:brace_end].split(',')

    defline = "def " + routine + "(" + ", ".join(args) + "):"
    
    print ""
    print "" 
    print "#", comment[:-1]
    print defline
    print "    \"\"\""
    print ""
    print "    Parameters"
    print "    ----------"
    for arg in args:
        print "   ", arg, ":"
        print "        T"
    
    print ""
    print "    Returns"
    print "    -------"
    print ""
    print ""
    print "    \"\"\""
    print "    # return _awips." + routine + "(" + ", ".join(args) + ")"
    print "    raise NotImplemented"

if __name__ == "__main__":
    
    signature_file = "_awips.pyf"
    f = open(signature_file)
    for line in f:
        if "subroutine" in line and "end subroutine" not in line:
            make_func_stub(line)

    f.close()

