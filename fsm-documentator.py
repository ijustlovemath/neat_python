import sys

# hacky argparse to follow, could be extended
# default value of name for the FSM
name = "state_machine"
if len(sys.argv) == 3:
    switch, tmp = sys.argv[1:]
    if switch == "--name":
        name = tmp

lines = sys.stdin.readlines()
prefix = "@DOT: "
print(f"digraph {name} {{")
for line in lines:
    if prefix in line:
        edge = line.rstrip().split(prefix, 1)[1]
        if "->" in edge:
            print(f"  {edge};")
        else:
            print(f"[WARNING] Improperly formatted graph edge: {edge}", file=sys.stderr)
print("}")
