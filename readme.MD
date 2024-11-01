# Advanced Calculator with Design Patterns and Plugin Architecture
### Overview
A sophisticated Python-based calculator application demonstrating modern software engineering principles through the implementation of design patterns and plugin architecture. This project serves as a practical example of building maintainable, extensible software using the Command Pattern and plugin-based system architecture, while incorporating comprehensive logging, history tracking, and thorough testing practices.
Project Architecture
Core Components

### REPL Interface

Interactive command-line interface for user interaction
Command parsing and validation
Real-time calculation display
Error handling and user feedback


### Plugin System

Dynamic command loading mechanism
Extensible architecture for adding new operations
Plugin registry and management
Hot-loading capabilities for new commands


### Command Pattern Implementation

Separation of command logic from execution
Encapsulation of operations
Support for operation history and undo functionality
Standardized command interface


### History Management

Calculation tracking and storage
CSV export functionality
Historical data analysis capabilities
Data persistence between sessions



### Branch Structure

The project is organized across multiple branches, each dedicated to specific functionality:

#### Master Branch

Production-ready core implementation
Integration of all stable features
Main REPL interface
Complete test suite
Documentation

#### Commands Branch
Focuses on the implementation of the Command Pattern:

Base command interface
Core arithmetic operations:

Addition implementation
Subtraction implementation
Multiplication implementation
Division implementation with error handling


Command factory implementation
Command registration system

#### Logging Branch
Dedicated to system logging and monitoring:

Operation logging framework
Error tracking system
Debug information collection
Log rotation and management
Performance monitoring

#### History Branch
Manages calculation history and data persistence:

History tracking implementation
CSV export functionality
Data storage optimization
History query interface
Backup management

### Installation and Setup

#### Prerequisites

```bash
Python 3.8 or higher
pip package manager
Git version control
```

#### Installation Steps

Clone the repository:
```bash 
git clone https://github.com/sharonekula/MidTerm
cd MidTerm
```
Install required dependencies:

```bash
pip install -r requirements.txt
```

Verify installation:
```bash
python -m pytest tests/
```

### Operations Guide

Running the App:

```bash
python main.py
```

Command Operation:

```bash
2024-11-01 05:58:37,970 - root - INFO - Logging configured.
2024-11-01 05:58:37,971 - root - INFO - Environment variables loaded.
2024-11-01 05:58:37,972 - root - INFO - Command 'add' from plugin 'add' registered.
2024-11-01 05:58:37,973 - root - INFO - Command 'divide' from plugin 'divide' registered.
2024-11-01 05:58:37,973 - root - INFO - Command 'exit' from plugin 'exit' registered.
2024-11-01 05:58:37,974 - root - INFO - Command 'multiply' from plugin 'multiply' registered.
2024-11-01 05:58:37,975 - root - INFO - Command 'subtract' from plugin 'subtract' registered.
2024-11-01 05:58:37,975 - root - INFO - Application started. REPL Calculator
Enter command to perform operation Add Subtract Multiply Divide or 'exit' to Exit
>>> add
Enter two numbers space-separated: 3 4
2024-11-01 05:58:42,491 - root - INFO - Performing addition for 3.0 and 4.0
2024-11-01 05:58:42,491 - root - INFO - Adding to history : Addition,3.0,4.0,7.0
Result of add operation between 3.0 and 4.0 is: 7.0
>>> subtract
Enter two numbers space-separated: 4 3
2024-11-01 05:58:49,930 - root - INFO - Peforming Subtaction between 4.0 and 3.0
2024-11-01 05:58:49,930 - root - INFO - Adding to history: Subtraction, 4.0, 3.0, 1.0
Result of subtract operation between 4.0 and 3.0 is: 1.0
>>> multiply
Enter two numbers space-separated: 5 4
2024-11-01 05:58:57,382 - root - INFO - Performing Multiplication between 5.0 and 4.0
2024-11-01 05:58:57,382 - root - INFO - Adding to history: Multiplication, 5.0, 4.0, 20.0
Result of multiply operation between 5.0 and 4.0 is: 20.0
>>> divide
Enter two numbers space-separated: 4 2
2024-11-01 05:59:06,823 - root - INFO - Performing Division for 4.0 and 2.0
2024-11-01 05:59:06,823 - root - INFO - Adding to history Division, 4.0, 2.0, 2.0
Result of divide operation between 4.0 and 2.0 is: 2.0
>>> exit
Do you want to save the history? Y or N :
Y
History exported to data/calculator_history.csv in the specified format.
2024-11-01 05:59:12,610 - root - INFO - Exiting the calculator After Saving to csv.
Exiting the calculator After Saving to csv.
2024-11-01 05:59:12,611 - root - INFO - System Exit Raised.
Application shutdown.
```
### History Management
#### Data Storage

Calculations are stored in CSV format with the following structure:

|   Operation     |   Operand1   |   Operand2   |   Result   |
|-----------------|---------------|---------------|------------|
|   Add           |   3.0        |   4.0        |   7.0      |
|   Subtract      |   4.0        |   3.0        |   1.0     |
|   Multiplication |   5.0       |   4.0        |   20.0     |
|   Division      |   4.0       |   2.0        |   2.0     |

When the exit command is triggered. You will be prompted with the confirmation to save the history.

Depending on the user option save will be triggered.

Each row in the CSV contains:
- **Operation**: Type of arithmetic operation (Addition, Subtraction, Multiplication, Division)
- **Operand1**: First number in the calculation
- **Operand2**: Second number in the calculation
- **Result**: Final result of the operation

