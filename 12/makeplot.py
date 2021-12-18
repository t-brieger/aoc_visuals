#!/usr/bin/env python3
# 
# Make an image of the directed graph provided in Advent of Code 2021, Day 12.
# Inspired by basic graphviz documentation, including:
#   - https://graphviz.readthedocs.io/en/stable/
#   - https://pypi.org/project/graphviz/
#   - https://stackoverflow.com/questions/10379448/plotting-directed-graphs-in-python-in-a-way-that-show-all-edges-separately
#

import graphviz

rec = open("input.txt", "r");
lineStr = rec.read().split("\n")
size=len(lineStr)-1

diGraph = graphviz.Digraph()

labels = {}
nextLetter = "A"

for lineIndex in range(0, size):
  thisLine = lineStr[lineIndex]
  pairArr = thisLine.split("-")
  if (not pairArr[0] in labels.keys()):
    diGraph.node(nextLetter, pairArr[0])
    labels[pairArr[0]] = nextLetter
    nextLetter = str(chr(ord(nextLetter) + 1))
    print(f"New nextLetter will be {nextLetter}")
  if (not pairArr[1] in labels.keys()):
    diGraph.node(nextLetter, pairArr[1])
    labels[pairArr[1]] = nextLetter
    nextLetter = str(chr(ord(nextLetter) + 1))
    print(f"New nextLetter will be {nextLetter}")
  print(f"Now about to concatenate {labels[pairArr[0]]} with {labels[pairArr[1]]} to get {labels[pairArr[0]] + labels[pairArr[1]]}")
  if (pairArr[1] != "start" and pairArr[0] != "end"):
    diGraph.edges([labels[pairArr[0]] + labels[pairArr[1]]])
  if (pairArr[1] != "end" and pairArr[0] != "start"):
    diGraph.edges([labels[pairArr[1]] + labels[pairArr[0]]])

print(diGraph.source)
diGraph.render(view=True)

