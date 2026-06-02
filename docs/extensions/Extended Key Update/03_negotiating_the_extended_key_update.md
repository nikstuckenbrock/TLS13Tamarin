# 3. Negotiating the Extended Key Update

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Draft
```title="Draft"
Client and servers use the TLS flags extension [TLS-FLAGS] to indicate support for the functionality defined in this document. We call this flag "Extended_Key_Update" flag.

The "Extended_Key_Update" flag proposed by the client in the ClientHello (CH) MUST be acknowledged in the EncryptedExtensions (EE), if the server also supports the functionality defined in this document and is configured to use it.

If the "Extended_Key_Update" flag is not set, servers ignore any of the functionality specified in this document and applications that require post-compromise security will have to initiate a full handshake.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
# Tamarin Model
Negotiation of the Extended Key Update extension is not modelled at the moment.
Nontheless, the extension will be part of the `ClientHello` and `ServerHello` message structures, to indicate that both parties support and want to use it.
///

/// html | div[style='clear: both;']
///