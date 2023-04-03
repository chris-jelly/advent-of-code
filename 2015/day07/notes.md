# This is gonna be tough

## Plan
- We need to map the status of all of the variables
  - a list of dicts?
    - (bn{value}, lf{value})
- We need to parse (Regex, here we go again) the string for:
  - first variable
  - Command
  - second variable
  - result variable
- We need to understand what each bitwise operation does.
  - Probably need a function that performs bitwise operations?
- We need to

## Notes
- Each wire can only get a signal from one source
  - We only need to track the last 'input' to a wire, overwriting if there are repeats
- Each wire can provide its signal to multiple destinations
  - We need to track all the destinations the wire connects to


So in summary, iterate through the commands. For each string, record the singular source and the list of destinations.

Need a method to set the value of a line