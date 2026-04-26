# Lessons Learned

## Reflection questions

- Which ports were open on `192.168.50.10`?
- Which services could Nmap identify confidently?
- Which version results were vague or uncertain?
- What is the difference between `-sV` and `-sC`?
- Why is it useful to save scan output with `-oN`?
- What risks would exist if these commands were run against a system you do not own?

## Notes

- Port numbers are hints, not proof. Service detection provides stronger evidence.
- Version banners can be incomplete, customized, or intentionally hidden.
- Focused scans are easier to read after initial discovery identifies open ports.
- Enumeration should stay within the explicit lab scope.
