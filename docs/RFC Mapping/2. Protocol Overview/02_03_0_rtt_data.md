# [2.3. 0-RTT Data](https://datatracker.ietf.org/doc/html/rfc8446#section-2.3)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
When clients and servers share a PSK (either obtained externally or
via a previous handshake), TLS 1.3 allows clients to send data on the
first flight ("early data").  The client uses the PSK to authenticate
the server and to encrypt the early data.

As shown in Figure 4, the 0-RTT data is just added to the 1-RTT
handshake in the first flight.  The rest of the handshake uses the
same messages as for a 1-RTT handshake with PSK resumption.

        Client                                               Server

        ClientHello
        + early_data
        + key_share*
        + psk_key_exchange_modes
        + pre_shared_key
        (Application Data*)     -------->
                                                        ServerHello
                                                + pre_shared_key
                                                    + key_share*
                                            {EncryptedExtensions}
                                                    + early_data*
                                                        {Finished}
                                <--------       [Application Data*]
        (EndOfEarlyData)
        {Finished}              -------->
        [Application Data]      <------->        [Application Data]

            +  Indicates noteworthy extensions sent in the
                previously noted message.

            *  Indicates optional or situation-dependent
                messages/extensions that are not always sent.

            () Indicates messages protected using keys
                derived from a client_early_traffic_secret.

            {} Indicates messages protected using keys
                derived from a [sender]_handshake_traffic_secret.

            [] Indicates messages protected using keys
                derived from [sender]_application_traffic_secret_N.

            Figure 4: Message Flow for a 0-RTT Handshake
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///