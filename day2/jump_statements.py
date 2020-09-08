# break and continue allow to control the flow of the loops

# using break, we can go outside the loop
names = ["Scaler", "Interviewbit", "scaler", "interviewbit"]
for name in names:
  print(name)
  if (name == "Scaler"):
    break

# using continue, we can skip a particular iteration, and go to next one
for name in names:
  if (name == "Scaler"):
    continue
  print(name)

# using break in nested loops
# break in the inner loop just breaks out of the inner loop
# outer loop will continue to run
target = 'i'
for name in names:
  print(f"{name} in outer loop")
  for char in name:
    if char == target:
      print(f"Found {name} with letter: {target}")
      print("Breaking out of the inner loop")
      break