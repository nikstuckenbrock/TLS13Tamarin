# [4.2. Extensions](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2)

Key exchange messages like the [Client Hello](./04_01_key_exchange_message.md#412-client-hello) or [Server Hello](./04_01_key_exchange_message.md#413-server-hello) support an optional list of extensions.
Each extension is identified by a unique number.
All enumeration values (relevant for the model) are directly encoded in the extension [`macros.splib`](https://github.com/nikstuckenbrock/TLS13Tamarin/blob/rfc8446-updates/src/).
The code belows shows an example for the Support Version extension.


/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
enum {
    server_name(0),                             /* RFC 6066 */
    max_fragment_length(1),                     /* RFC 6066 */
    status_request(5),                          /* RFC 6066 */
    supported_groups(10),                       /* RFC 8422, 7919 */
    signature_algorithms(13),                   /* RFC 8446 */
    use_srtp(14),                               /* RFC 5764 */
    heartbeat(15),                              /* RFC 6520 */
    application_layer_protocol_negotiation(16), /* RFC 7301 */
    signed_certificate_timestamp(18),           /* RFC 6962 */
    client_certificate_type(19),                /* RFC 7250 */
    server_certificate_type(20),                /* RFC 7250 */
    padding(21),                                /* RFC 7685 */
    pre_shared_key(41),                         /* RFC 8446 */
    early_data(42),                             /* RFC 8446 */
    supported_versions(43),                     /* RFC 8446 */
    cookie(44),                                 /* RFC 8446 */
    psk_key_exchange_modes(45),                 /* RFC 8446 */
    certificate_authorities(47),                /* RFC 8446 */
    oid_filters(48),                            /* RFC 8446 */
    post_handshake_auth(49),                    /* RFC 8446 */
    signature_algorithms_cert(50),              /* RFC 8446 */
    key_share(51),                              /* RFC 8446 */
    (65535)
} ExtensionType;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
ProtocolVersion() = '0x0303',
ExtensionSupportedVersions() = Extension('43', ProtocolVersion()),
```
///

/// html | div[style='clear: both;']
///

The structure of an extension is based on the extension itself.
Therefor the extension wrapper struct just contains the type and the extension data.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
struct {
    ExtensionType extension_type;
    opaque extension_data<0..2^16-1>;
} Extension;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
Extension(extension_type, extension_data) = <extension_type, extension_data>,
```
///

/// html | div[style='clear: both;']
///

## [4.2.1. Supported Versions](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.1)

Downgrade protection and therefor multiple supported versions are not implemented in the model by now.
Nevertheless the model includes the extension itself but does not negotiate the supported version.
It is assumed that both peers only support one version, which is the same.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
uint16 ProtocolVersion;
struct {
    select (Handshake.msg_type) {
        case client_hello:
            ProtocolVersion versions<2..254>;

        case server_hello: /* and HelloRetryRequest */
            ProtocolVersion selected_version;
    };
} SupportedVersions;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
ProtocolVersion() = '0x0304',
ExtensionSupportedVersions() = Extension('43', ProtocolVersion()),
```
///

/// html | div[style='clear: both;']
///

## [4.2.2. Cookie](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.2)

This extension is currently not covered in the model.

## [4.2.3. Signature Algorithms](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.3)

The client uses the "signature_algorithms" extension to indicate to the server which signature algorithms may be used in digital signatures. Clients which desire the server to authenticate itself via a certificate MUST send this extension.
Due to the assumption of "perfect crypto" much of this extension is irrelevant.
The offered list is simply modelled as some public knowledge parameter and validate the integrity of those algorithms in the transcript.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
TLS 1.3 provides two extensions for indicating which signature
algorithms may be used in digital signatures.  The
"signature_algorithms_cert" extension applies to signatures in
certificates, and the "signature_algorithms" extension, which
originally appeared in TLS 1.2, applies to signatures in
CertificateVerify messages.  The keys found in certificates MUST also
be of appropriate type for the signature algorithms they are used
with.  This is a particular issue for RSA keys and PSS signatures, as
described below.  If no "signature_algorithms_cert" extension is
present, then the "signature_algorithms" extension also applies to
signatures appearing in certificates.  Clients which desire the
server to authenticate itself via a certificate MUST send the
"signature_algorithms" extension.  If a server is authenticating via
a certificate and the client has not sent a "signature_algorithms"
extension, then the server MUST abort the handshake with a
"missing_extension" alert (see Section 9.2).

    struct {
        SignatureScheme supported_signature_algorithms<2..2^16-2>;
    } SignatureSchemeList;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
ExtensionSignatureSchemeList(supported_signature_algorithms) = Extension('13', supported_signature_algorithms)
```

```title="src/model/serverPsk.splib"
extensions = <
    ExtensionSignatureSchemeList($sig_algs),
    <'41', '0'>,
    p_edi
>
```
///

/// html | div[style='clear: both;']
///

## [4.2.4. Certificate Algorithms](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.4)

The certificate authorities extension is not modelled at the moment.

## [4.2.5. OID Filters](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.5)

The OID filters extension is not modelled at the moment.

## [4.2.6. Post-Handshake Client Authentication](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.6)

The Post-Handshake Client Authentication is not modelled at the moment.

## [4.2.7. Supported Groups](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.7)

When sent by the client, the "supported_groups" extension indicates the named groups which the client supports for key exchange, ordered from most preferred to least preferred.
The model only support the client sending two (distinct) groups.
However, `$g1` and `$g2` are free to be any value, so any two client hello messages may have no overlapping groups.
You can find more information about this in [section 4.1.4](./04_01_key_exchange_message.md#414-hello-retry-request).

As of TLS 1.3, servers are permitted to send the "supported_groups" extension to the client. If the server has a group it prefers to the ones in the "key_share" extension but is still willing to accept the ClientHello, it SHOULD send "supported_groups" to update the client's view of its preferences; this extension SHOULD contain all groups the server supports, regardless of whether they are currently supported by the client. Clients MUST NOT act upon any information found in "supported_groups" prior to successful completion of the handshake, but MAY use the information learned from a successfully completed handshake to change what groups they use in their "key_share" extension in subsequent connections.
This behavior is not modelled at the moment.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
When sent by the client, the "supported_groups" extension indicates
the named groups which the client supports for key exchange, ordered
from most preferred to least preferred.

Note: In versions of TLS prior to TLS 1.3, this extension was named
"elliptic_curves" and only contained elliptic curve groups.  See
[RFC8422] and [RFC7919].  This extension was also used to negotiate
ECDSA curves.  Signature algorithms are now negotiated independently
(see Section 4.2.3).

The "extension_data" field of this extension contains a
"NamedGroupList" value:

    enum {

        /* Elliptic Curve Groups (ECDHE) */
        secp256r1(0x0017), secp384r1(0x0018), secp521r1(0x0019),
        x25519(0x001D), x448(0x001E),

        /* Finite Field Groups (DHE) */
        ffdhe2048(0x0100), ffdhe3072(0x0101), ffdhe4096(0x0102),
        ffdhe6144(0x0103), ffdhe8192(0x0104),

        /* Reserved Code Points */
        ffdhe_private_use(0x01FC..0x01FF),
        ecdhe_private_use(0xFE00..0xFEFF),
        (0xFFFF)
    } NamedGroup;

    struct {
        NamedGroup named_group_list<2..2^16-1>;
    } NamedGroupList;

Elliptic Curve Groups (ECDHE):  Indicates support for the
    corresponding named curve, defined in either FIPS 186-4 [DSS] or
    [RFC7748].  Values 0xFE00 through 0xFEFF are reserved for
    Private Use [RFC8126].

Finite Field Groups (DHE):  Indicates support for the corresponding
    finite field group, defined in [RFC7919].  Values 0x01FC through
    0x01FF are reserved for Private Use.

Items in named_group_list are ordered according to the sender's
preferences (most preferred choice first).

As of TLS 1.3, servers are permitted to send the "supported_groups"
extension to the client.  Clients MUST NOT act upon any information
found in "supported_groups" prior to successful completion of the
handshake but MAY use the information learned from a successfully
completed handshake to change what groups they use in their
"key_share" extension in subsequent connections.  If the server has a
group it prefers to the ones in the "key_share" extension but is
still willing to accept the ClientHello, it SHOULD send
"supported_groups" to update the client's view of its preferences;
this extension SHOULD contain all groups the server supports,
regardless of whether they are currently supported by the client.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
ExtensionNamedGroupdList(supported_groups) = Extension('10', supported_groups),
```

```title="src/model/client.splib"
supported_groups = <$g1, $g2>
extensions = <
    ExtensionSupportedVersions(),
    ExtensionNamedGroupdList(supported_groups),
    ExtensionSignatureSchemeList($sig_algs),
    ExtensionKeyShare(KeyShareEntry($g1, gx))
>
```
///

/// html | div[style='clear: both;']
///

## [4.2.8. Key Share](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.8)

The key share extension is modelled using macros.
Named groups are global values and the key exchange contains the calculated value for the key.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Clients MAY send an empty client_shares vector in order to request
group selection from the server, at the cost of an additional round
trip (see Section 4.1.4).

    struct {
        NamedGroup group;
        opaque key_exchange<1..2^16-1>;
    } KeyShareEntry;

group:  The named group for the key being exchanged.

key_exchange:  Key exchange information.  The contents of this field
    are determined by the specified group and its corresponding
    definition.  Finite Field Diffie-Hellman [DH76] parameters are
    described in Section 4.2.8.1; Elliptic Curve Diffie-Hellman
    parameters are described in Section 4.2.8.2.

In the ClientHello message, the "extension_data" field of this
extension contains a "KeyShareClientHello" value:

    struct {
        KeyShareEntry client_shares<0..2^16-1>;
    } KeyShareClientHello;

client_shares:  A list of offered KeyShareEntry values in descending
    order of client preference.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
KeyShareEntry(named_group, key_exchange) = <named_group, key_exchange>,
ExtensionKeyShare(share) = Extension('51', share),
```

```title="src/model/client.splib"
ExtensionKeyShare(KeyShareEntry($g1, gx))
```
///

/// html | div[style='clear: both;']
///

### [4.2.8.1. Diffie-Hellman Parameters](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.8.1)

The diagram below shows how the two parties agree on DHE parameters.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Diffie-Hellman [DH76] parameters for both clients and servers are
encoded in the opaque key_exchange field of a KeyShareEntry in a
KeyShare structure.  The opaque value contains the Diffie-Hellman
public value (Y = g^X mod p) for the specified group (see [RFC7919]
for group definitions) encoded as a big-endian integer and padded to
the left with zeros to the size of p in bytes.

Note: For a given Diffie-Hellman group, the padding results in all
public keys having the same length.

Peers MUST validate each other's public key Y by ensuring that 1 < Y
< p-1.  This check ensures that the remote peer is properly behaved
and isn't forcing the local system into a small subgroup.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/client.splib"
gx = $g1^~x
ExtensionKeyShare(KeyShareEntry($g1, gx))
```

```
    Client                        Server
supports g1, g2               supports g

<g1, g2>, <g1, g1^x> ---->  if g != g1

                    <----- HRR <g>

checks g2 == g 
<g1, g2>, <g2, g2^x2> ---->  checks g == g2

                    <------ <g, g^y>


                Both parties compute
                        g^xy
```
///

/// html | div[style='clear: both;']
///

### [4.2.8.2. ECDHE Parameters](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.8.2)

For the symbolic model there is no specific modelling of the ECDHE parameters.

## [4.2.9. Pre-Shared Key Exchange Modes](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.9)

The client as always supports both modes, allowing the server to choose between `psk_ke` and `psk_dhe_ke`.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
In order to use PSKs, clients MUST also send a
"psk_key_exchange_modes" extension.  The semantics of this extension
are that the client only supports the use of PSKs with these modes,
which restricts both the use of PSKs offered in this ClientHello and
those which the server might supply via NewSessionTicket.

A client MUST provide a "psk_key_exchange_modes" extension if it
offers a "pre_shared_key" extension.  If clients offer
"pre_shared_key" without a "psk_key_exchange_modes" extension,
servers MUST abort the handshake.  Servers MUST NOT select a key
exchange mode that is not listed by the client.  This extension also
restricts the modes for use with PSK resumption.  Servers SHOULD NOT
send NewSessionTicket with tickets that are not compatible with the
advertised modes; however, if a server does so, the impact will just
be that the client's attempts at resumption fail.

The server MUST NOT send a "psk_key_exchange_modes" extension.

    enum { psk_ke(0), psk_dhe_ke(1), (255) } PskKeyExchangeMode;

    struct {
        PskKeyExchangeMode ke_modes<1..255>;
    } PskKeyExchangeModes;

psk_ke:  PSK-only key establishment.  In this mode, the server
    MUST NOT supply a "key_share" value.

psk_dhe_ke:  PSK with (EC)DHE key establishment.  In this mode, the
    client and server MUST supply "key_share" values as described in
    Section 4.2.8.

Any future values that are allocated must ensure that the transmitted
protocol messages unambiguously identify which mode was selected by
the server; at present, this is indicated by the presence of the
"key_share" in the ServerHello.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
PskKeyExchangeModePskKe() = '0',
PskKeyExchangeModePskDheKe() = '1',
ExtensionPskKeyExchangeModes(ke_mode) = Extension('45', ke_mode),
```

```title="src/model/clientPsk.splib"
psk_ke_mode = <PskKeyExchangeModePskKe(), PskKeyExchangeModePskDheKe()>

...

ExtensionPskKeyExchangeModes(psk_ke_mode),
```
///

/// html | div[style='clear: both;']
///

## [4.2.10. Early Data Indication](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.10)

When sending a `ClientHello` for a PSK handshake, space is always allocated for the `EarlyDataIndication` extension. However, depending on whether the extension should be used or not, the value is changed locally.

This allows us to pattern match on the server-side the client sending a hello with the extension present or not. For example, the client always sends this extension on the first PSK handshake attempt, but if the server sends a HRR in response to the initial message, the client never sends the extension on the second flight.

As noted in the PSK extension section, we use a pair of functions mask, unmask to capture the obfuscated ticket age mechanism, though it is not clear if this models anything interesting.

The `EndOfEarlyData` message message is currently not modelled.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
When a PSK is used, the client can send application data in its first flight of messages. If the client opts to do so, it MUST supply an "early_data" extension as well as the "pre_shared_key" extension.

The "extension_data" field of this extension contains an "EarlyDataIndication" value:

   struct {} Empty;

   struct {
       select (Handshake.msg_type) {
           case new_session_ticket:   uint32 max_early_data_size;
           case client_hello:         Empty;
           case encrypted_extensions: Empty;
       };
   } EarlyDataIndication;

See for the use of the max_early_data_size field.

The parameters for the 0-RTT data (symmetric cipher suite, ALPN protocol, etc.) are the same as those which were negotiated in the connection which established the PSK. The PSK used to encrypt the early data MUST be the first PSK listed in the client's "pre_shared_key" extension.

For PSKs provisioned via NewSessionTicket, a server MUST validate that the ticket age for the selected PSK identity (computed by subtracting ticket_age_add from PskIdentity.obfuscated_ticket_age modulo 2^32) is within a small tolerance of the time since the ticket was issued (see ). If it is not, the server SHOULD proceed with the handshake but reject 0-RTT, and SHOULD NOT take any other action that assumes that this ClientHello is fresh.

0-RTT messages sent in the first flight have the same (encrypted) content types as their corresponding messages sent in other flights (handshake and application_data) but are protected under different keys. After receiving the server's Finished message, if the server has accepted early data, an EndOfEarlyData message will be sent to indicate the key change. This message will be encrypted with the 0-RTT traffic keys.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
ExtensionEarlyDataIndication() = Extension('42', <'0'>),
```
///

/// html | div[style='clear: both;']
///

## [4.2.11. Pres-Shared Key Extension](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.11)