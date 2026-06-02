# 4. Extended Key Update Messages

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
If the client and server agree to use the extended key update mechanism, the standard key update MUST NOT be used. In this case, the extended key update fully replaces the standard key update functionality.

Implementations that receive a classic KeyUpdate message after successfully negotiating the Extended Key Update functionality MUST terminate the connection with an "unexpected_message" alert.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
///

/// html | div[style='clear: both;']
///


/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
The extended key update messages are signaled in a new handshake message named ExtendedKeyUpdate (EKU), with an internal uint8 message subtype indicating its role. This specification defines three ExtendedKeyUpdate message subtypes:

    key_update_request (0)

    key_update_response (1)

    key_update_finish (2)

New ExtendedKeyUpdate message subtypes are assigned by IANA as described in Section 13.3.

A TLS peer which receives a ExtendedKeyUpdate with an unexpected message subtype MUST abort the connection with an "unexpected_message" alert.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The threee message subtypes are defined as macros in the [macros.splib](#).
```
ExtendedKeyUpdateRequest(key_share_entry) = <'0', key_share_entry>,
ExtendedKeyUpdateResponse(key_share_entry) = <'1', key_share_entry>,
ExtendedKeyUpdateFinish() = <'2'>,
```
As the extended key update messages are a subtype of the handshake message, a knew handshake message type was introduced as a macro.
```
HandshakeMessageTypeExtendedKeyUpdate() = 'TBD',
```
///

/// html | div[style='clear: both;']
///


