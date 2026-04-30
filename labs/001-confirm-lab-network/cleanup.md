# Cleanup

## Cleanup steps

1. Stop any `ping` command that is still running by pressing `Ctrl+C` in that terminal.
2. Save any useful command output under `results/logs/`.
3. Remove accidental non-lab data from `results.md` or `results/logs/`.
4. Keep the static IP assignments in place. They are intentional and will be used by later labs.
5. Shut down the Kali VM or Raspberry Pi only if your normal lab workflow calls for it.

## Validation

No cleanup command should be needed on the lab devices. This lab only sends basic ICMP traffic and reads local network state.

If a device could not reach another device, keep the failed result in `results.md`. Do not hide failures by changing live settings during this lab.
