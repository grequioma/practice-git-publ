# Exercise 16 Study Drill

filename = "textSample_16sd.txt"

from sys import argv

script, first, second, third, filename = argv
prompt = '> '

txt = open(filename)

target = open(filename, 'w')

print(f"Hi I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Your first variable {first}:")
first = input(prompt)

print(f"Your first variable {second}:")
second = input(prompt)

print(f"Your third variable {third}:")
third = input(prompt)

print(f"Name of script: {script}")
print(f"First variable: {first}")
print(f"Second variable: {second}")
print(f"Third variable: {third}")

print("I'm going to write these to the file.")

target.write(first)
target.write("\n")
target.write(second)
target.write("\n")
target.write(third)
target.write("\n")

print("And finally, we close it.")
target.close()

print(f"Here's your file {filename}:")
print(txt.read())
