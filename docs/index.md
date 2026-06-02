# TLS 1.3 Tamarin Model

This site serves a description of the Tamarin Prover TLS 1.3 model.
The model has already undergone several revisions of TLS and is now at the level of [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446) (with a few restrictions).
You can find a brief overview of the models history also including some forks and variants of the model in the [history](./history/index.md) section.
This documentation is based on the documentation by Sam Scott which can be found [here](https://samscott89.github.io/TLS13_Tamarin).
The documentation is split into multiple sections:

<div class="grid cards" markdown>

-   :material-graph:{ .lg .middle } __Model__

    ---

    The model itself containing all necessary Multiset-Rewriting-Rules

    [:octicons-arrow-right-24: More](./model/index.md)

-   :material-security-network:{ .lg .middle } __Lemmas__

    ---

    Auxiliary lemmas and proven security properties

    [:octicons-arrow-right-24: More](./history/index.md)

- :material-history:{ .lg .middle } __History__

    ---

    Brief overview of older revisions of the model and some forks and variants.
    [:octicons-arrow-right-24: More](./history/index.md)

- :material-script-text:{ .lg .middle } __RFC Mapping__

    ---

    Annotated RFC 8446 to explain mapping to the model.
    [:octicons-arrow-right-24: More](./RFC%20Mapping/index.md)

- :material-puzzle:{ .lg .middle } __Extensions__

    ---

    Detailed description on the implementation of selected extensions
    [:octicons-arrow-right-24: More](./extensions/index.md)

</div>
