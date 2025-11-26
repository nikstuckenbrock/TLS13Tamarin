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
```title="macros.splib"
ProtocolVersion() = '0x0303',
ExtensionSupportedVersions() = Extension('43', ProtocolVersion()),
```
///

/// html | div[style='clear: both;']
///

The structure of an extension is based on the extension itself.
Therefor the extension wrapper struct just contains the type and the extension data.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
struct {
    ExtensionType extension_type;
    opaque extension_data<0..2^16-1>;
} Extension;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
Extension(extension_type, extension_data) = <extension_type, extension_data>,
```
///

/// html | div[style='clear: both;']
///

## 4.2.1. Supported Versions

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
ProtocolVersion() = '0x0303',
ExtensionSupportedVersions() = Extension('43', ProtocolVersion()),
```
///

/// html | div[style='clear: both;']
///

## 4.2.2. Cookie

## 4.2.3. Signature Algorithms

## 4.2.4. Certificate Algorithms

## 4.2.5. OID Filters

## 4.2.6. Post-Handshake Client Authentication
