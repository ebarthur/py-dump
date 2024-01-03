# Characteristics of Python programming language
'''Python is a high-level, interpreted, and dynamically typed programming 
language known for its readability and simplicity. It features a large standard 
library, supports object-oriented programming, and has a vibrant community. 
Python is versatile, used across various domains, and is platform-independent. 
Its clean syntax, automatic memory management, and emphasis on code 
readability make it an ideal choice for a wide range of applications, 
from scripting to web development, data science, and machine learning.'''


# Dynamic vs Static Programming Languages
''''Dynamic and static programming languages differ in how they handle variables and types during program execution.

**Dynamic Programming Languages:**
1. **Type Checking:** Determined at runtime, allowing flexibility in changing variable types.
2. **Memory Allocation:** Dynamic, with structures able to change size during execution.
3. **Flexibility:** More flexible and concise, making them easier to write and read.
4. **Late Binding:** Variable bindings and method calls are resolved at runtime.
5. **Examples:** Python, JavaScript, Ruby, PHP.

**Static Programming Languages:**
1. **Type Checking:** Occurs at compile-time, with explicit type declarations.
2. **Memory Allocation:** Static, with fixed memory allocation determined at compile-time.
3. **Safety and Performance:** Offers better safety due to early error detection and potential performance optimizations.
4. **Early Binding:** Variable bindings and method calls are resolved at compile-time.
5. **Examples:** Java, C, C++, C#, Swift.

**Choosing Between Dynamic and Static Languages:**
- **Project Complexity:** Dynamic for rapid development and smaller projects; static for larger, complex projects with early error detection needs.
- **Performance:** Static languages often provide better performance due to compiler optimizations.
- **Type Safety:** Static languages offer better type safety.
- **Readability:** Dynamic languages are often more concise and readable.

Ultimately, the choice depends on project requirements and the desired balance between flexibility, safety, and performance.'''


# Interpreted vs Compiled languages
'''Interpreted languages execute code line by line at runtime using an interpreter, allowing for platform independence and a faster development cycle. Examples include Python and JavaScript.

Compiled languages translate code into machine or intermediate code before execution, resulting in platform-specific binaries. They often offer better performance but have a longer development cycle. Examples include C, C++, and Java (when compiled to bytecode).

The choice between interpreted and compiled languages depends on factors such as performance, portability, development speed, and debugging preferences. Some languages, like Java, combine both approaches for a balance of performance and portability.'''


# High level vs Low level languages
'''High-level languages offer greater abstraction, readability, and portability,
making them suitable for general-purpose programming. Examples include Python
and Java. Low-level languages provide less abstraction, require deeper
understanding of hardware, and may offer better control over system resources.
Examples include Assembly and machine code. The choice depends on project requirements,
with high-level languages favored for general development and low-level languages for
tasks requiring fine-grained control over hardware.'''


firstName = 'Kwame'
firstName = 'Ama'
firstName = 123 #Python is dynamic. It allows overwriting.
print(type(firstName))