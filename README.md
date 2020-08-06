# banking_app_refactor
A refactoring of a python banking app script i saw on a programming instagram page. Note will probably be incomplete since the snippets of code weren't complete either.

A lot of the changes have come from clean code practices i've read and best practices stated online, and https://connascence.io (to learn more about Connascence and uncoupling complex code)

## Connasce... what now?

Connascence. it's a software quality metric invented by Meilir Page-Jones to allow reasoning about the complexity caused by dependency relationships in object oriented design much like coupling did for structured design...

Well basically, it's just a way of checking how tightly bound and dependent one piece of code is over another. Think of it like a chain of dependencies where a change in one part of the code means you need to change a lot of other different places. The trick to making more flexible software is to ensure that these dependencies are more loose and affect less in your codebase.

Part of the reason for this refactoring exercise was to learn where these "connascences" can occur through normal programming, and see how to minimize them without having to go overboard and try to overperfect the code. 
And let's face it, refactoring code is fun😉
