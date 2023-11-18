#Jay Bacchus
#agyei.bacchus92@myhunter.cuny.edu
#Sample program that loops from 50 down to 0


ADDI $s0, $zero, 0
ADDI $s1, $zero, 5
ADDI $t0, $zero, 50
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $t0, DONE
J AGAIN
DONE:  