# Hello Retry Request

The Hello Retry Request is actually a special `ServerHello` message.
It uses the a constant value for the Random value of the `ServerHello` struct.

```
For reasons of backward compatibility with middleboxes (see
Appendix D.4), the HelloRetryRequest message uses the same structure
as the ServerHello, but with Random set to the special value of the
SHA-256 of "HelloRetryRequest":

  CF 21 AD 74 E5 9A 61 11 BE 1D 8C 02 1E 65 B8 91
  C2 A2 11 16 7A BB 8C 5E 07 9E 09 E2 C8 A8 33 9C

Upon receiving a message with type server_hello, implementations MUST
first examine the Random value and, if it matches this value, process
it as described in Section 4.1.4).
```

In Tamarin the special value is modelled using a macro `HelloRetryRequestRandom() = h('HelloRetryRequest')` in the [`macros.splib`](https://github.com/nikstuckenbrock/TLS13Tamarin/blob/rfc8446-updates/src/model/macros.splib).