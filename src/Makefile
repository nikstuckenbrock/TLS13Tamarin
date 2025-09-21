TAMARIN = tamarin-prover +RTS -N16 -H75G -M150G -RTS
STATES = C0 S0 C1 S1 C2a S2a S2b

reachability: $(STATES:%=../proofs/reachability.exists_%.spthy)

../proofs/reachability.exists_%.spthy: tls13.spthy
	$(TAMARIN) -Dreachability --heuristic=S --prove=exists_$* tls13.spthy --output=$@

uniqueness:
	$(TAMARIN) -Duniqueness --heuristic=S --prove tls13.spthy --output=../proofs/uniqueness.spthy

invariants:
	$(TAMARIN) -Dinvariants --heuristic=SC --prove=one_start_per_tid tls13.spthy --output=../proofs/invariants.one_start_per_tid.spthy
	$(TAMARIN) -Dinvariants --heuristic=S --prove=tid tls13.spthy --output=../proofs/invariants.tid.spthy