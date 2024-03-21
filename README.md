# Data Structures and Algorithms

The goal of this repository is self-learning. As I came to understand a topic I've decided to write down here.
The result that I want to obtain from this is to stick the information on my brain and check if I'm really learning.

# Introduction

Data structures and Algorithms focuses on problem solving, so for us as programers this knowledge is so essencial as fuel to a car.
The programers skills to solve daily problems are very grounded on this knowledge and experience. So, the importance.

# What are Data Structures?

When solvig a problem using algorithms the way that we choice to store data really matter. 
Data Structures can be understood as a strategically way to store data in which it can be accessed and manipulated on computers memory efficiently.
So the data structure will be boldy dependent about the problem we want to solve. 
We can also separate the structures in primitive which includes integers, booleans, floats, characters and the complex ones, such lists, arrays, trees and graphs.

# RAM

The random access memory (RAM) is a very fast but more limited space on computers that is used by CPU to store and manipulate data.
This space is calculated by blocks of bytes that at the end is reduced by bits (1 byte = 8 bits) of 0s and 1s. 
Normally a personal computer have 8 gigabytes (10⁹ bits).

For example the array: [1,3,5] is stored at RAM:

```
...|  1 ||  3 ||  5 |...
...| $0 || $4 || $8 |...
```

The numbers can be seen at the first row and on the second row we can observe the cursor referencing each value.
When we talk about integers the cursor is incremented by 4 at each value. And it's because each interger uses 4 bytes (32 bits) of RAM to store it number (it can be different by language).

That's another example of characters: "abc" at RAM:

```
...|  a ||  b ||  c |...
...| $0 || $1 || $2 |...
```

You could realize something different here? It's is the quantity by which the cursor is incremented, by 1.
It's because in this case characters uses 1 bytes per value to store on RAM (8 bits).

Hence each structure will utilize a different quantity of bits to store its data.

# Static Arrays



# Dynamic Arrays


