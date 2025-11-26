# [4. Handshake Protocol](https://datatracker.ietf.org/doc/html/rfc8446#section-4)

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
All the different handshake message type values are defined as single macros in the [`macros.splib`](https://github.com/nikstuckenbrock/TLS13Tamarin/blob/rfc8446-updates/src/model/macros.splib).
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