# [4. Handshake Protocol](https://datatracker.ietf.org/doc/html/rfc8446#section-4)

The handshake protocol consists of several message types.
Each message type is identified by a unique number.
All enumeration values (relevant for the model) are defined as macros containing a string with the message identifier in the [`macros.splib`](https://github.com/nikstuckenbrock/TLS13Tamarin/blob/rfc8446-updates/src/).

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
enum {
    client_hello(1),
    server_hello(2),
    new_session_ticket(4),
    end_of_early_data(5),
    encrypted_extensions(8),
    certificate(11),
    certificate_request(13),
    certificate_verify(15),
    finished(20),
    key_update(24),
    message_hash(254),
    (255)
} HandshakeType;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
HandshakeMessageTypeClientHello() = '1',
HandshakeMessageTypeServerHello() = '2',
HandshakeMessageTypeNewSessionTicket() = '4',
HandshakeMessageTypeEncryptedExtensions() = '8',
HandshakeMessageTypeCertificate() = '11',
HandshakeMessageTypeCertificateRequest() = '13',
HandshakeMessageTypeCertificateVerify() = '15',
HandshakeMessageTypeFinished() = '20',
HandshakeMessageTypeKeyUpdate() = '24',
```
///

/// html | div[style='clear: both;']
///

Each message type has a different content.
Therefor the general handshake message structure is modelled using a macro.
The length of the message is not modelled because in symbolic modelling we use abstract terms for messages.
Concrete representation of messages (e.g. length, bit-structure or padding) are not validated.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
struct {
    HandshakeType msg_type;    /* handshake type */
    uint24 length;             /* remaining bytes in message */
    select (Handshake.msg_type) {
        case client_hello:          ClientHello;
        case server_hello:          ServerHello;
        case end_of_early_data:     EndOfEarlyData;
        case encrypted_extensions:  EncryptedExtensions;
        case certificate_request:   CertificateRequest;
        case certificate:           Certificate;
        case certificate_verify:    CertificateVerify;
        case finished:              Finished;
        case new_session_ticket:    NewSessionTicket;
        case key_update:            KeyUpdate;
    };
} Handshake;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
Handshake(msg_type, content) = <msg_type, content>,
```
///

/// html | div[style='clear: both;']
///