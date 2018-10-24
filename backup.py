#Notice: This is a Python recreation of the html file. I made this to show what I visualized when I did the idea.
effort = raw_input("How much effort do you want to put in? Choose a number from 1 to 5 (1 - Light, 5 - Vigorous)")
etype = raw_input("What type of workout do you want? (Cardio[C], Strength[S])")
weight = raw_input("Do you know how much weight you can carry in pounds? [I = I don't know]")
effort = float(effort)
weight = float(weight)
if effort == 1:
  if etype == "C":
    print "You should run or walk 2.5 - 4mph."
  if etype == "S":
    print "You should lift ", weight - 2.5, "pounds."
if effort == 2:
  if etype == "C":
    print "You should run or walk 4 - 6.5mph."
  if etype == "S":
    print "You should lift ", weight, "pounds."
if effort == 3:
  if etype == "C":
    print "You should run or walk 6.5 - 8mph."
  if etype == "S":
    print "You should lift ", weight + 2.5, "pounds."
if effort == 4:
  if etype == "C":
    print "You should run or walk 8 - 10mph."
  if etype == "S":
    print "You should lift ", weight + 5, "pounds."    
if effort == 5:
  if etype == "C":
    print "You should run or walk 10+ mph."
  if etype == "S":
    print "You should lift ", weight + 10, "pounds."    
