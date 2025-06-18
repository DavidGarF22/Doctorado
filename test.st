PROGRAM test
VAR
    my_trigger : R_TRIG;
    input : BOOL;
    output : BOOL;
END_VAR

my_trigger(CLK := input);
output := my_trigger.Q;
END_PROGRAM

CONFIGURATION Config0
    RESOURCE Res0 ON PLC
        TASK Main(INTERVAL := T#50ms, PRIORITY := 0);
        PROGRAM Inst0 WITH Main : test;
    END_RESOURCE
END_CONFIGURATION
