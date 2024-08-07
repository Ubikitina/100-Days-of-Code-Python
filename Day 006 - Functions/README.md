# Day 6: Learning to Use Functions

## Goal
- Learn to use functions effectively in Python.

## Activities:
- **01-the-hurdles-loop-challenge-1.py**:
  - **Task**: Solve [Hurdle 1 Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json).
  - **Solution**: Created functions to turn right and to jump over a hurdle, then used a for loop to repeat the jump action six times.
  - **Key Functions**:
    - `turn_right()`: Turns the robot right by turning left three times.
    - `one_jump()`: Moves the robot over a hurdle.



- **02-the-hurdles-loop-challenge-2.py**:
  - **Task**: Solve [Hurdle 2 Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json) using a while loop.
  - **Solution**: Used a while loop to repeat the jump action until the robot reaches the goal.
  - **Key Functions**: Same as in Challenge 1.


- **03-the-hurdles-loop-challenge-3.py**:
  - **Task**: Solve [Hurdle 3 Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json) with additional conditions.
  - **Solution**: Used a while loop with conditions to either move forward or jump over hurdles.
  - **Key Functions**: `turn_right()`, `one_jump()`, `front_is_clear()`, `wall_in_front()`.
  - **New Logic**: Check if front is clear or there's a wall in front and act accordingly.


- **04-the-hurdles-loop-challenge-4.py**:
  - **Task**: Solve [Hurdle 4 Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json) with more complex conditions.
  - **Solution**: Used a while loop with multiple conditions to navigate the course.
  - **Key Functions**: `turn_right()`, `at_goal()`, `front_is_clear()`, `wall_in_front()`, `right_is_clear()`.
  - **New Logic**: Handle multiple scenarios including clear front, walls on the right, and right being clear.


- **05-escaping-maze.py**:
  - **Task**: Solve the [Lost in Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).
  - **Solution**: Used a combination of conditions and loops to navigate through the maze.
  - **New Logic**: Ensure continuous movement forward when the front is clear, and then use a series of conditions to navigate turns and dead ends.


## Key Learning Outcomes:
- Mastery of using functions to encapsulate repetitive tasks.
- Understanding and application of loops (`for` and `while`) to solve problems iteratively.
- Development of conditional logic to handle varying scenarios in problem-solving.