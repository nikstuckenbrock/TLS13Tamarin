# [2.2. Resumption and Pre-Shared Key (PSK)](https://datatracker.ietf.org/doc/html/rfc8446#section-2.2)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Although TLS PSKs can be established out of band, PSKs can also be
established in a previous connection and then used to establish a new
connection ("session resumption" or "resuming" with a PSK).  Once a
handshake has completed, the server can send the client a PSK
identity that corresponds to a unique key derived from the initial
handshake (see Section 4.6.1).  The client can then use that PSK
identity in future handshakes to negotiate the use of the associated
PSK.  If the server accepts the PSK, then the security context of the
new connection is cryptographically tied to the original connection
and the key derived from the initial handshake is used to bootstrap
the cryptographic state instead of a full handshake.  In TLS 1.2 and
below, this functionality was provided by "session IDs" and "session
tickets" [RFC5077].  Both mechanisms are obsoleted in TLS 1.3.

PSKs can be used with (EC)DHE key exchange in order to provide
forward secrecy in combination with shared keys, or can be used
alone, at the cost of losing forward secrecy for the application
data.
```
/// 

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Note:  When using an out-of-band provisioned pre-shared secret, a
    critical consideration is using sufficient entropy during the key
    generation, as discussed in [RFC4086].  Deriving a shared secret
    from a password or other low-entropy sources is not secure.  A
    low-entropy secret, or password, is subject to dictionary attacks
    based on the PSK binder.  The specified PSK authentication is not
    a strong password-based authenticated key exchange even when used
    with Diffie-Hellman key establishment.  Specifically, it does not
    prevent an attacker that can observe the handshake from performing
    a brute-force attack on the password/pre-shared key.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
This note on out-of-band provisioned pre-shared secret is not implemented in the model for now.
Cryprographic primitives are considered perfect.
Non the less one could implement sufficient entropy by modelling the assumed problems it has.
Then one could analyse the consequences of this.
///

/// html | div[style='clear: both;']
///