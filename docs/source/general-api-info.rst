General Concepts
================

Utilities is a static library collecting low-level functionality that is widely
available and may be hard-linked against.

Core is a tiny shared library that declares interfaces of common class
patterns throughout all SCINE software and contains functionality that manages
the runtime loading of shared libraries and instantiation of provided
implementations of these interfaces. These shared libraries that follow the
conventions set out here for runtime loading are called a Module, for the
following reasons:

- It implements a class derived from Core's `Module` class that can be
  imported at runtime providing functionality extensions to consumers.
- It reflects a CMake `MODULE <https://cmake.org/cmake/help/v3.9/command/add_library.html#normal-libraries>`_ 
  library which is not linked against, but loaded at runtime


Component is a collection of topic-specific functionality. Most of this is
contained in a Module target, that may define a class derived from
the Module interface declared in Core for runtime loading. The component may
contain its own GUI Module, Tests and (possibly) a command line interface (
CLI). This group is called a component because it shall represent a CMake level
`COMPONENT` of the entire SCINE software.

As a component developer, you may link against the Utilities library. 
Depending on whether types define in the Utilities form part of your API, your link should be 
`PUBLIC` or `PRIVATE` at CMake level.


C++ Code Conventions
--------------------

Collectively, we have decided upon the following C++ coding conventions for all
SCINE projects:

=============================== ============================================================================================================
Topic                            Conventions
=============================== ============================================================================================================
File extensions                  .cpp, .h (.hxx for inline class implementation)
Indentation                      With 2 spaces
Namespace indentation            None
Variable naming                  CamelCase with first capital lowered: `myVariable`
Class naming                     CamelCase: `MyClass`
Function naming                  CamelCase with first capital lowered: `myFunction`
Member variable naming           Distinguish it from normal variables, for instance with a trailing underscore or some prefix: `myVariable_`
Braces in function definitions   Opening brace on the same line as the function: `void f() {`
Pointer/Reference type names     Append directly to the type and then have a single space: `MyType& myVariable`, `MyType* myVariable`
Documentation                    Doxygen
Source line length               Maximum of 120 characters
Private implementation pattern   `Impl` is a nested class, `unique_ptr<Impl> pImpl_` member.
=============================== ============================================================================================================

CMake Structure Standards
-------------------------
In a final installation of multiple parts of SCINE, which would minimally
comprise Core and Utilities, all parts of the program have to come together.

To this end, we standardize the following:

- All Scine repositories use the same minimal CMake version to avoid policy
  conflicts. To this end, we have settled on 3.9 on the basis of widespread unix
  distribution adoption.
- CMake target names are CamelCase
- All CMake targets that will be used externally  must receive an alias target
  into the `Scine` namespace
- Each Git repository represents at least one SCINE `COMPONENT` in CMake. Each
  `COMPONENT` must define an identically named target that is properly
  namespaced. This implies that `COMPONENT` names are also CamelCase. E.g. The
  core git repository provides the Core `COMPONENT` and contains a
  `Scine::Core` CMake target. The installed directory structure is:
 
  - `<prefix>/lib/cmake/Scine/Core/CoreConfig.cmake` defines dependencies via
    `find_dependency` calls and includes the generated targets file
  - `<prefix>/lib/cmake/Scine/Core/CoreTargets.cmake` defines the targets
    contained in this `COMPONENT`.
  - `<prefix>/lib/cmake/Scine/ScineConfig.cmake` receives the
    `find_package(Scine COMPONENTS Core)` call and includes
    `Core/CoreConfig.cmake` appropriately.

- Static libraries, if present, shall receive a `Static` CMake target name
  suffix. Shared libraries do not receive a suffix.
- Library disk filenames are all-lowercase.
- Headers are installed at `<prefix>/include/Scine/COMPONENT/Header.h`
  The relative include directory is set at `<prefix>/include/Scine` so that in
  code, it suffices to specify `#include "Core/ModuleManager.h"`.
- Since Utilities are split into open and closed source, naming should reflect
  Utilities before license type in all cases where both information is required.
- Configure-time CMake messages should be limited to the most important
  information (missing dependencies, what is being used from where, what
  version and what is being downloaded instead)
- All `cmake/` Modules regarding dependency inclusion are standardized and are
  to be included in-tree via a git submodule for universality across projects
- Several CMake variables names are reserved for communication between SCINE
  CMake subtrees:

  - SCINE_BUILD_TESTS indicates whether a tree's tests should be built
  - SCINE_BUILD_PYTHON_BINDINGS indicates whether a tree's python bindings (if
    present) should be built
  - ...

The following files should closely follow templated forms:

- The topmost CMakeLists.txt is standardized save for very few customization points
- Installation / `COMPONENT`-level handling is abstracted into functions as good
  as possible
- Avoid multiple project calls. 
- Do not use `${PROJECT_NAME}` or other variables for target names.

The following behavior is intended for consumers:

- Any SCINE software git repository can be cloned and built without having any
  of its SCINE-internal dependencies installed, or with all dependencies preinstalled. 
  By default, the dependencies are sought in the PATH, and
  downloaded if they are not found.
- At configure time, third-party library dependencies are resolved and missing dependencies 
  communicated transparently to the consumer.
- At build time, all targets defined in each CMake sub-tree are built.
- At install time, all install steps are carried out for each CMake sub-tree.



Repository Structure
--------------------

Each repository must follow the following structure:

.. code::

   - src/
     - <COMPONENT-name>/
       - <COMPONENT-name>/
         - Header.h
         - Impl.cpp
       - Tests/
       - GUI/
       - ...

This is to enable repositories to be split and merged more easily should
structural circumstances change.


Utilities
---------

The Utilities contain contain a lot of code that is shared and used by all
other parts of the code. The code present in the Utilities includes the
definition of many important interfaces. In order to unify the usage of some of
them, please consider the following:

**Settings**

The `Settings` class defined in the Utilities wraps the `UniversalSettings`
constructs in a single class that is supposed to be easier to use that a handful
of classes used within a set of `Settings`. The `UniversalSettings`, in
principle, allow for the infinite nesting of collections of settings into one
another. Because deep nesting of the actual settings complicates its use and
also it makes the code based understanding of any settings harder than it has
to be, it is imperative that nesting is kept to a minimum. 

Python Bindings
---------------

If an individual component of Scine chooses to offer Python bindings, the
following rules apply:

- Do not bind classes defined in other components. This is to avoid multiple
  definition issues when loading both components' Python bindings.
- If you have a class that is derived from a class from another component, you
  may bind it. Note that this creates a hard dependency on the other module's
  bindings and requires that this other python module is imported first in
  consuming python programs.
- Python `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ applies
  for naming conventions. In short:

  - Classes are CamelCase
  - Functions are lowercase_underscore
  - Modules are short lowercase, and should have underscores only if really
    necessary
  - Constants are UPPERCASE_UNDERSCORE
