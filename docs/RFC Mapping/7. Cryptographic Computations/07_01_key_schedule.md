# [7.1. Key Schedule](https://datatracker.ietf.org/doc/html/rfc8446#section-7.1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
The key derivation process makes use of the HKDF-Extract and
HKDF-Expand functions as defined for HKDF [RFC5869], as well as the
functions defined below:

    HKDF-Expand-Label(Secret, Label, Context, Length) =
        HKDF-Expand(Secret, HkdfLabel, Length)

    Where HkdfLabel is specified as:

    struct {
        uint16 length = Length;
        opaque label<7..255> = "tls13 " + Label;
        opaque context<0..255> = Context;
    } HkdfLabel;

    Derive-Secret(Secret, Label, Messages) =
        HKDF-Expand-Label(Secret, Label,
                            Transcript-Hash(Messages), Hash.length)
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
To map the Derive-Secret function described above and all dependencies, two [functions](https://tamarin-prover.com/manual/master/book/004_cryptographic-messages.html) are defined in Tamarin: Expand and Extract.

```
functions: Expand/3, Extract/2
```
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
            0
            |
            v
PSK ->  HKDF-Extract = Early Secret
            |
            +-----> Derive-Secret(., "ext binder" | "res binder", "")
            |                     = binder_key
            |
            +-----> Derive-Secret(., "c e traffic", ClientHello)
            |                     = client_early_traffic_secret
            |
            +-----> Derive-Secret(., "e exp master", ClientHello)
            |                     = early_exporter_master_secret
            v
    Derive-Secret(., "derived", "")
            |
            v
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
# rule client_hello
earlySecret = Extract('0', '0')

# rule client_hello_psk
es = Extract(res_psk, '0')
```
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
(EC)DHE -> HKDF-Extract = Handshake Secret
            |
            +-----> Derive-Secret(., "c hs traffic",
            |                     ClientHello...ServerHello)
            |                     = client_handshake_traffic_secret
            |
            +-----> Derive-Secret(., "s hs traffic",
            |                     ClientHello...ServerHello)
            |                     = server_handshake_traffic_secret
            v
    Derive-Secret(., "derived", "")
            |
            v
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
# rule client_gen_keys
handshakeSecret = Extract(p_gxy, p_es)
```
///

/// html | div[style='clear: both;']
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
0 -> HKDF-Extract = Master Secret
            |
            +-----> Derive-Secret(., "c ap traffic",
            |                     ClientHello...server Finished)
            |                     = client_application_traffic_secret_0
            |
            +-----> Derive-Secret(., "s ap traffic",
            |                     ClientHello...server Finished)
            |                     = server_application_traffic_secret_0
            |
            +-----> Derive-Secret(., "exp master",
            |                     ClientHello...server Finished)
            |                     = exporter_master_secret
            |
            +-----> Derive-Secret(., "res master",
                                ClientHello...client Finished)
                                = resumption_master_secret
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
///

/// html | div[style='clear: both;']
///