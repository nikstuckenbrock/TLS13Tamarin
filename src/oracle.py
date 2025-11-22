#!/usr/bin/env python3

import re
from sys import argv, stdin

def splitter(line):
    splitted = line.split(":")
    assert len(splitted) == 2
    return (splitted[0], splitted[1].strip())

def sub_token(token, line):
    (num, goal) = line
    if isinstance(token, str):
        return num if token in goal else None
    else:
        return num if token.search(goal) is not None else None

def match_against_list(priority_list, lines):
    for token in priority_list:
        try:
            return next(filter(bool, map(lambda line: sub_token(token, line), lines)))
        except StopIteration:
            pass

lines = list(map(splitter, stdin.readlines()))
if not lines:
    exit(0)

match = None
if argv[1].startswith("one_C") or (argv[1].startswith("C") and "vs" in argv[1]):
    match = match_against_list([
        "(#i < #j)  ∥ (#j < #i)",
        "ClientState"
    ], lines)
elif argv[1].startswith("one_S") or (argv[1].startswith("S") and "vs" in argv[1]):
    match = match_against_list([
        "(#i < #j)  ∥ (#j < #i)",
        "ServerState"
    ], lines)
elif argv[1].startswith("tid_invariant"):
    match = match_against_list([
        "last",
        "Instance",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "matching_nonces":
    match = match_against_list([
        "RNonces",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "matching_rms_nonces":
    match = match_against_list([
        "ClientState( ~tid, 'C3'",
        "!Ltk",
        "!Pk",
        "RRMS",
        "ServerState( ~tid.1, 'S3'",
        "ServerState( ~tid, 'S1'",
        "CNonces",
        "ClientState"
    ], lines)
elif argv[1] == "consistent_nonces":
    match = match_against_list([
        "CNonces",
        "RNonces",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "invariant_nonces":
    match = match_against_list([
        "(#i < #j)  ∥ (#j < #i)",
        "ClientState( ~tid, 'C1'",
        "RNonces",
        "ServerState( ~tid, 'S1'"
    ], lines)
elif argv[1].startswith("posths_rms"):
    match = match_against_list([
        "(#k < #i)  ∥ (#k = #i)",
        "last",
        "Instance",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1].startswith("hsms_"):
    match = match_against_list([
        "RHSMS",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "matching_rms_actors":
    match = match_against_list([
        "RRMS",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "matching_sessions":
    new_lines: list = []
    for line in lines:
        if "∀ tid tid2 actor actor2 role role2 peer peer2 rms" in line[1]:
            pass
        else:
            new_lines.append(line)
    match = match_against_list([
        "RRMS( tid",
        "ClientState( ~tid, 'C3'",
        "ServerState( ~tid.1, 'S3'",
        "ServerState( ~tid, 'S3'",
        "ClientState( ~tid.1, 'C3'",
        "RevealPSK",
        "RevDHExp",
        "F_SecretPSK",
        "(∃ #j."
    ], new_lines)
elif argv[1] == "secret_session_keys":
    match = match_against_list([
        "SessionKey",
        "Reveal",
        "F_SecretPSK",
        "ClientState",
        "ServerState"
    ], lines)
elif argv[1] == "matching_hsms":
    match = match_against_list([
        "CHS",
        "RHSMS",
        "RRMS",
        "ClientState( ~tid, 'C3'"
    ], lines)
elif argv[1] == "post_master_secret":
    match = match_against_list([
        "!Pk",
        "CHS",
        "RPostHS",
        "F_MessageIn(",
        "UseLtk",
        "!Ltk",
        re.compile(r"(?s).*RevDHExp.*RevDHExp.*RevealPSK.*RevealPSK.*")
    ], lines)
elif argv[1] == "entity_authentication":
    match = match_against_list([
        "∀ tid actor peer nonces cas #i.",
        "last(#i)",
        "CNonces(",
        re.compile(r"^\s*CIdentity\(\s*\~tid,"),
        "!Pk",
        "($S = $S.1)",
        "F_MessageIn",
        "∃ #j. (!KU( ~ltkS ) @ #j) ∧ #j < #vk)",
        "∃ #j.   (!KU( Expand(Extract('0'",
        "∃ #j.6.   (!KU( Extract('0',",
        "∃ #j",
        re.compile(r"^\s*F\_SecretPSK"),
        re.compile(r"(?s).*RevLtk.*RevDHExp.*RevDHExp.*RevealPSK.*RevealPSK.*"),
        "UseLtk",
        "!Ltk",
        "ClientState( ~tid, 'C2d'",
        "!KU( senc(<'20'", # may make problems before
        re.compile(r"(?s).*CIdentity.*CIdentityPost.*"),
        "ServerState( ~tid.1, 'S2d'"
    ], lines)
elif argv[1] == "injective_mutual_entity_authentication":
    match = match_against_list([
        "CNonces",
        "CIdentity",
        re.compile(r"(?s).*RevLtk.*RevDHExp.*RevDHExp.*RevealPSK.*RevealPSK.*.RNonces.*"),
        re.compile(r"(?s).*RevLtk.*RevDHExp.*RevDHExp.*RevealPSK.*RevealPSK.*.RTranscript.*")
    ], lines)
elif argv[1] == "secret_session_keys_pfs":
    match = match_against_list([
        "∃ #r.",
        "∃ #j.",
        "ClientState( ~tid, 'C3'",
        "ServerState( ~tid, 'S3'",
        "SessionKey("
        "RMode(",
        "F_SecretPSK( $A",
        "!Pk( $C, pk(~ltkC)"
    ], lines)
elif argv[1] == "dh_chal_dual":
    match = match_against_list([
        "DHChal( g, x",
        "Instance( tid.1, actor",
        "DHChal( $g, ~x",
        "Instance( tid2, actor2",
        "!KU( ~x",
        "!KU( ~y",
        "DH(",
        "ClientState( ~tid, 'C1'",
        "ServerState( ~tid.1, 'S1'",
        "!KU( $g^(~x*",
        "!KU( $g^(~y*",
        "!KU( ~ticket"
    ], lines)
elif argv[1] == "rev_dh_before_hs":
    match = match_against_list([
        "ServerState( ~tid, 'S1'",
    ], lines)
elif argv[1] == "invariant_post_hs":
    match = match_against_list([
        "RRMS",
    ], lines)
elif argv[1] == "handshake_secret":
    match = match_against_list([
        " CHS(",
        "RRMS(",
        "∃ #j.",
        " (∃ #r.",
        "CIdentity( ~tid",
        "ServerState( ~tid, 'S3'",
        "ServerState( ~tid, 'S2d'",
        "∃ aas2"
    ], lines)
elif argv[1] == "mutual_transcript_agreement":
    match = match_against_list([
    ], lines)
elif argv[1] == "auth_psk":
    match = match_against_list([
        "ClientState( ~tid, 'C3'",
        "ServerState( ~tid.1, 'S3'",
        "CIdentity",
        "RRMS"
    ], lines)

if match is not None:
    print(match)
