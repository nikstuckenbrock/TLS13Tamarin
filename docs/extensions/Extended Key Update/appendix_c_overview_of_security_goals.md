# Apendix C. Overview of Security Goals

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
A complete security analysis of the EKU is outside the scope of this document. This appendix provides an informal description of the primary security goals that EKU is designed to achieve.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
///

/// html | div[style='clear: both;']
///

## C.1. Post-Compromise Security (PCS)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Extended Key Update supports post-compromise security under the assumptions described in Section 12.1. If an attacker temporarily compromises an endpoint and obtains the traffic keys in use before an Extended Key Update takes place, but the compromise does not persist after the EKU completes, the attacker cannot derive the new keying material established by EKU. This property follows from the use of fresh ephemeral key exchange material during each Extended Key Update, which produces new traffic keys that are independent of the previous ones. This property provides only best-effort post-compromise security, as it assumes the attacker is not acting as a MiTM during the Extended Key Update.

As a result, confidentiality of application data encrypted after the Extended Key Update is preserved even if the earlier traffic keys were exposed.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## C.2. Key Freshness and Cryptographic Independence

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Each Extended Key Update derives new traffic keys from ephemeral key exchange material. This ensures strong separation between successive traffic keys:

*   The new traffic keys established by an Extended Key Update are independent of the previous traffic keys.

*   Compromise of one of traffic keys does not allow recovery of any earlier or later traffic keys.

*   Application data protected under one of the traffic keys cannot be decrypted using keys from another.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## C.3. Elimination of Standard KeyUpdate

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
Once Extended Key Update has been negotiated for a session, peers rely exclusively on EKU rather than the standard TLS 1.3 KeyUpdate mechanism. Relying solely on Extended Key Update helps maintain PCS properties throughout the lifetime of the TLS session.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///

## C.4. Detecting Divergent Key State

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="Draft"
As described in Section 11, both Post-handshake Certificate-Based Client Authentication and Exported Authenticators can be used after an Extended Key Update to confirm that both endpoints derived the same traffic keys. Because the authentication messages produced by these mechanisms depend on values derived from the updated traffic keys, any divergence in those traffic keys causes validation to fail, revealing interference by an active attacker.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///