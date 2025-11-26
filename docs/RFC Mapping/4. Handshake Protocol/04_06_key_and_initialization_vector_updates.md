# [4.6.3. Key and Initialization Vector Update](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.3)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```
enum {
    update_not_requested(0), update_requested(1), (255)
} KeyUpdateRequest;

struct {
    KeyUpdateRequest request_update;
} KeyUpdate;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
KeyUpdateUpdateNotRequested() = '0',
KeyUpdateUpdateRequested() = '1',
KeyUpdate(update_requested) = Handshake(HandshakeMessageTypeKeyUpdate(), <update_requested>),
///

/// html | div[style='clear: both;']
///