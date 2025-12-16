# [1. Introduction](https://datatracker.ietf.org/doc/html/rfc8446#section-1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
The primary goal of TLS is to provide a secure channel between two
communicating peers; the only requirement from the underlying
transport is a reliable, in-order data stream.  Specifically, the
secure channel should provide the following properties:

-  Authentication: The server side of the channel is always
    authenticated; the client side is optionally authenticated.
    Authentication can happen via asymmetric cryptography (e.g., RSA
    [RSA], the Elliptic Curve Digital Signature Algorithm (ECDSA)
    [ECDSA], or the Edwards-Curve Digital Signature Algorithm (EdDSA)
    [RFC8032]) or a symmetric pre-shared key (PSK).

-  Confidentiality: Data sent over the channel after establishment is
    only visible to the endpoints.  TLS does not hide the length of
    the data it transmits, though endpoints are able to pad TLS
    records in order to obscure lengths and improve protection against
    traffic analysis techniques.

-  Integrity: Data sent over the channel after establishment cannot
    be modified by attackers without detection.

These properties should be true even in the face of an attacker who
has complete control of the network, as described in [RFC3552].  See
Appendix E for a more complete statement of the relevant security
properties.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
As the introduction section of the RFC mentions, the protocol should provide a secure channel between two communicating peers.
The two peers are modelled as `server` and `client`.
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
TLS consists of two primary components:

-  A handshake protocol (Section 4) that authenticates the
    communicating parties, negotiates cryptographic modes and
    parameters, and establishes shared keying material.  The handshake
    protocol is designed to resist tampering; an active attacker
    should not be able to force the peers to negotiate different
    parameters than they would if the connection were not under
    attack.

-  A record protocol (Section 5) that uses the parameters established
    by the handshake protocol to protect traffic between the
    communicating peers.  The record protocol divides traffic up into
    a series of records, each of which is independently protected
    using the traffic keys.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The model focuses on the Handshake proctol in [section 4](./../4.%20Handshake%20Protocol/index.md).
Nevertheless there is a highly abstract version of the record layer modeled and it is explained in [section 5.1](./../5.%20Record%20Protocol/05_01_record_layer.md).
///

/// html | div[style='clear: both;']
///