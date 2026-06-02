# 12. Security Considerations

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
his section discusses additional security and operational aspects introduced by the Extended Key Update mechanism. All security considerations of TLS 1.3 [TLS] and DTLS 1.3 [DTLS] continue to apply.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
///

/// html | div[style='clear: both;']
///

## 12.1. Scope of Key Compromise

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 12.2. Post-Compromise Security

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Extended Key Update provides post-compromise security for long-lived TLS sessions. To ensure post-compromise security guarantees:

*   Each update MUST use freshly generated ephemeral key-exchange material. Implementations MUST NOT reuse ephemeral key-exchange material across updates or across TLS sessions.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 12.3. Denial-of-Service (DoS)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
The Extended Key Update mechanism increases computational and state-management overhead. A malicious peer could attempt to exhaust CPU or memory resources by initiating excessive update requests.

Implementations SHOULD apply the following mitigations:

*   Limit the frequency of accepted Extended Key Update requests per session.

*   A peer that has sent an Extended Key Update MUST NOT initiate another until the previous update completes. If a peer violates this rule, the receiving peer MUST treat it as a protocol violation, send an "unexpected_message" alert, and terminate the connection.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## 12.4. Operational Guidance

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Deployments SHOULD evaluate Extended Key Update performance under load and fault conditions, such as high-frequency or concurrent updates. TLS policies SHOULD define explicit rate limits that balance post-compromise security benefits against potential DoS exposure.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///