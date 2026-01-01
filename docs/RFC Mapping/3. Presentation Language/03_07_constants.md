# [3.7. Constants](https://datatracker.ietf.org/doc/html/rfc8446#section-3.7)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
Fields and variables may be assigned a fixed value using "=", as in:

    struct {
        T1 f1 = 8;  /* T.f1 must always be 8 */
        T2 f2;
    } T;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
Constants are modelled through integrated Tamarin macros and can be found in the [`macros.splib`](https://github.com/nikstuckenbrock/TLS13Tamarin/blob/rfc8446-updates/src/model/macros.splib).
///

/// html | div[style='clear: both;']
///