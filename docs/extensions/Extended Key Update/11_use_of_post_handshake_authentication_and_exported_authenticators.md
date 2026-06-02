# 11. Use of Post-Handshake Authentication and Exported Authenticators with Extended Key Update

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
EKU provides fresh traffic secrets, but EKU alone does not authenticate that both endpoints derived the same updated keys. An attacker that temporarily compromises an endpoint may later act as an active MitM capable of interfering with the EKU exchange. Such an attacker can cause the peers to transition to divergent traffic secrets without detection, but cannot compromise the endpoint to derive secrets after the new epoch is established. To confirm that both peers transitioned to the same new key state, TLS 1.3 provides two mechanisms: Post-Handshake Certificate-Based Client Authentication and Exported Authenticators [RFC9261].
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
///

/// html | div[style='clear: both;']
///

## 11.1. Post-Handshake Certificate-Based Client Authentication

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
When Post-Handshake Certificate-Based Client Authentication (Section 4.6.2 of [TLS]) is performed after an Extended Key Update (EKU) is complete, the Handshake Context used for the transcript hash is updated. It consists of transcript_hash_N+1 concatenated with the CertificateRequest message. The Finished message is computed using a MAC key derived from the Base Key of the new epoch (client_application_traffic_secret_N+1). This confirms that both peers are operating with the same updated traffic keys and completes an authenticated transition after the EKU.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 11.2. Exported Authenticators

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
This document updates Section 5.1 of [RFC9261] to specify that, after an Extended Key Update has completed, the Handshake Context and Finished MAC Key used for Exported Authenticators MUST be derived from the exporter secret associated with the current epoch. Implementations that support the epoch-aware Exported Authenticators interface MUST provide a means for applications to request the generation or validation of Exported Authenticators using the exporter secret for a specific epoch.

The Handshake Context and Finished MAC Key used in both the CertificateVerify message (Section 5.2.2 of [RFC9261]) and the Finished message (Section 5.2.3 of [RFC9261]) are derived from the exporter secret associated with the current epoch. If a MitM interferes with the EKU exchange and causes the peers to derive different traffic and exporter secrets, their Handshake Contexts and Finished MAC Keys will differ. As a result, validation procedures specified in Section 5.2.4 of [RFC9261] will fail, thereby detecting the divergence of key state between peers.

A new optional API SHOULD be defined to permit applications to request or verify Exported Authenticators for a specific exporter epoch. As discussed in Section 7 of [RFC9261], this can, as an exception, be implemented at the application layer when the epoch-aware TLS exporter is available. The APIs defined in [RFC9261] remain unchanged, so existing applications continue to operate without modification. The epoch-aware API accepts an epoch identifier; when present, the (D)TLS implementation MUST derive the Handshake Context and Finished MAC Key from the exporter secret associated with that epoch. When Exported Authenticators are generated using the epoch-aware Exported Authenticators interface, the epoch identifier used for their derivation can be conveyed in the certificate_request_context field, allowing the peer, particularly in DTLS where records may be reordered, to determine the correct exporter secret for validation.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 11.3. Interaction of Extended Key Update and Post-Handshake Authentication

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
EKU and post-handshake authentication may both occur during the lifetime of a (D)TLS connection. Post-Handshake Certificate-Based Client Authentication (PHA) is bound to the handshake transcript and computes its Finished message as specified in Section 4.4 of [TLS], using a key derived from the application traffic secret that is active at the time the CertificateRequest is sent. Therefore, specific ordering constraints are required to preserve cryptographic consistency.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

### 11.3.1. Post-Handshake Certificate-Based Client Authentication

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
An endpoint MUST NOT complete an EKU exchange in a manner that transitions to new application traffic secrets while a PHA exchange is in progress.

The following constraints apply to both TLS 1.3 and DTLS 1.3:

*   An endpoint MUST NOT initiate PHA while an EKU exchange is in progress.

*    If PHA has been initiated and the corresponding authentication exchange has not yet completed, neither endpoint MUST initiate an EKU exchange.

*    In a cross-flight condition, if a (D)TLS client sends an EKU request and, before receiving a response, receives a CertificateRequest from the (D)TLS server, the endpoints MUST defer completion of the EKU exchange and proceed with the post-handshake authentication exchange. The endpoints MUST NOT transition to new application traffic secrets until the authentication exchange has completed.

In DTLS, deferred EKU request is acknowledged as specified in Section 6.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
To ensure this behaviour a new information has been added to the `ServerState` and `ClientState` as well as two new macros for a running or not running Post-Handshake authentication.
```title="src/model/macros.splib"
PostHandshakeAuthenticationRunning() = <'1'>,
PostHandshakeAuthenticationNotRunning() = <'0'>
```
Each rule implemented for the Extended Key Update requires the Post-Handshake not to be running, which ensures the priorisation describes on the left hand side.
```title="src/model/extendedKeyUpdate.splib"
rule extended_key_update_request_client[color=#340068]:
    let
        gx = p_g^~x
        key_share_entry = KeyShareEntry(p_g, gx)
        request = Handshake(HandshakeMessageTypeExtendedKeyUpdate(), ExtendedKeyUpdateRequest(key_share_entry))
    in
    [
        Fr(~x),
        SendStream(~tid, $C, $S, p_auth_status, applicationTrafficKeyClient),
        ClientState(
            ...
            PostHandshakeAuthenticationNotRunning()
        )
    ]
    --[
        ExtendedKeyUpdateRequestClient(~tid),
        Instance(~tid, $C, 'client')
    ]->
    [
        C4_Extended_Key_Update(~tid, 'EKU0', $C, $S, ~x, gx, '0', <request>),
        MessageOut(senc{request}applicationTrafficKeyClient),
        !ExtendedKeyUpdateDH(~tid, $C, ~x),
        ClientState(
            ...
            PostHandshakeAuthenticationNotRunning()
        )
    ]
```
///

/// html | div[style='clear: both;']
///

### 11.3.2. Exported Authenticators

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Because the exporter interface defined in this document is epoch-aware, the exporter secret used for an Exported Authenticator exchange is explicitly determined by the epoch selected by the application.

As a result, cross-flight exchanges of EKU and AuthenticatorRequest messages do not introduce cryptographic ambiguity. Therefore, no serialization requirement is imposed between EKU and Exported Authenticator exchanges.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///
