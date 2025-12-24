# TLS 1.3 Tamarin Model

This site serves a description of the Tamarin Prover TLS 1.3 model.
The model has already undergone several revisions of TLS and is now at the level of [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) (with a few restrictions).
You can find a brief overview of the models history also including some forks and variants of the model in the [history](./history/index.md) section.
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
- [ ] 3.6.Constructed Types
- [x] 3.7.Constants
- [ ] 3.8.Variants
- [ ] 4.Handshake Protocol
- [ ] 4.1.Key Exchange Messages
- [ ] 4.1.1.Cryptographic Negotiation
- [ ] 4.1.2.Client Hello
- [ ] 4.1.3.Server Hello
- [ ] 4.1.4.Hello Retry Request
- [ ] 4.2.Extensions
- [ ] 4.2.1.Supported Versions
- [ ] 4.2.2.Cookie
- [ ] 4.2.3.Signature Algorithms
- [ ] 4.2.4.Certificate Authorities
- [ ] 4.2.5.OID Filters
- [ ] 4.2.6.Post-Handshake Client Authentication
- [ ] 4.2.7.Supported Groups
- [ ] 4.2.8.Key Share
- [ ] 4.2.8.1.Diffie-Hellman Parameters
- [ ] 4.2.8.2.ECDHE Parameters
- [ ] 4.2.9.Pre-Shared Key Exchange Modes
- [ ] 4.2.10.Early Data Indication
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
- [ ] 4.5.End of Early Data
- [ ] 4.6.Post-Handshake Messages
- [ ] 4.6.1.New Session Ticket Message
- [ ] 4.6.2.Post-Handshake Authentication
- [ ] 4.6.3.Key and Initialization Vector Update
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
- [ ] 9.Compliance Requirements
- [ ] 9.1.Mandatory-to-Implement Cipher Suites
- [ ] 9.2.Mandatory-to-Implement Extensions
- [ ] 9.3.Protocol Invariants
- [ ] 10.Security Considerations
- [x] 11.IANA Considerations
- [x] 12.References
- [x] 12.1.Normative References
- [x] 12.2.Informative References
- [ ] A.State Machine
- [ ] A.1.Client
- [ ] A.2.Server
- [ ] B.Protocol Data Structures and Constant Values
- [ ] B.1.Record Layer
- [x] B.2.Alert Messages
- [ ] B.3.Handshake Protocol
- [ ] B.3.1.Key Exchange Messages
- [ ] B.3.1.1.Version Extension
- [ ] B.3.1.2.Cookie Extension
- [ ] B.3.1.3.Signature Algorithm Extension
- [ ] B.3.1.4.Supported Groups Extension
- [ ] B.3.2.Server Parameters Messages
- [ ] B.3.3.Authentication Messages
- [ ] B.3.4.Ticket Establishment
- [ ] B.3.5.Updating Keys
- [ ] B.4.Cipher Suites
- [ ] C.Implementation Notes
- [ ] C.1.Random Number Generation and Seeding
- [ ] C.2.Certificates and Authentication
- [ ] C.3.Implementation Pitfalls
- [ ] C.4.Client Tracking Prevention
- [ ] C.5.Unauthenticated Operation
- [x] D.Backward Compatibility
- [x] D.1.Negotiating with an Older Server
- [x] D.2.Negotiating with an Older Client
- [x] D.3.0-RTT Backward Compatibility
- [x] D.4.Middlebox Compatibility Mode
- [x] D.5.Security Restrictions Related to Backward Compatibility
- [ ] E.Overview of Security Properties
- [ ] E.1.Handshake
- [ ] E.1.1.Key Derivation and HKDF
- [ ] E.1.2.Client Authentication
- [ ] E.1.3.0-RTT
- [ ] E.1.4.Exporter Independence
- [ ] E.1.5.Post-Compromise Security
- [ ] E.1.6.External References
- [ ] E.2.Record Layer
- [ ] E.2.1.External References
- [ ] E.3.Traffic Analysis
- [ ] E.4.Side-Channel Attacks
- [ ] E.5.Replay Attacks on 0-RTT
- [ ] E.5.1.Replay and Exporters
- [ ] E.6.PSK Identity Exposure
- [ ] E.7.Sharing PSKs
- [ ] E.8.Attacks on Static RSA