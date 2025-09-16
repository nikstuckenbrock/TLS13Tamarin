TAMARIN=tamarin-prover +RTS -N16 -H75G -M150G -RTS

reachability:
	$(TAMARIN) -Dreachability --heuristic=S --prove tls13.spthy --output=../proofs/reachability.spthy

uniqueness:
	$(TAMARIN) -Duniqueness --heuristic=S --prove tls13.spthy --output=../proofs/uniqueness.spthy