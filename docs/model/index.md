# Model

The multiset rewriting rules defining the protocol model are split into several security protocol library files (`.splib`).

```python
📦TLS13Tamarin
 ┗ 📂src
   ┗ 📂model
     ┣ 📜client.splib # (1)
     ┣ 📜clientPsk.splib # (2)
     ┣ 📜earlyData.splib # (3)
     ┣ 📜keyUpdate.splib # (4)
     ┣ 📜macros.splib # (5)
     ┣ 📜postHandshake.splib # (6)
     ┣ 📜publicKeyInfrastructure.splib # (7)
     ┣ 📜record.splib # (8)
     ┣ 📜reveal.splib # (9)
     ┣ 📜server.splib # (10)
     ┗ 📜serverPsk.splib # (11)
```

1. General client related rule for sending and receiving (e.g. `ClientHello` ...).
2. Client rules regarding the PSK mode.
3. ab
4. Rules related to the default key update defined in [RFC 8446 Section 4.6.3](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.3). [More](./key_update.md)
5. ab
6. ab
7. Contains the rules dictating the public-key infrastructure. [More](./public_key_infrastructure.md)
8. ab
9. ab
10. abc
11. abc