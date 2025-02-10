import plotly.express as px

from die import Die


# Create a D6.
die = Die()

# Make some rolls and store the results in a list.
results = []
for roll_num in range(1000):
    results.append(die.roll())

# Analyze the results.
frequencies = []
possible_results = range(1, die.num_sides + 1)
for value in possible_results:
    frequencies.append(results.count(value))

# Visualize the results.
title = "Results of Rolling a D6 1000 Times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()
