# C++ Forwarding References

## References

* [Forwarding References](https://en.cppreference.com/w/cpp/language/reference#Forwarding_references) (summary on cppreference.com)
* [Universal References in C++11 -- Scott Meyers](https://isocpp.org/blog/2012/11/universal-references-in-c11-scott-meyers)
  * "Universal references" was Meyers' proposed name for forwarding references before the latter entered common use.
  * [The "Nitty Gritty Details" section](https://isocpp.org/blog/2012/11/universal-references-in-c11-scott-meyers#NittyGrittyDetails) is of particular interest; it describes reference collapsing rules. In a nutshell:
    * An rvalue reference to an rvalue reference becomes an rvalue reference.
    * All other combinations of references (i.e., all those involving an lvalue reference) become an lvalue reference.
* ["Why forwarding reference does not deduce to rvalue reference in case of rvalue?"](https://stackoverflow.com/questions/16373881/why-forwarding-reference-does-not-deduce-to-rvalue-reference-in-case-of-rvalue)
  * A good question highlighting the lack of symmetry between type deduction for lvalues and rvalues.
  * [Interesting answer](https://stackoverflow.com/a/16376056) regarding design history from [Howard Hinnant](https://howardhinnant.github.io/). 
* [SonarSource: "std::move" and "std::forward" should not be confused](https://rules.sonarsource.com/cpp/RSPEC-5417/)
* [SonarSource: "Forwarding references" parameters should be used only to forward parameters](https://rules.sonarsource.com/cpp/RSPEC-5425/)
