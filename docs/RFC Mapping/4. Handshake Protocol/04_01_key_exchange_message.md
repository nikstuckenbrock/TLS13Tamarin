# [4.1. Key Exchange Messages](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1)

## [4.1.2 Client Hello](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
struct {
    ProtocolVersion legacy_version = 0x0303;    /* TLS v1.2 */
    Random random;
    opaque legacy_session_id<0..32>;
    CipherSuite cipher_suites<2..2^16-2>;
    opaque legacy_compression_methods<1..2^8-1>;
    Extension extensions<8..2^16-1>;
} ClientHello;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
LegacyVersion() = '0x0303',
ClientHello(
    random,
    legacy_session_id,
    cipher_suites,
    legacy_compression_methods,
    extensions
) = Handshake(
    HandshakeMessageTypeClientHello(),
    <LegacyVersion(),
    random,
    legacy_session_id,
    cipher_suites,
    legacy_compression_methods,
    extensions>
),
```
///

/// html | div[style='clear: both;']
///

## [4.1.3 Server Hello](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.3)

## [4.1.4 Hello Retry Request](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.4)