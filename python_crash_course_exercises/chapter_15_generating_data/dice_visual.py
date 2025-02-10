import plotly.express as px

from die import Die


# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result + 1)
for value in possible_results:
    frequencies.append(results.count(value))

# Visualize the results.
title = "Results of Rolling two D6 1000 Times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# Use the line bellow to save the figure.
# fig.write_html('dice_visual.html')

fig.show()
