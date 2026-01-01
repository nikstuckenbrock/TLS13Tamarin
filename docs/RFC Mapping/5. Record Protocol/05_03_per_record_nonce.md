# [5.3. Per-Record Nonce](https://datatracker.ietf.org/doc/html/rfc8446#section-5.3)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
A 64-bit sequence number is maintained separately for reading and
writing records.  The appropriate sequence number is incremented by
one after reading or writing each record.  Each sequence number is
set to zero at the beginning of a connection and whenever the key is
changed; the first record transmitted under a particular traffic key
MUST use sequence number 0.
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
As explained in [section 5](./index.md) the modelling of the Record Protocol is quite coarse.
The Per-Record Nonce is not modelled at the moment.
///

/// html | div[style='clear: both;']
///