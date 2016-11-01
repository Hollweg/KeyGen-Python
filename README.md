#KeyGen-Python

##The purpose

Software for **pseudo-random keys generation using python language.**

##Utility

The algorithm objective is the key generation in a **pseudo-random** way that can be implemented in simple ambients that involve **information security**. </br>
The Keygen uses a seed based in a list of 16 inputs, having 4 bits each.

##How it works?

The generation key algorithm works in the following form: 

1. Generate (pseudo-randomically) a list containing 16 algarisms from 0 to 9. </br>
2. Search this list and every term must be squared. So, it is picked up the rest of the division by 2 (it must return 0 or 1). </br>
3. These values must be converted to hexadecimal and a patterns is mantained, converting all terms in list to uppercase. </br>
4. There is a possibility of the algorithm contain less than 10 digits. If this occurs, the process is redone, and are generated new words. </br>
5. Returns the generated key in the format: "XXXXXXXXXX", where X is a number (0-9) or a capital letter from A to F, with a minimum size of 10 characters each key. 

##Copyright

**The project can be reproduced with no problem.** </br>
However, I only ask you to **mantain original credits/references to the author.**


Enjoy!

Hollweg


