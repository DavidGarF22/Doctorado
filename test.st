PROGRAM test
VAR
    my_trigger : R_TRIG;
    input : BOOL;
    output : BOOL;
END_VAR

my_trigger(CLK := input);
output := my_trigger.Q;
END_PROGRAM
