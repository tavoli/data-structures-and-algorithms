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

# Arrays
A contiguous data that is represented in the same way that is the RAM. Each type of data need a different quantity of bits in a RAM, for example, integer 32 bits or characters 8 bits, so at each 32 bits or 8 bits one value will be saved and so on, continuaslly.

Arrays performance:

r(read), ins(insert), del(delete), mid(middle)

|   r   | ins/del mid | ins/del end |
|  ---  | ----------- | ----------- |
|  O(1) | O(n)        | O(1)        |

Arrays have constant time operation to read and to insert/delete at the end, and it's because these operations uses the index of the array to do. The indexes are the way that arrays know where in memory the value are. So, for every value containing on a array, we have a index. The worst cases when manipulating a array are if we need to ins/del at the middle. It's for the way arrays are: contiguous in memory. We cannot delete an item at the middle and let there a hole, it would break the array in two parts and the second part we would loose for do not known it anymore. Then, for operations on the middle, we need to shift all the rest of values to accomodate the changes.

# Static Arrays
Are fixed size of arrays pre-allocatted on compilation time. It means that before the algorithm run we already know the quantity of bits the CPU will need to execute the task. So we say to the computer to save that space on a RAM to us and then nothing can use it even if we not utilize that space entirelly, hence we can notice that when we use that kind of arrays we are reservating memory to use on the present, future or never. 

# Dynamic Arrays
When using languages like python or javascript, that is the default type of array offerred to be used. This type of array works by calculating the size of the array automaticly for us. As the arrays need to be stored continuously in memory we always need to know the space we would need to use this kind of structure. When we do not know, we can create a strategy where when the algorithm reach the limit of the array, it can create another new array with doubled size of the first, then move all elements from the first to the second. So it is what happens under the hood when we use dynamic arrays.
Realize that not always the insertion operation at the end will be O(1) - constant time, but can be O(n) if we are in cases in which we need to create another array with doubled size and move all elements to the another one.

# Stack
One of the most common data structures of all. This is used on arrays and have a law that it works called as LIFO (Last in First Out). In stack all operations are made at the end. It means that insertions goes on the end together with deletes.

In our wordly view one example of place we often use this law is on set of plates. Take notice that always we used to get a plate from the top of the set (delete) and after wash it to return the object to the set we put that at the top again (push/append).

As this structure delete objects from its sets from the top (the very end), the output of the removed items will be in reverse order. Which can be very interesting to use on tasks that demands reverse of strings or when we need to read the objects from the top.

Stacks technically supports the operations push, delete and peek. As all these operations occur at top of the array and don't need to rearrange the containing items in the array ending up with a very fast O(1) - constant time type of structure.


