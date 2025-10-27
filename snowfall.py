import streamlit as st
import sys
import matplotlib.pyplot as plt
from pathlib import Path

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %% [markdown] cell_id="277df626b5ab4ea6b5b5515f18bba2c2" deepnote_cell_type="markdown"
#
# # Intro to Python in Notebooks
# MIT Beaver Works Classroom Edition
#

# %% [markdown] cell_id="67772d067a2a4976927e522c27fcc932" deepnote_cell_type="markdown"
#
# ## Objectives
#
# 1. Understand how notebook documents work and how to use code and text cells effectively.
# 2. Learn Python fundamentals: variables, data types, arithmetic, strings, lists, loops, conditionals, and functions.
# 3. Build a small but real project in the same notebook and export artifacts.
# 4. Practice clear communication of results using Markdown and visualizations.
#

# %% [markdown] cell_id="36f15bac43bf466982910685afe810c5" deepnote_cell_type="markdown"
#
# ## What is a Notebook
#
# A notebook is an interactive scientific document that combines code, text, and outputs in one place. It supports incremental exploration. You can run code cells in any order, document your reasoning in Markdown cells, and preserve results for review.
#

# %% [markdown] cell_id="8791b2e317834f4b98f1e660875df549" deepnote_cell_type="markdown"
#
# ## Using Cells
#
# 1. Create a new cell and choose Code or Markdown from the toolbar.
# 2. Write code in a Code cell and execute it.
# 3. Write explanations, section headers, and instructions in Markdown cells.
# 4. Rerun cells at any time to reproduce results.
#

# %% cell_id="b45a2f8388eb430cbf1381f9d49f155e" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=0 execution_start=1760809668300 source_hash="5d9c11d6"

st.write("Hello from a notebook")


# %% [markdown] cell_id="b6a55d9fb5e04a6aacff15f6bd7e648f" deepnote_cell_type="markdown"
#
# ## Markdown Basics
#
# 1. Use `#` for a top level header and `##` for a section header.
# 2. Use backticks for inline code.
# 3. Use triple backticks to create code blocks in Markdown when you want to show snippets without running them.
# 4. Use numbered lists for step by step instructions.
#

# %% [markdown] cell_id="a89e14a22b704160b8fbbcd2a6efbe45" deepnote_cell_type="markdown"
#
# ## Python Fundamentals
#
# This section introduces the core language features used in scientific and engineering workflows.
#

# %% [markdown] cell_id="258486c4c88340c7a17e49bd40a6069b" deepnote_cell_type="markdown"
#
# ### Variables and Types
#
# Python variables are created by assignment. The type is inferred at runtime.
#

# %% cell_id="73995274c44b4ea696c4551cc79c7764" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668366 source_hash="792cb30e"

name = "Beaver Works Student"
age = 16
height_m = 1.68
enrolled = True

st.subheader("Student Info")
st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Height (m):** {height_m}")
st.write(f"**Enrolled:** {enrolled}")

# %% [markdown] cell_id="51f313e404ea46e58a4aa7ec76b91a13" deepnote_cell_type="markdown"
#
# ### Arithmetic and Expressions
#
# Arithmetic works on numbers and variables. Parentheses control order of operations.
#

# %% cell_id="b5bd9e9a3e374f3b92100c228e5fc0ad" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668417 source_hash="7bf8f884"

a, b = 12, 5
st.subheader("Basic Arithmetic")
st.write({
    "Sum": a + b,
    "Difference": a - b,
    "Product": a * b,
    "Quotient": a / b,
    "Power": a ** 2
})


# %% [markdown] cell_id="c6c37adcb033419a9125242413a4d7b0" deepnote_cell_type="markdown"
#
# ### Strings
#
# Strings represent text data. Use concatenation and formatted strings for clean output.
#

# %% cell_id="8c35b28af17b45e88937845311ac2fc0" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668476 source_hash="8230b618"

st.subheader("Strings and Formatting")
combined = "Beaver" + " " + "Works"
st.write(combined)
st.write(f"Brianna scored {93}")


# %% [markdown] cell_id="23442339f34a44eab719dbcea474b4a8" deepnote_cell_type="markdown"
#
# ### Exercise A
#
# 1. Create variables describing yourself: a string for your name, an integer for a favorite number, and a float for any measurement you choose.
# 2. Print a single formatted sentence that combines them.
# 3. Compute a new value that uses arithmetic on your numeric variables and print it.
#

# %% cell_id="9fa6c42febee411daa62f65bcfba1a51" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668526 source_hash="242d6e55"

# Your work for Exercise A below. Replace the placeholders and run the cell.

st.subheader("Personal Variables")
your_name = "Nissi Sanju"
favorite_number = 7
ratio = 0.957
st.write(f"My name is {your_name}. My favorite number is {favorite_number}. The ratio I chose is {ratio}.")
st.write("Computation:", favorite_number * ratio)


# %% [markdown] cell_id="378e575ba44749cb9bc3eb6901a311e2" deepnote_cell_type="markdown"
#
# ### Lists and Indexing
#
# A list stores an ordered collection of items.
#

# %% cell_id="a11c948b88c6487ba3344a0ca0184d06" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=0 execution_start=1760809668576 source_hash="62e0f0d9"

st.subheader("Working with Lists")
students = ["Brianna", "Logan", "Grace"]
students.extend(["Martha", "5th", "6th"])
st.write("Students:", students)
st.write("Total students:", len(students))
for s in students:
    st.write(f"Welcome {s}")


# %% [markdown] cell_id="1a8643b663e74cde853a24dbdab4833a" deepnote_cell_type="markdown"
#
# ### Loops
#
# Loops repeat actions over a sequence.
#

# %% cell_id="f9f3520dc8c446099ca539fb88105540" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668626 source_hash="c6f3d4d9"


# %% [markdown] cell_id="3242c85b11ee4995b92f439ccea36fc5" deepnote_cell_type="markdown"
#
# ### Conditionals
#
# Conditionals choose between paths of execution.
#

# %% cell_id="3d3dffaa37004460b90c4885fa4deec5" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668676 source_hash="aa4e3ca7"

st.subheader("Conditionals and Functions")
score = 95
if score >= 90:
    st.write("Grade A")
elif score >= 80:
    st.write("Grade B")
else:
    st.write("Keep improving!")

def letter_grade(g):
    if g >= 90:
        return "A"
    elif g >= 80:
        return "B"
    elif g >= 70:
        return "C"
    else:
        return "D/F"

st.write(f"Letter grade for 80: {letter_grade(80)}")

def square(x):
    return x * x

nums = list(range(1, 11))
even_squares = [square(n) for n in nums if n % 2 == 0]
st.write("Even squares:", even_squares)


# %% [markdown] cell_id="29223ca70dfb47a99eba5b0648ddc9c9" deepnote_cell_type="markdown"
#
# ### Functions
#
# A function packages reusable logic and can return a value.
#

# %% cell_id="c18dc848e3084d4b8002a30454cd79cd" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=2 execution_start=1760809668736 source_hash="1bead792"


# %% [markdown] cell_id="7e51fb5d18dc46308abf481c9db173d8" deepnote_cell_type="markdown"
#
# ### Exercise B
#
# 1. Write a function `square(x)` that returns the square of a number.
# 2. Create a list of integers from 1 to 10 and build a new list that contains the squares of the even numbers only.
# 3. Print the final list.
#

# %% cell_id="19347e9f678040b9831826a004ea6c31" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=0 execution_start=1760809668799 source_hash="87365bf3"

# Your work for Exercise B below.



# %% [markdown] cell_id="2b7f37b891854df2ae0dc71b3f4f0e6e" deepnote_cell_type="markdown"
#
# ## Simple Descriptive Statistics
#
# We will compute descriptive statistics on a small numeric list to prepare for visualization.
#

# %% cell_id="4363604e867b4dde884059c151223684" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809668866 source_hash="53e8f55c"

st.subheader("Data Analysis Example")
values = [88, 92, 76, 95, 83, 90, 78, 85]
avg, hi, lo = sum(values) / len(values), max(values), min(values)

st.write(f"Average: {avg:.2f}")
st.write(f"Highest: {hi}")
st.write(f"Lowest: {lo}")


# %% [markdown] cell_id="b03ab0cff7784bc9a8250ef6404ac769" deepnote_cell_type="markdown"
#
# ## Visualization with Matplotlib
#
# Each chart appears after running a code cell. Use one figure per chart.
#

# %% cell_id="c6bd0e00586940dc88a2ac48d0da13c8" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=725 execution_start=1760809668916 source_hash="3527059"


fig, ax = plt.subplots()
ax.plot(values, marker='o')
ax.set_title("Example Line Plot")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.grid(True)
st.pyplot(fig)

# %% cell_id="a1e6f3ebe2384aeaa23e2aab5288db21" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=35 execution_start=1760809669704 source_hash="bda0f6e4"

# Bar chart example
categories = ["A", "B", "C", "D"]
measurements = [4, 7, 1, 6]
fig, ax = plt.subplots()
ax.bar(categories, measurements)
ax.set_title("Example Bar Chart")
ax.set_xlabel("Category")
ax.set_ylabel("Measurement")
st.pyplot(fig)



# %% [markdown] cell_id="ca3df6f84a454588b0c4691aa2b9745d" deepnote_cell_type="markdown"
#
# # Final Project: Weekly Mood Tracker Dashboard
#
# Goal
#
# 1. Record a numeric mood score for each day of a week on a scale from 1 to 10.
# 2. Compute summary statistics.
# 3. Render a line chart that shows the pattern across the week.
# 4. Save the chart image to disk and present a short written interpretation.
# 5. Package the project by organizing a final section and exporting your notebook.
#

# %% [markdown] cell_id="6b606a13064e446c8673f3da3d587644" deepnote_cell_type="markdown"
#
# ## Step 1 Collect Data
#
# Create two lists: one for the day names and one for the mood scores. You can enter your own data or start with the template.
#

# %% cell_id="c4f7d435de414194bb2b7510d8dfa2b9" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=0 execution_start=1760809669787 source_hash="46b0c7c"

st.subheader("Snowfall Data Analysis")
months = ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
inches = [2.9, 5.3, 6.7, 1.4, 0.0, 0.0]


# %% [markdown] cell_id="fcf028c33b254128815e3a2046eb31de" deepnote_cell_type="markdown"
#
# ## Step 2 Validate and Summarize
#
# Ensure the lists have the same length and the values are within the expected range.
#

# %% cell_id="e3b83232772d4714a6979697c8601bb7" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809669846 source_hash="3bd64106"
# Quick check
st.write("Month:", months)
st.write("Inches of snow:", inches)
st.write("Number of month:", len(months))
st.write("Total inches of snow:", sum(inches))

# Simple summary
average = sum(inches) / len(inches)
highest, lowest = max(inches), min(inches)
month_high, month_low = months[inches.index(highest)], months[inches.index(lowest)]

st.write(f"Average snowfall: {average:.2f} inches")
st.write(f"Most snowfall: {highest} inches in {month_high}")
st.write(f"Least snowfall: {lowest} inches in {month_low}")

# %% [markdown] cell_id="aaebfb4cc750494a936c4a0c98d985ac" deepnote_cell_type="markdown"
#
# ## Step 3 Plot the Weekly Pattern
#
# Create a line chart for mood across the week. Use a single figure for this chart.
#

# %% cell_id="3d1df159683f4f1594daed87f2d4f238" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=58 execution_start=1760809669902 source_hash="be43aff5"

fig, ax = plt.subplots()
ax.plot(months, inches, marker='o')
ax.set_title("Monthly Snowfall in Chicago")
ax.set_xlabel("Month")
ax.set_ylabel("Inches of Snow")
ax.grid(True)
st.pyplot(fig)


# %% [markdown] cell_id="b8cd192f443b4d3483ddc9beac54a195" deepnote_cell_type="markdown"
#
# ## Step 4 Save the Figure
#
# Save the figure to a file so you can reference it in reports or README files.
#

# %% cell_id="e8f28e385a9c4ab7b0eb448a1417eaa7" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=534 execution_start=1760809670008 source_hash="aae2c0a9"

out_dir = Path("outputs")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "monthly_snowfall.png"
fig.savefig(out_path, dpi=200)
st.success(f"Saved figure to {out_path.resolve()}")

st.subheader("Chicago vs Alaska Snowfall Comparison")
chicago_inches = [2.9, 5.3, 6.7, 1.4, 0.0, 0.0]
alaska_inches = [39.3, 30.9, 22.2, 15.2, 10.4, 10.4]

fig, ax = plt.subplots()
ax.plot(months, chicago_inches, marker='o', label="Chicago")
ax.plot(months, alaska_inches, marker='s', label="Alaska")
ax.set_title("Snowfall: Chicago vs Alaska")
ax.set_xlabel("Months")
ax.set_ylabel("Snowfall (inches)")
ax.legend()
ax.grid(True)
st.pyplot(fig)


# %% [markdown] cell_id="ff75bd8fdf2a49a2ad2d0a10e1d76d37" deepnote_cell_type="markdown"
# ## Step 5 Optional Extension
#
# Choose one:
# 1. Add a second week or a friend's mood list and plot it on the same chart with a legend.
# 2. Mark the best day on the chart with a text label.
#

# %% cell_id="08ae5cd8a54d49aead47309c41a0d1c1" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=169 execution_start=1760809670609 source_hash="8aec6120"
# Option 1: Second series on the same chart
months = ["Nov","Dec","Jan", "Feb", "Mar", "Apr"]
chicago_inches = [2.9, 5.3, 6.7, 1.4, 0.0, 0.0]
alaska_inches = [39.3, 30.9, 22.2, 15.2, 10.4, 10.4]  # example values; change if you like


highest_value = max(chicago_inches)
best_month = months[chicago_inches.index(highest_value)]

fig, ax = plt.subplots()
ax.plot(months, chicago_inches, marker='o')
ax.set_title("Highest Snowfall Highlighted")
ax.set_xlabel("Months")
ax.set_ylabel("Snowfall (inches)")
ax.grid(True)
idx = chicago_inches.index(highest_value)
ax.text(idx, highest_value + 0.2, f"Best: {best_month} ({highest_value})", ha='center')
st.pyplot(fig)

# %% [markdown] cell_id="daaad6c18b3c480c85da043096f9b600" deepnote_cell_type="markdown"
#
# ## Step 6 Communicate Findings
#
# Write a short narrative that explains the pattern you see and a plausible reason. Keep it concise and evidence based.
#

# %% [markdown] cell_id="f6378fc43e2146a7979549508dfbbe32" deepnote_cell_type="markdown"
#
# ### Example Interpretation
#
# The average snowfall in inches for Chicago was 2.72. The highest snowfall occurred on January with 6.7 inches. The lowest snowfall occurred on March and April with 0.0 inches. The pattern shows a peak in snowfall in winter months and minimal snowfall in spring months. The overall pattern suggests that snowfall is correlated with what month it is.
#

# %% [markdown] cell_id="492d53ea82024d4aa73914c571f0d1c7" deepnote_cell_type="markdown"
#
# ## Export and Share
#
# 1. Save the notebook after completing the project.
# 2. Download the notebook file for submission or version control.
# 3. Optionally include the generated image from the outputs directory.
# 4. Share a link if using Deepnote or push the notebook to a public repository.
#

# %% [markdown] cell_id="9942c64dda51469cb1da836cfe23fa0d" deepnote_cell_type="markdown"
#
# ## Resume Language Example
#
# Created an interactive Python notebook project that computes descriptive statistics and visualizes a weekly time series. Used core Python constructs and Matplotlib to present results and exported reproducible artifacts.
#

# %% [markdown] cell_id="923d2746901c4b6191e79c02be423ec6" deepnote_cell_type="markdown"
#
# ## Environment Check
#
# This cell confirms library versions used in the notebook for reproducibility.
#

# %% cell_id="6d15b7fbe3fd429c90d7a9d396b15fbd" deepnote_cell_type="code" execution_context_id="ebd34259-3033-452c-8908-077af554ab9a" execution_millis=1 execution_start=1760809670866 source_hash="fa4021f1"




# %% [markdown] created_in_deepnote_cell=true deepnote_cell_type="markdown"
# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=d93e6d1f-2c58-4d45-b6a7-58bb555c85af' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
