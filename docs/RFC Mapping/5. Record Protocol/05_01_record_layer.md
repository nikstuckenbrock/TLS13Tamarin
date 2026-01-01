# [5.1. Record Layer](https://datatracker.ietf.org/doc/html/rfc8446#section-5.1)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
enum {
    invalid(0),
    change_cipher_spec(20),
    alert(21),
    handshake(22),
    application_data(23),
    (255)
} ContentType;

struct {
    ContentType type;
    ProtocolVersion legacy_record_version;
    uint16 length;
    opaque fragment[TLSPlaintext.length];
} TLSPlaintext;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/macros.splib"
DataRecord(data) = <data, '23'>
```
///

/// html | div[style='clear: both;']
///

Sending and receiving data is modelled by sending and receiving some fresh term `~data`.
The keys used for encryption are stored in the `SendStream` and `RecvStream` facts which are introduced [here]().

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/record.splib"
rule send:
    [
        SendStream(~tid, $actor, $peer, auth_status, app_key_out),
        Fr(~data)
    ]
    --[
        Send(~tid),
        SendData(~tid, $actor, $peer, auth_status, ~data)
    ]->
    [
        SendStream(~tid, $actor, $peer, auth_status, app_key_out),
        MessageOut(senc{DataRecord(~data)}app_key_out)
    ]
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="src/model/record.splib"
rule recv:
    [
        RecvStream(~tid, $actor, $peer, auth_status, app_key_in),
        F_MessageIn(senc{DataRecord(data)}app_key_in)
    ]
    --[
        Recv(~tid),
        RecvData(~tid, $actor, $peer, auth_status, data)
    ]->
    [
      RecvStream(~tid, $actor, $peer, auth_status, app_key_in)
    ]
```
///

/// html | div[style='clear: both;']
///