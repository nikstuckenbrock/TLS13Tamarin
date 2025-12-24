# [5.5. Limits on Key Usage](https://datatracker.ietf.org/doc/html/rfc8446#section-5.5)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
There are cryptographic limits on the amount of plaintext which can
be safely encrypted under a given set of keys.  [AEAD-LIMITS]
provides an analysis of these limits under the assumption that the
underlying primitive (AES or ChaCha20) has no weaknesses.
Implementations SHOULD do a key update as described in Section 4.6.3
prior to reaching these limits.

For AES-GCM, up to 2^24.5 full-size records (about 24 million) may be
encrypted on a given connection while keeping a safety margin of
approximately 2^-57 for Authenticated Encryption (AE) security.  For
ChaCha20/Poly1305, the record sequence number would wrap before the
safety limit is reached.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The RFC states that at specific timepoint implementations should initiate a key update as described in [section 4.6.3](./../4.%20Handshake%20Protocol/04_06_post_handshake_messages.md).
///

/// html | div[style='clear: both;']
///