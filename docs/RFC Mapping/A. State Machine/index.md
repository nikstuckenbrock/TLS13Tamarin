# [A. State Machine](https://datatracker.ietf.org/doc/html/rfc8446#appendix-A)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
This appendix provides a summary of the legal state transitions for
the client and server handshakes.  State names (in all capitals,
e.g., START) have no formal meaning but are provided for ease of
comprehension.  Actions which are taken only in certain circumstances
are indicated in [].  The notation "K_{send,recv} = foo" means "set
the send/recv key to the given key".
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The state machines shown in the following section won't map completely to the RFC.
This is because of the model not covering all TLS features and extensions.
///

/// html | div[style='clear: both;']
///