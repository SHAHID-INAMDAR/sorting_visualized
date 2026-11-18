# Sorting Visualized

A simple Python program that visualizes how different sorting algorithms work, using `matplotlib`. Each point is plotted as (index, value), so you can watch a shuffled, scattered cloud of points turn into a clean diagonal line as the array gets sorted.

## Algorithms

| Algorithm      | Best       | Average    | Worst      |
|----------------|------------|------------|------------|
| Insertion Sort | O(n)       | O(n²)      | O(n²)      |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      |

## Requirements

- Python 3.8+
- matplotlib
- 
## Usage

```bash
python insertion_sort.py
python selection_sort.py
python quick_sort.py
```

A window opens and the sort is animated step by step.

## Configuration

Change `SIZE` at the top of each file to sort more or fewer points. Larger values look smoother but animate more slowly.

## How it works

1. A list of values `0..SIZE-1` is shuffled randomly.
2. Each point is plotted at (index, value).
3. After each step of the algorithm, the plot is cleared and redrawn with `plt.pause()`.
4. When the points form a straight diagonal line, the array is sorted.
