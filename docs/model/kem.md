# KEM

The KEM Tamarin library used for this analysis is based on the work of Cas Cremers, Alexander Dax, and Niklas Medinger [^1].

### How to implement

The module introduces the following action facts:
* Encaps(k, ct, pk)
* Decaps(pk, ct, pk, sk)
* GoodKey(pk)

[^1]: Cas Cremers, Alexander Dax, and Niklas Medinger. 2024. Keeping Up with the KEMs: Stronger Security Notions for KEMs and Automated Analysis of KEM-based Protocols. In Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security (CCS '24). Association for Computing Machinery, New York, NY, USA, 1046–1060. https://doi.org/10.1145/3658644.3670283