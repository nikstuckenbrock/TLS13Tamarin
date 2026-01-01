# [4.6. Post-Handshake Messages](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6)

```title="RFC 8446"
TLS also allows other messages to be sent after the main handshake.
These messages use a handshake content type and are encrypted under
the appropriate application traffic key.
```

## [4.6.1. New Session Ticket Message](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.1)

Currently the server can send a `NewSessionTicket` message using the rule `new_session_ticket`.
The corresponding `recv_` rule on the client side completes the exchange by receiving the message and generating the relevant values.
That is, the lifetime of a session ticket is not modelled at the moment.
When the server/client sends/receives resp. the NewSessionTicket message, they also output a !Server/!ClientPSK fact which encapsulates the PSK state:

`!ServerPSK(S, C, res_psk, auth_status, NewSessionTicket, 'nst'),`

This stores:
* server and client identities
* resumption master secret (res_psk)
* authentication status of the peer
* NewSessionTicket message blob, containing all other variables (ticket, ticket_age_add, etc.)
* type of session ticket ('nst' for NewSessionTicket, 'oob' for out of band PSK)


/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
At any time after the server has received the client Finished
message, it MAY send a NewSessionTicket message.  This message
creates a unique association between the ticket value and a secret
PSK derived from the resumption master secret (see Section 7).
```

```title="RFC 8446"
struct {
    uint32 ticket_lifetime;
    uint32 ticket_age_add;
    opaque ticket_nonce<0..255>;
    opaque ticket<1..2^16-1>;
    Extension extensions<0..2^16-2>;
} NewSessionTicket;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
NewSessionTicket(ticket_lifetime, ticket_age_add, ticket, ticket_extension) = Handshake(HandshakeMessageTypeNewSessionTicket(), <ticket_lifetime, ticket_age_add, ticket, ticket_extension>),
```

```title="src/model/server.splib"
ticket_extension = <
    <'46', $max_early_data_size>
>
message = NewSessionTicket($ticket_lifetime, ~ticket_age_add, ~ticket, ticket_extension)
```
///

/// html | div[style='clear: both;']
///

## [4.6.2. Post-Handshake Authentication](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.2)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
When the client has sent the "post_handshake_auth" extension (see
Section 4.2.6), a server MAY request client authentication at any
time after the handshake has completed by sending a
CertificateRequest message.  The client MUST respond with the
appropriate Authentication messages (see Section 4.4).  If the client
chooses to authenticate, it MUST send Certificate, CertificateVerify,

and Finished.  If it declines, it MUST send a Certificate message
containing no certificates followed by Finished.  All of the client's
messages for a given response MUST appear consecutively on the wire
with no intervening messages of other types.

A client that receives a CertificateRequest message without having
sent the "post_handshake_auth" extension MUST send an
"unexpected_message" fatal alert.

Note: Because client authentication could involve prompting the user,
servers MUST be prepared for some delay, including receiving an
arbitrary number of other messages between sending the
CertificateRequest and receiving a response.  In addition, clients
which receive multiple CertificateRequests in close succession MAY
respond to them in a different order than they were received (the
certificate_request_context value allows the server to disambiguate
the responses).
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
There are two main concerns to model:

1. Optional client auth
2. Multiple concurrent auth reqs/responses

The first one is currently not supported.
That is, the client will either never reply, or will send a certificate.
Server certificate requests generate a new `ServerCertReq` fact which encapsulates the server storing additional state to track the certificate requests.
This value is: `ServerCertReq(tid, S, C, certificate_request_context),` which tracks the current session (tid), the identities of server and client, and the context value used to disambiguate the requests.
The client has equivalent facts for the same purpose.
///

/// html | div[style='clear: both;']
///

## [4.6.3. Key and Initialization Vector Update](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.3)

All key update related rules can be found in `src/model/keyUpdate.splib`.

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
enum {
    update_not_requested(0), update_requested(1), (255)
} KeyUpdateRequest;

struct {
    KeyUpdateRequest request_update;
} KeyUpdate;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
KeyUpdateUpdateNotRequested() = '0',
KeyUpdateUpdateRequested() = '1',
KeyUpdate(update_requested) = Handshake(HandshakeMessageTypeKeyUpdate(), <update_requested>),
```
///

/// html | div[style='clear: both;']
///