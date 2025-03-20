# TypeScript Algorithm Notebook

A personal collection of algorithm implementations and solutions to programming challenges using TypeScript.

## Overview

This repository serves as a knowledge base and practice ground for algorithms and data structures using TypeScript. It includes solutions to various LeetCode problems, implementation of common algorithms, and custom data structure solutions.

## Features

- TypeScript implementations of common algorithms and data structures
- Solutions to LeetCode problems with explanations
- Test cases for validating algorithm correctness
- Organized file structure for easy navigation

## Key Contents

### Data Structures (`src/adt`)
This directory contains implementations of many classic data structures in TypeScript, including:
- Linked Lists
- Trees (Binary Trees, BST, AVL, etc.)
- Graphs
- Heaps
- Stacks and Queues
- Hash Tables
- And more advanced data structures

### LeetCode Solutions (`src/leetcode`)
An organized collection of 200+ classic LeetCode problems categorized by topics. Each problem includes:
- Multiple solution approaches (from simple to complex)
- Time and space complexity analysis
- Detailed explanations and thought processes
- Edge case handling

The problems are carefully selected to cover fundamental algorithm patterns and techniques.

### Frontend Coding Challenges (`src/front-end`)
A compilation of frontend-related coding challenges and implementations, including:
- Promise Implementation
- Throttle & Debounce
- Curring
- Event Loop Principal

## Project Structure

```
.
├── src/                  # Source code for algorithms and data structures
│   ├── adt/              # Abstract Data Types implementations
│   ├── leetcode/         # 200+ LeetCode problems by topic
│   └── front-end/        # Frontend-related coding challenges
├── tests/                # Test cases for validating implementations
├── scripts/              # Utility scripts for the project
├── assets/               # Supporting assets and diagrams
├── *.(ts|js)             # Individual algorithm solutions
```

## Setup

### Prerequisites

- Node.js (v14 or higher)
- pnpm (recommended) or npm

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ts-algo-prac.git
   cd ts-algo-prac
   ```

2. Install dependencies:
   ```bash
   pnpm install
   # or
   npm install
   ```

## Usage

### Running a specific algorithm:

```bash
pnpm ts-node path/to/algorithm-file.ts
# or
npm run ts-node path/to/algorithm-file.ts
```

### Running tests:

```bash
pnpm test
# or
npm test
```

## Contributing

Feel free to use this repository as inspiration for your own algorithm practice. If you have suggestions for improvements, please open an issue or submit a pull request.

## License

[MIT](LICENSE) 