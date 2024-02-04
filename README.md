# 2-Phase Compiler

## Description
This project implements a 2-phase compiler featuring lexical, syntax, and semantic analyzers to scan, parse, and validate input commands. It utilizes a set of Context-Free Grammar (CFG) rules to ensure input conformity to the intended grammar structure. The compiler produces parse and syntax trees for supported statements.

## Flowchart
- **Lexical Analysis**
   - User inputs code
   - Code undergoes tokenization and classification
   - Token types include operators, reserved words, punctuators, identifiers, and constants
   - Number of lines in the code is determined

- **Context-Free Grammar**
   - CFG rules are constructed and specified within the code
   - CFG is printed for reference

- **Syntax Analyzer**
   - Validates input code against the specified grammar
   - If valid, compiles code into a parse tree
   - Parse tree is processed to generate output expressions for semantic analysis
   - White spaces are removed, and expressions are organized into lists for further processing

- **Semantic Analyzer**
   - Converts infix expressions from parse tree to postfix expressions to construct a syntax tree
   - Builds an expression tree and traverses it to produce output expressions

## Files
- **`compiler.py`**
   - Contains the main code implementing lexical, syntax, and semantic analysis
   - Utilizes NLTK for CFG and parse tree generation

- **`input.py`**
   - Sample input file containing code snippets for analysis

## Usage
1. Ensure Python and NLTK are installed
2. Run `compiler.py` and provide input code in `input.py`
3. Follow on-screen instructions for analysis and output

## Libraries Used
- NLTK (Natural Language Toolkit)
- Regular Expressions (re)

## Note
This is a basic implementation and may require enhancements for more complex scenarios. Please feel free to contribute improvements or report issues.
