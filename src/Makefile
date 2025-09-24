TAMARIN = tamarin-prover +RTS -N16 -H75G -M150G -RTS
STATES = C0 S0 C1 S1 S1_retry C2d S2 C3 S3 C1_PSK C0_PSK S0_PSK S1_PSK_DHE S1_PSK C2d_PSK

reachability: $(STATES:%=../proofs/reachability.exists_%.spthy)

../proofs/reachability.exists_%.spthy: tls13.spthy
	$(TAMARIN) -Dreachability --heuristic=S --prove=exists_$* tls13.spthy --output=$@ >> ../logs/exists.log 2>&1

uniqueness:
	$(TAMARIN) -Duniqueness --heuristic=S --prove tls13.spthy --output=../proofs/uniqueness.spthy >> ../logs/uniqueness.log 2>&1

invariants:
	$(TAMARIN) -Dinvariants --heuristic=SC --prove=one_start_per_tid tls13.spthy --output=../proofs/invariants.one_start_per_tid.spthy >> ../logs/invariants.log 2>&1
	$(TAMARIN) -Dinvariants --heuristic=S --prove=tid_invariant tls13.spthy --output=../proofs/invariants.tid_invariant.spthy >> ../logs/invariants.log 2>&1

authHelpers:
	$(TAMARIN) -DauthHelpers --prove=matching_nonces tls13.spthy --heuristic=S --output=../proofs/auth_helpers.matching_nonces.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=matching_rms_nonces tls13.spthy --heuristic=S --output=../proofs/auth_helpers.matching_rms_nonces.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=consistent_nonces tls13.spthy --heuristic=S --output=../proofs/auth_helpers.consistent.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=invariant_nonces tls13.spthy --heuristic=S --output=../proofs/auth_helpers.invariant_nonces.spthy >> ../logs/auth_helpers.log 2>&1

dhInj:
	$(TAMARIN) -DdhInj --prove=dh_exp_invariant tls13.spthy --heuristic=C --output=../proofs/dh_inj.dh_exp_invariant.spthy >> ../logs/dh_inj.log 2>&1
	$(TAMARIN) -DdhInj --prove=one_dh_per_x tls13.spthy --heuristic=C --output=../proofs/dh_inj.one_dh_per_x.spthy >> ../logs/dh_inj.log 2>&1
	$(TAMARIN) -DdhInj --prove=rev_dh_ordering tls13.spthy --heuristic=C --output=../proofs/dh_inj.rev_dh_ordering.spthy >> ../logs/dh_inj.log 2>&1
	$(TAMARIN) -DdhInj --prove=rev_dh_before_hs tls13.spthy --heuristic=C --output=../proofs/dh_inj.rev_dh_before_hs.spthy >> ../logs/dh_inj.log 2>&1

dhCal:
	$(TAMARIN) -DdhCal --prove=dh_chal_dual --heuristic=cccccccccsssssssssssssssssssss --output=../proofs/dh_chal.spthy >> ../logs/dh_cal.log 2>&1