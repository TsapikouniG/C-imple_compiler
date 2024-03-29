## Overview
Cimple is a small, educational programming language designed to introduce fundamental concepts of compiler construction. Inspired by the C language, Cimple is significantly simplified in terms of supported structures and programming capabilities, making it an excellent tool for educational purposes. This project encompasses both the definition of the Cimple language and the development of a fully functional compiler that translates Cimple code into RISC-V assembly language.

## Features
- **Simplified Syntax:** Cimple's syntax is reminiscent of C but with fewer structures and functionalities to ease the learning curve.
- **Educational Focus:** The language includes essential programming constructs like `if-else`, `while`, and unique `forcase` and `incase` structures, without complex data types like real numbers, strings, or arrays.
- **Compiler Development:** The project details the step-by-step development of the Cimple compiler without using development tools, solely relying on a programming language.
- **RISC-V Assembly Output:** The compiler generates RISC-V assembly language as its output, allowing programs to be run on a RISC-V processor emulator for educational insights into assembly language and processor architecture.

## Getting Started
To compile and run Cimple programs, follow these steps:

### Prerequisites
- Ensure you have a Java development environment set up if the compiler is written in Java.
- Install a RISC-V processor emulator to run the compiled assembly code.

### Compilation Process
1. Write your Cimple program in a file with a `.ci` extension.
2. Run the Cimple compiler with your `.ci` file as the input.
3. The compiler will generate a file containing RISC-V assembly code.
4. Use the RISC-V emulator to run the generated assembly code and observe the program's behavior.

## Acknowledgments
 Thanks to Prof. Georgios Manis and the University of Ioannina for the initial concept and guidance.

Cs team:
Dafnakis Georgios 
Tsapikouni Georgia 
