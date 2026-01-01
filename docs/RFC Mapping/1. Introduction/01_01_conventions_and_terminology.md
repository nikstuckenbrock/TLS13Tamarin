# [1.1. Conventions and Terminology](https://datatracker.ietf.org/doc/html/rfc8446#section-1.1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all
capitals, as shown here.

The following terms are used:

client:  The endpoint initiating the TLS connection.

connection:  A transport-layer connection between two endpoints.

endpoint:  Either the client or server of the connection.

handshake:  An initial negotiation between client and server that
    establishes the parameters of their subsequent interactions
    within TLS.

peer:  An endpoint.  When discussing a particular endpoint, "peer"
    refers to the endpoint that is not the primary subject of
    discussion.

receiver:  An endpoint that is receiving records.

sender:  An endpoint that is transmitting records.

server:  The endpoint that did not initiate the TLS connection.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The defined conventions and terminology are also valid for the model.
The terms `client` and `server` are frequently used in the context of the model.
///

/// html | div[style='clear: both;']
///