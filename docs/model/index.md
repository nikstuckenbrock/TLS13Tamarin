# Model

The Multiset-Rewriting-Rules are split into several security protocol library files (`.splib`).

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

1. abc
2. ab
3. ab
4. Rules related to the default key update defined in [RFC 8446 Section 4.6.3](https://datatracker.ietf.org/doc/html/rfc8446#section-4.6.3).
5. ab
6. ab
7. ab
8. ab
9. ab
10. abc
11. abc