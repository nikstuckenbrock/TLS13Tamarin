# [5.2. Record Payload Protection](https://datatracker.ietf.org/doc/html/rfc8446#section-5.2)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
The record protection functions translate a TLSPlaintext structure
into a TLSCiphertext structure.  The deprotection functions reverse
the process.  In TLS 1.3, as opposed to previous versions of TLS, all
ciphers are modeled as "Authenticated Encryption with Associated
Data" (AEAD) [RFC5116].  AEAD functions provide a unified encryption
and authentication operation which turns plaintext into authenticated
ciphertext and back again.  Each encrypted record consists of a
plaintext header followed by an encrypted body, which itself contains
a type and optional padding.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The record payload protection is not modelled in detail.
For more information have a look at [section 5](./index.md).
///

/// html | div[style='clear: both;']
///