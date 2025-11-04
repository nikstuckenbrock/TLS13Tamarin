TAMARIN = tamarin-prover +RTS -N16 -H75G -M150G -RTS
STATES = C0 S0 C1 S1 S1_retry C2a C2b C2c C2d S2a S2b S2c S2d C3 S3 C1_PSK C0_PSK S0_PSK S1_PSK_DHE S1_PSK C2d_PSK S4_NST S4_update_recv S4_update_recv S4_update_req

reachability: $(STATES:%=../proofs/reachability.exists_%.spthy)

../proofs/reachability.exists_%.spthy: tls13.spthy
	$(TAMARIN) -Dreachability --prove=exists_$* tls13.spthy --output=$@ >> ../logs/exists.log 2>&1

uniqueness:
	$(TAMARIN) -Duniqueness --prove=one_C0_per_tid tls13.spthy --output=../proofs/uniqueness.one_C0_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C1_per_tid tls13.spthy --output=../proofs/uniqueness.one_C1_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C1_retry_per_tid tls13.spthy --output=../proofs/uniqueness.one_C1_retry_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S1_per_tid tls13.spthy --output=../proofs/uniqueness.one_S1_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S1_PSK_per_tid tls13.spthy --output=../proofs/uniqueness.one_S1_PSK_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S1_PSK_DHE_per_tid tls13.spthy --output=../proofs/uniqueness.one_S1_PSK_DHE_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C1_PSK_per_tid tls13.spthy --output=../proofs/uniqueness.one_C1_PSK_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C1_PSK_DHE_per_tid tls13.spthy --output=../proofs/uniqueness.one_C1_PSK_DHE_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2a_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2a_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2b_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2b_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2c_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2c_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2c_req_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2c_req_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2d_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2d_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S2d_PSK_per_tid tls13.spthy --output=../proofs/uniqueness.one_S2d_PSK_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2a_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2a_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2b_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2b_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2c_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2c_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2c_req_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2c_req_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2d_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2d_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C2d_PSK_per_tid tls13.spthy --output=../proofs/uniqueness.one_C2d_PSK_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C3_per_tid tls13.spthy --output=../proofs/uniqueness.one_C3_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_C3_cert_per_tid tls13.spthy --output=../proofs/uniqueness.one_C3_cert_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S3_per_tid tls13.spthy --output=../proofs/uniqueness.one_S3_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=one_S3_cert_per_tid tls13.spthy --output=../proofs/uniqueness.one_S3_cert_per_tid.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=S1_vs_S1_PSK_DHE tls13.spthy --output=../proofs/uniqueness.S1_vs_S1_PSK_DHE.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=S1_PSK_vs_S1_PSK_DHE tls13.spthy --output=../proofs/uniqueness.S1_PSK_vs_S1_PSK_DHE.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=S1_PSK_vs_S1 tls13.spthy --output=../proofs/uniqueness.S1_PSK_vs_S1.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=C1_vs_C1_PSK_DHE tls13.spthy --output=../proofs/uniqueness.C1_vs_C1_PSK_DHE.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=C1_PSK_vs_C1_PSK_DHE tls13.spthy --output=../proofs/uniqueness.C1_PSK_vs_C1_PSK_DHE.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=C1_PSK_vs_C1 tls13.spthy --output=../proofs/uniqueness.C1_PSK_vs_C1.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=S3_vs_S3_cert tls13.spthy --output=../proofs/uniqueness.S3_vs_S3_cert.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=C3_vs_C3_cert tls13.spthy --output=../proofs/uniqueness.C3_vs_C3_cert.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=S2d_vs_S2d_PSK tls13.spthy --output=../proofs/uniqueness.S2d_vs_S2d_PSK.spthy >> ../logs/uniqueness.log 2>&1
	$(TAMARIN) -Duniqueness --prove=C2d_vs_C2d_PSK tls13.spthy --output=../proofs/uniqueness.C2d_vs_C2d_PSK.spthy >> ../logs/uniqueness.log 2>&1

invariants:
	$(TAMARIN) -Dinvariants --prove=one_start_per_tid tls13.spthy --output=../proofs/invariants.one_start_per_tid.spthy >> ../logs/invariants.log 2>&1
	$(TAMARIN) -Dinvariants --prove=tid_invariant tls13.spthy --output=../proofs/invariants.tid_invariant.spthy >> ../logs/invariants.log 2>&1

authHelpers:
	$(TAMARIN) -DauthHelpers --prove=matching_nonces tls13.spthy --output=../proofs/auth_helpers.matching_nonces.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=matching_rms_nonces tls13.spthy --output=../proofs/auth_helpers.matching_rms_nonces.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=consistent_nonces tls13.spthy --output=../proofs/auth_helpers.consistent.spthy >> ../logs/auth_helpers.log 2>&1
	$(TAMARIN) -DauthHelpers --prove=invariant_nonces tls13.spthy --output=../proofs/auth_helpers.invariant_nonces.spthy >> ../logs/auth_helpers.log 2>&1

dhInj:
	$(TAMARIN) -DdhInj --prove=dh_exp_invariant tls13.spthy --output=../proofs/dh_inj.dh_exp_invariant.spthy >> ../logs/dh_inj.log 2>&1
	$(TAMARIN) -DdhInj --prove=one_dh_per_x tls13.spthy --output=../proofs/dh_inj.one_dh_per_x.spthy >> ../logs/dh_inj.log 2>&1
	#not_working_anymore$(TAMARIN) -DdhInj --prove=rev_dh_ordering tls13.spthy --output=../proofs/dh_inj.rev_dh_ordering.spthy >> ../logs/dh_inj.log 2>&1
	#not_working_anymore$(TAMARIN) -DdhInj --prove=rev_dh_before_hs tls13.spthy --output=../proofs/dh_inj.rev_dh_before_hs.spthy >> ../logs/dh_inj.log 2>&1

dhCal:
	$(TAMARIN) -DdhCal --prove=dh_chal_dual tls13.spthy --output=../proofs/dh_chal.spthy >> ../logs/dh_cal.log 2>&1

secretHelpers:
	$(TAMARIN) -DsecretHelpers --prove=ku_extract tls13.spthy --output=../proofs/secret_helpers.ku_extract.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=ku_expand tls13.spthy --output=../proofs/secret_helpers.ku_expand.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=ku_hs tls13.spthy --output=../proofs/secret_helpers.ku_hs.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=ku_ltk tls13.spthy --output=../proofs/secret_helpers.ku_ltk.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=ku_fresh_psk tls13.spthy --output=../proofs/secret_helpers.ku_fresh_psk.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=hsms_derive tls13.spthy --output=../proofs/secret_helpers.hsms_derive.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=sig_origin tls13.spthy --output=../proofs/secret_helpers.sig_origin.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=posths_rms tls13.spthy --output=../proofs/secret_helpers.posths_rms.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=posths_rms_weak tls13.spthy --output=../proofs/secret_helpers.posths_rms_weak.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=matching_rms_posths tls13.spthy --output=../proofs/secret_helpers.matching_rms_posths.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=matching_transcripts_posths tls13.spthy --output=../proofs/secret_helpers.matching_transcripts_posths.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=matching_rms_actors tls13.spthy --output=../proofs/secret_helpers.matching_rms_actors.spthy >> ../logs/secret_helpers.log 2>&1
	$(TAMARIN) -DsecretHelpers --prove=matching_sessions tls13.spthy --output=../proofs/secret_helpers.matching_sessions.spthy >> ../logs/secret_helpers.log 2>&1

lemmata:
	$(TAMARIN) -Dlemmas --prove=secret_session_keys tls13.spthy --output=../proofs/lemmas.secret_session_keys.spthy >> ../logs/lemmas.log 2>&1
	$(TAMARIN) -Dlemmas --prove=unique_session_keys tls13.spthy --output=../proofs/lemmas.unique_session_keys.spthy >> ../logs/lemmas.log 2>&1
