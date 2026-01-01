# Out of band PSK

For the establishment of a out of band PSK the rule `out_of_band_psk` is used.
It only uses fresh facts as a premise so it can be instantiated at any time.
To indicate out of band usage the authentication status for both peers is set to a constant string of `oob_auth`.

```title="src/model/publicKeyInfrastructure.splib"
rule out_of_band_psk:
    let
        auth_status = <'oob_auth', 'oob_auth'>
        sessionTicket = <'4', $ticket_lifetime, ~ticket_age_add, ~ticket, <<'46', $max_early_data_size>>>
    in
    [
        Fr(~ticket),
        Fr(~res_psk),
        Fr(~ticket_age_add)
    ]
    --[
        GenPSK($S, 'server'),
        GenPSK($C, 'client'),
        FreshPSK(~ticket, ~res_psk)
    ]->
    [
        !ClientPSK($C, $S, ~res_psk, auth_status, sessionTicket, 'ext'),
        !ServerPSK($S, $C, ~res_psk, auth_status, sessionTicket, 'ext'),
        F_SecretPSK($S, ~res_psk),
        F_SecretPSK($C, ~res_psk)
    ]
```