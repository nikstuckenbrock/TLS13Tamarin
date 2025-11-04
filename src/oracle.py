#!/usr/bin/env python3

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
    match = match_against_list([
        "RRMS",
        "ClientState",
        "ServerState",
        "RevealPSK",
        "RevDHExp",
        "F_SecretPSK"
    ], lines)
elif argv[1] == "secret_session_keys":
    match = match_against_list([
        "SessionKey",
        "Reveal",
        "F_SecretPSK",
        "ClientState",
        "ServerState"
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

if match is not None:
    print(match)

