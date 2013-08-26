#! /usr/bin/env python


def make_table_line(line):
    command, comment = line.split('!')
   
    if '(' not in command:
        return

    sub_start = command.index('subroutine')
    brace_start = command.index('(')
    brace_end = command.index(')')

    routine = command[sub_start+10:brace_start].strip()
    filename = comment.split(':')[-1].strip()

    return routine, filename
    #print routine.ljust(15), filename.ljust(16), "No   ", "No one"
    #return len(filename)

if __name__ == "__main__":
   
    signature_file = "_awips.pyf"
    f = open(signature_file)
    print "=============== ================ ===== ================"
    print "Subroutine      Source file      Done  Assigned To"  
    print "=============== ================ ===== ================"
    
    table_lines = []
    for line in f:
        if "subroutine" in line and "end subroutine" not in line:
            table_lines.append(make_table_line(line))
    # no () so funny
    table_lines.append(('radrtns', 'radrtns.f'))
    table_lines.sort()

    f.close()
    for line in table_lines:
        if line != None:
            routine, filename = line
            print routine.ljust(15), filename.ljust(16), "No   ", "No one"

    print "=============== ================ ===== ================"
