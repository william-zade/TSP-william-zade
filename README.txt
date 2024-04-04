# Zade
## Solving The Traveling Salesman Problem Using Python

### OBJECTIVES:
  
1. Understand the Traveling Salesman Problem (TSP)
2. Algorithmic Design
3. Data Structures Design
4. Documentation
    - Recommended: Read all the way through the slide deck once before you start doing any of the work. But there may be notes about what NOT to do that will save you time and frustration.

### NOTES:

This week we begin implementing the Traveling Salesman Problem. This is a class of problems that appear in planning and logistics domains. For example, if you need to travel to 20 cities, it would be good to know the order of cities to visit to drive the least miles, thus saving on gas, time and vehicle wear and tear.
However, before we get too far down that path, we need to:
- Understand the problem
- Design a data structure to hold our problem
- Code to load and display our data structure for testing

Not every node you start at will yield a nearest neighbor solution. Two different starting nodes could yield different total path weights. Must check all paths and determine which ones visited every node and which of those had the least path weight total. A node/vertex is connected to other nodes/vertices (neighbors) via edges with weights.

### Node Connections:
- The number next to the node connection is the weight of that connection
    1. A connects to node B (23) and C (19)
    2. B connects to node A (23) and D (5)
    3. C connects to node A (19) and D (50)
    4. D connects to node B (5) and C (50)

The whole network is designed as a Triangle, with nodes A, B, and C being the points of the Triangle, and node D being in the center of that triangle.

The traveling salesman problem states that I must develop an algorithm where the salesman can start at a node, travel to each node only once, reach every node, and stop on the node he started from. The problem also states that we should travel in the most efficient way possible, meaning the lowest weighted travel that we can achieve to preserve energy.

The Nearest Neighbor solution suggests that when we are presented with two weighted options, we should choose the lower weight of those options unless it leads to a node that we have already been to. In that case, even though it is a lower weighted option, it no longer counts as a viable route.

### TASKS:

#### Task #1:
Create a README file
- All your notes should be in this file. You can add graphs or illustrations to this graph if you need to. Please use syntax formatting when you add content to your file.
- The top of your README file should look like the following:
    * # <your last name>
    * ## Solving The Traveling Salesman Problem Using Python

#### Task #2:
Using the graph on slide 9 (now in my noteAssets folder), determine all the circuits and their total cost.
- Document this in your README.md file (including a picture of your graph)
    (hint, store any snapshots or graphics in a folder called noteAssets)

- I ran these by hand after struggling to develop a Python code to automate these findings automatically. I will need to reapproach the Python code again and implement changes that will produce these results.

#### Solutions from Node A:
1. A > C (19)
2. C > B (10)
3. C > D (5)
4. No possible solution without violating the Nearest Neighbor principle.
5. Total possible weight = 34

#### Solutions from Node B:
1. B > D (5)
2. D > C (50)
3. C > A (19)
4. A > B (23)
5. Only possible solution from node B without violating the Nearest Neighbor principle.
6. Total weighted score = 97

#### Solutions from Node C:
1. C > B (10)
2. B > D (5)
3. No possible solution without breaking the Nearest Neighbor principle.
4. Total possible weight = 15

#### Solutions from Node D:
1. D > B (5)
2. B > C (10)
3. C > A (19)
4. No possible solution without breaking our Nearest Neighbor principle and no repeat visit to a node.
5. Total possible weight = 34


#### Task #3:
Design a data structure that holds all the nodes in your graph and all the neighbors and edge weights. NO code!
- Document in your README.md file.

  For this task, I've chosen to represent the graph using an adjacency list. In this data structure:
    - Each node is associated with a dictionary containing its neighbors as keys and the corresponding edge weights as values.
    - This representation allows for efficient access to neighbors and their edge weights.

Example:
```python
graph = {
    'A': {'B': 23, 'C': 19},
    'B': {'A': 23, 'D': 5},
    'C': {'A': 19, 'D': 50},
    'D': {'B': 5, 'C': 50}
}


#### Task #4:
Lastly, create a local GIT Repo.
- Push your REPO to your BitBucket account.
- Give access to me: mthoney@sheridan.edu

I connected my replit account with my Github account, and the associated Github page for this particular repository is:
  https://github.com/william-zade/replit-sdev

I am next connecting this to my bitbucket account, and then also pushing my git commits to my own personal git repo on my Home account on my desktop.



Of course I got carried away and hyper-focused on developing a Python Program that could do what I could do by hand in a few minutes. After several hours, it occured to me that it was unnecessary to the assignment at hand. HOWEVER, as a Software Developer it is good practice for me to get into the habit of documenting what I have done so far so that when I come back to the project (or someone else for that matter) they will have a good idea of what work has already been done, where we are at now, and what still needs to happen (ideally).


# Summary of TSP Solver Development

## Steps Taken:

### 1. Initial Setup:
   - Defined the graph representing cities and connections with weights.

### 2. Finding All Paths:
   - Implemented `find_all_paths` function to explore all possible paths in the graph.
   - Ensured each node is visited only once and ended at the origin node.
   - Considered connection weights to choose the next node.

### 3. Calculating Total Value:
   - Created `calculate_total_value` function to compute the total connection value for a given path.

### 4. Finding All Solutions:
   - Developed `find_all_solutions` function to find all possible solutions by exploring paths starting from each node.

### 5. Printing Solutions:
   - Printed all solutions, iterating through the list of solutions and displaying each path with its total connection value.
   - Differentiated between viable and non-viable solutions based on the last node in the path.

### 6. Troubleshooting:
   - Identified and fixed issues such as not printing solutions and incorrect formatting.
   - Used print statements and logic review to debug the code.

### 7. Finalizing:
   - Refined the code to handle the final leg of travel and print solutions in different colors based on viability.

### 8. Summary for README:
   - Documented the steps taken in this README file for future reference and troubleshooting.

Currently code is non-functional and still needs further debugging. The graph is currently "undefined" as far as the logic is concerned, somehow, and will need addressed.