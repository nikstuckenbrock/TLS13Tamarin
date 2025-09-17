TAMARIN=tamarin-prover +RTS -N16 -H75G -M150G -RTS

reachability:
	$(TAMARIN) -Dreachability --heuristic=S --prove tls13.spthy --output=../proofs/reachability.spthy

uniqueness:
	$(TAMARIN) -Duniqueness --heuristic=S --prove tls13.spthy --output=../proofs/uniqueness.spthy

invariants:
	$(TAMARIN) -Done_start_per_id --heuristic=SC --prove=one_start_per_tid tls13.spthy --output=../proofs/one_start_per_tid.spthy