# [3.8. Variants](https://datatracker.ietf.org/doc/html/rfc8446#section-3.8)

/// html | div[style='float: left; width: 50%; padding: 5px;']
```title="RFC 8446"
Defined structures may have variants based on some knowledge that is
available within the environment.  The selector must be an enumerated
type that defines the possible variants the structure defines.  Each
arm of the select (below) specifies the type of that variant's field
and an optional field label.  The mechanism by which the variant is
selected at runtime is not prescribed by the presentation language.

    struct {
        T1 f1;
        T2 f2;
        ....
        Tn fn;
        select (E) {
            case e1: Te1 [[fe1]];
            case e2: Te2 [[fe2]];
            ....
            case en: Ten [[fen]];
        };
    } Tv;

For example:

    enum { apple(0), orange(1) } VariantTag;

    struct {
        uint16 number;
        opaque string<0..10>; /* variable length */
    } V1;

    struct {
        uint32 number;
        opaque string[10];    /* fixed length */
    } V2;

    struct {
        VariantTag type;
        select (VariantRecord.type) {
            case apple:  V1;
            case orange: V2;
        };
    } VariantRecord;
```
///

/// html | div[style='float: left; width: 50%; padding: 5px;']
Variants structures are modelled using integrated Tamarin macros which are then nested inside each other.
Taken the given example the macros in Tamarin could look like this.
```title="Tamarin"
VariantRecord(type, content) = <type, content>
Apple(number, string) = VariantRecord('0', <number, string>)
Orange(number, string) = VariantRecord('1', <number, string>)
```
///

/// html | div[style='clear: both;']
///