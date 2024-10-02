# PageRank Recommendation System

This repository implements a block-based PageRank algorithm for efficient large-scale computation using sparse matrices. The project is designed to handle very large datasets by splitting the matrix and vector operations into manageable blocks.

## Project Structure

- `readWriteBlock.py`: Utility functions for loading and saving matrix and vector blocks using pickle.
- `pageranker1.py`: Implements the PageRank algorithm, including handling leaks and iterating to calculate PageRank values.
- `sparse_matrix.py`: Defines the sparse matrix and vector structures used in the PageRank computation.
- `main.py`: The main entry point to run the PageRank process. It initializes the matrix, iterates through the blocks, and computes the final PageRank values.
- `initBlock.py`: Initializes the matrix and vector blocks from input data, preparing for PageRank calculations.

## How to Use

1. **Initialize Blocks**:
   - The first step is to initialize the matrix and vector blocks using `initBlock.py`. This script reads the input data, creates matrix blocks, and sets up the vectors.
   - You can modify the `init_block()` function to adjust how the blocks are initialized.

2. **Run PageRank**:
   - Execute `main.py` to start the PageRank calculation. The script iterates through the matrix blocks and updates the PageRank vector in each step.
   - The results are stored as blocks, which can be accessed through the utility functions in `readWriteBlock.py`.

3. **Handling Leaks**:
   - The PageRank algorithm includes a mechanism for handling leaks in the rank calculation using the `leak_pagerank()` function in `pageranker1.py`.

## Dependencies

- Python 3.x
- Libraries: `pickle`, `math`

## Future Improvements

- Add more efficient handling of very large datasets by optimizing block read/write operations.
- Implement distributed computation to further speed up the PageRank iterations.
