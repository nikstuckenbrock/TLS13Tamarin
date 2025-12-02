# [C.1. Random Number Generation and Seeding](https://datatracker.ietf.org/doc/html/rfc8446#appendix-C.1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
TLS requires a cryptographically secure pseudorandom number generator
(CSPRNG).  In most cases, the operating system provides an
appropriate facility such as /dev/urandom, which should be used
absent other (e.g., performance) concerns.  It is RECOMMENDED to use
an existing CSPRNG implementation in preference to crafting a new
one.  Many adequate cryptographic libraries are already available
under favorable license terms.  Should those prove unsatisfactory,
[RFC4086] provides guidance on the generation of random values.

TLS uses random values (1) in public protocol fields such as the
public Random values in the ClientHello and ServerHello and (2) to
generate keying material.  With a properly functioning CSPRNG, this
does not present a security problem, as it is not feasible to
determine the CSPRNG state from its output.  However, with a broken
CSPRNG, it may be possible for an attacker to use the public output
to determine the CSPRNG internal state and thereby predict the keying
material, as documented in [CHECKOWAY].  Implementations can provide
extra security against this form of attack by using separate CSPRNGs
to generate public and private values.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
All cryptographic primitives including number generators and seeding are considered perfect in the model for now.
In future work one could model several known issues related to those functions and then analyze the impact.
///

/// html | div[style='clear: both;']
///