# Cleanup

## Cleanup steps

1. Stop any scans that are still running in Kali.
2. Review the files under `results/logs/` and remove any accidental non-lab data before committing results.
3. Shut down the owned Linux target VM if it is no longer needed.
4. Shut down Kali if the lab session is complete.
5. Return the isolated lab network to its normal state.

## Validation

No Nmap processes are still running:

```bash
pgrep -a nmap
```

If the command prints nothing, no Nmap process is running.

The lab target remains unchanged. This lab does not require login, exploitation, file uploads, or configuration changes.
