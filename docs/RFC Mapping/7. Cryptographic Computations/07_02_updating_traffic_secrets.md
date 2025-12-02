# [7.2. Updating Traffic Secrets](https://datatracker.ietf.org/doc/html/rfc8446#section-7.2)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Once the handshake is complete, it is possible for either side to
update its sending traffic keys using the KeyUpdate handshake message
defined in Section 4.6.3.  The next generation of traffic keys is
computed by generating client_/server_application_traffic_secret_N+1
from client_/server_application_traffic_secret_N as described in this
section and then re-deriving the traffic keys as described in
Section 7.3.

The next-generation application_traffic_secret is computed as:

    application_traffic_secret_N+1 =
        HKDF-Expand-Label(application_traffic_secret_N,
                            "traffic upd", "", Hash.length)

Once client_/server_application_traffic_secret_N+1 and its associated
traffic keys have been computed, implementations SHOULD delete
client_/server_application_traffic_secret_N and its associated
traffic keys.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="keyUpdate.splib"
sats = Expand(p_sats, <'ats', '0'>, '32')
cats = Expand(p_cats, <'ats', '0'>, '32')
```
The traffic key update for the key update mentioned [here](./../../model/key_update.md) or in [section 4.6.3](./../4.%20Handshake%20Protocol/04_06_post_handshake_messages.md).
`p_sats` and `p_cats` are the corresponding `application_traffic_secret_N` and `cats` and `sats` are the corresponding `application_traffic_secret_N+1`.
///

/// html | div[style='clear: both;']
///