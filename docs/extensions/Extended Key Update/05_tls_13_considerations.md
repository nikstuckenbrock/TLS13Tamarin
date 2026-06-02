# 5. TLS 1.3 Considerations

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
The following steps are taken by a TLS 1.3 implementation; the steps
executed with DTLS 1.3 differ slightly.

1. The initiator sends `ExtendedKeyUpdate(key_update_request)` carrying a
`KeyShareEntry`. While an extended key update is in progress, the
initiator MUST NOT initiate another key update.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
2. Upon receipt, the responder sends its own `KeyShareEntry` in a `ExtendedKeyUpdate(key_update_response)` message.
While an extended key update is in progress, the responder MUST NOT initiate another key update.
The responder MAY defer sending a response if system load or resource constraints prevent immediate processing.
In such cases, the response MUST be sent once sufficient resources become available.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
3. After the responder sends the ExtendedKeyUpdate(key_update_response) it MUST update its send keys.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
4. Upon receipt of an ExtendedKeyUpdate(key_update_response) the initiator derives the new secrets from the exchanged key shares. The initiator then updates its receive keys and sends an empty ExtendedKeyUpdate(key_update_finish) message to complete the process. The initiator MUST NOT defer derivation of the secrets and sending the ExtendedKeyUpdate(key_update_finish) message as it would stall the communication.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 5.1. TLS 1.3 Extended Key Update Example