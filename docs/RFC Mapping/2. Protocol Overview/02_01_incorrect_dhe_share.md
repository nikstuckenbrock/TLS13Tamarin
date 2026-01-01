# [2.1. Incorrect DHE Share](https://datatracker.ietf.org/doc/html/rfc8446#section-2.1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
If the client has not provided a sufficient "key_share" extension
(e.g., it includes only DHE or ECDHE groups unacceptable to or
unsupported by the server), the server corrects the mismatch with a
HelloRetryRequest and the client needs to restart the handshake with
an appropriate "key_share" extension, as shown in Figure 2.  If no
common cryptographic parameters can be negotiated, the server MUST
abort the handshake with an appropriate alert.

      Client                                               Server

      ClientHello
      + key_share             -------->
                                                HelloRetryRequest
                              <--------               + key_share
      ClientHello
      + key_share             -------->
                                                      ServerHello
                                                      + key_share
                                             {EncryptedExtensions}
                                             {CertificateRequest*}
                                                   {Certificate*}
                                             {CertificateVerify*}
                                                      {Finished}
                              <--------       [Application Data*]
      {Certificate*}
      {CertificateVerify*}
      {Finished}              -------->
      [Application Data]      <------->        [Application Data]

            Figure 2: Message Flow for a Full Handshake with
                        Mismatched Parameters

Note: The handshake transcript incorporates the initial
ClientHello/HelloRetryRequest exchange; it is not reset with the
new ClientHello.

TLS also allows several optimized variants of the basic handshake, as
described in the following sections.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
The `HelloRetryRequest` mentioned in section 2.1. of the draft is actually a special `ServerHello` message which is defined in detail in [section 4.1.3.](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.3) of the RFC.
You can find details of the modelled HelloRetryRequest [here](./../../model/hello_retry_request.md).
///