# TLS 1.3 Tamarin Model

!!! danger
    This site is still work in progress. Sections might not be finished or contain all relevant details.

This site serves a description of the Tamarin Prover TLS 1.3 model.
The model has already undergone several revisions of TLS and is now at the level of [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) (with a few restrictions).
You can find a brief overview of the models history also including some forks and variants of the model in the [history](./history/index.md) section.
This documentation is based on the documentation by Sam Scott which can be found [here](https://samscott89.github.io/TLS13_Tamarin).
The documentation is split into multiple sections:

<div class="grid cards" markdown>

-   :material-graph:{ .lg .middle } __Model__

    ---

    The model itself containing all necessary Multiset-Rewriting-Rules

    [:octicons-arrow-right-24: More](./model/index.md)

-   :material-security-network:{ .lg .middle } __Lemmas__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: More](./history/index.md)

- :material-history:{ .lg .middle } __History__

    ---

    Brief overview of older revisions of the model and some forks and variants.
    [:octicons-arrow-right-24: More](./history/index.md)

- :material-script-text:{ .lg .middle } __RFC Mapping__

    ---

    Annotated RFC 8446 to explain mapping to the model.
    [:octicons-arrow-right-24: More](./RFC%20Mapping/index.md)

</div>

- [x] 1.Introduction
- [x] 1.1.Conventions and Terminology
- [x] 1.2.Major Differences from TLS 1.2
- [x] 1.3.Updates Affecting TLS 1.2
- [ ] 2.Protocol Overview
- [ ] 2.1.Incorrect DHE Share
- [ ] 2.2.Resumption and Pre-Shared Key (PSK)
- [ ] 2.3.0-RTT Data
- [x] 3.Presentation Language
- [x] 3.1.Basic Block Size
- [x] 3.2.Miscellaneous
- [x] 3.3.Numbers
- [x] 3.4.Vectors
- [x] 3.5.Enumerateds
- [x] 3.6.Constructed Types
- [x] 3.7.Constants
- [x] 3.8.Variants
- [x] 4.Handshake Protocol
- [ ] 4.1.Key Exchange Messages
- [ ] 4.1.1.Cryptographic Negotiation
- [ ] 4.1.2.Client Hello
- [ ] 4.1.3.Server Hello
- [ ] 4.1.4.Hello Retry Request
- [x] 4.2.Extensions
- [x] 4.2.1.Supported Versions
- [x] 4.2.2.Cookie
- [x] 4.2.3.Signature Algorithms
- [x] 4.2.4.Certificate Authorities
- [x] 4.2.5.OID Filters
- [x] 4.2.6.Post-Handshake Client Authentication
- [x] 4.2.7.Supported Groups
- [x] 4.2.8.Key Share
- [x] 4.2.8.1.Diffie-Hellman Parameters
- [x] 4.2.8.2.ECDHE Parameters
- [x] 4.2.9.Pre-Shared Key Exchange Modes
- [x] 4.2.10.Early Data Indication
- [ ] 4.2.11.Pre-Shared Key Extension
- [ ] 4.2.11.1.Ticket Age
- [ ] 4.2.11.2.PSK Binder
- [ ] 4.2.11.3.Processing Order
- [ ] 4.3.Server Parameters
- [ ] 4.3.1.Encrypted Extensions
- [ ] 4.3.2.Certificate Request
- [ ] 4.4.Authentication Messages
- [ ] 4.4.1.The Transcript Hash
- [ ] 4.4.2.Certificate
- [ ] 4.4.2.1.OCSP Status and SCT Extensions
- [ ] 4.4.2.2.Server Certificate Selection
- [ ] 4.4.2.3.Client Certificate Selection
- [ ] 4.4.2.4.Receiving a Certificate Message
- [ ] 4.4.3.Certificate Verify
- [ ] 4.4.4.Finished
- [x] 4.5.End of Early Data
- [x] 4.6.Post-Handshake Messages
- [x] 4.6.1.New Session Ticket Message
- [x] 4.6.2.Post-Handshake Authentication
- [x] 4.6.3.Key and Initialization Vector Update
- [x] 5.Record Protocol
- [x] 5.1.Record Layer
- [x] 5.2.Record Payload Protection
- [x] 5.3.Per-Record Nonce
- [x] 5.4.Record Padding
- [x] 5.5.Limits on Key Usage
- [x] 6.Alert Protocol
- [x] 6.1.Closure Alerts
- [x] 6.2.Error Alerts
- [ ] 7.Cryptographic Computations
- [ ] 7.1.Key Schedule
- [ ] 7.2.Updating Traffic Secrets
- [ ] 7.3.Traffic Key Calculation
- [ ] 7.4.(EC)DHE Shared Secret Calculation
- [ ] 7.4.1.Finite Field Diffie-Hellman
- [ ] 7.4.2.Elliptic Curve Diffie-Hellman
- [ ] 7.5.Exporters
- [ ] 8.0-RTT and Anti-Replay
- [ ] 8.1.Single-Use Tickets
- [ ] 8.2.Client Hello Recording
- [ ] 8.3.Freshness Checks
- [x] 9.Compliance Requirements
- [x] 9.1.Mandatory-to-Implement Cipher Suites
- [x] 9.2.Mandatory-to-Implement Extensions
- [x] 9.3.Protocol Invariants
- [x] 10.Security Considerations
- [x] 11.IANA Considerations
- [x] 12.References
- [x] 12.1.Normative References
- [x] 12.2.Informative References
- [x] A.State Machine
- [x] A.1.Client
- [x] A.2.Server
- [x] B.Protocol Data Structures and Constant Values
- [x] B.1.Record Layer
- [x] B.2.Alert Messages
- [x] B.3.Handshake Protocol
- [x] B.3.1.Key Exchange Messages
- [x] B.3.1.1.Version Extension
- [x] B.3.1.2.Cookie Extension
- [x] B.3.1.3.Signature Algorithm Extension
- [x] B.3.1.4.Supported Groups Extension
- [x] B.3.2.Server Parameters Messages
- [x] B.3.3.Authentication Messages
- [x] B.3.4.Ticket Establishment
- [x] B.3.5.Updating Keys
- [x] B.4.Cipher Suites
- [x] C.Implementation Notes
- [x] C.1.Random Number Generation and Seeding
- [x] C.2.Certificates and Authentication
- [x] C.3.Implementation Pitfalls
- [x] C.4.Client Tracking Prevention
- [x] C.5.Unauthenticated Operation
- [x] D.Backward Compatibility
- [x] D.1.Negotiating with an Older Server
- [x] D.2.Negotiating with an Older Client
- [x] D.3.0-RTT Backward Compatibility
- [x] D.4.Middlebox Compatibility Mode
- [x] D.5.Security Restrictions Related to Backward Compatibility
- [x] E.Overview of Security Properties
- [x] E.1.Handshake
- [x] E.1.1.Key Derivation and HKDF
- [x] E.1.2.Client Authentication
- [x] E.1.3.0-RTT
- [x] E.1.4.Exporter Independence
- [x] E.1.5.Post-Compromise Security
- [x] E.1.6.External References
- [x] E.2.Record Layer
- [x] E.2.1.External References
- [x] E.3.Traffic Analysis
- [x] E.4.Side-Channel Attacks
- [x] E.5.Replay Attacks on 0-RTT
- [x] E.5.1.Replay and Exporters
- [x] E.6.PSK Identity Exposure
- [x] E.7.Sharing PSKs
- [x] E.8.Attacks on Static RSA