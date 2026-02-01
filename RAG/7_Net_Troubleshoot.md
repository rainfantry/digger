
FIELD OPERATIONS MANUAL
Defensive Operations Guide for NETWORK TROUBLESHOOTING \& TESTING
CLASSIFICATION: PERSONAL USE ONLY
Operator: 22DIV / Callsign: Digger
Purpose: Extract and structure network troubleshooting methodologies, tools, and packet analysis techniques for rapid fault isolation, incident response, and defensive monitoring.

***

## **TABLE OF CONTENTS**

SECTION 1: I understand the methods used to troubleshoot a network.
SECTION 2: I can identify tools that may be helpful in troubleshooting a network.
SECTION 3: I understand what a test environment is and why it might be necessary.
SECTION 4: I understand the uses of Wireshark.
SECTION 5: I understand defensive troubleshooting and threat detection via network analysis (RECAP).

***

## SECTION 1: I understand the methods used to troubleshoot a network.

This section gives you structured approaches to isolate network faults quickly instead of random guessing. Troubleshooting is about eliminating variables systematically. The methods here are your mental frameworks for moving from "nothing works" to "fixed" or "attacker identified" with minimum wasted effort.

**Common troubleshooting methodologies:**

- **OSI bottom-up approach**: Start at Layer 1 (physical), verify each layer up to Layer 7 (application). Most issues are at L1-L3.
- **Top-down approach**: Start at application layer, work down. Use when app-specific issues are suspected.
- **Divide and conquer**: Test middle layers first (L3/L4), then binary search up or down based on results.
- **Follow the path**: Trace packet flow from source to destination; test each hop.
- **Spot the differences**: Compare working vs broken systems/configs to isolate the variable.
- **Swap components**: Replace suspected hardware/cables to confirm fault (physical troubleshooting).

**Standard troubleshooting sequence (OSI bottom-up):**

1. **Layer 1 (Physical)**: Cable plugged in? Link lights on? Correct cable type? Physical damage?
2. **Layer 2 (Data Link)**: Correct VLAN? MAC address learned? ARP table populated? Switch port enabled?
3. **Layer 3 (Network)**: Valid IP/mask/gateway? Can ping gateway? Routing table correct?
4. **Layer 4 (Transport)**: Correct ports open? Firewall blocking? TCP handshake completing?
5. **Layer 7 (Application)**: Service running? DNS resolving? Authentication working? App logs show errors?

**Defensive controls:**

- Always start with **OSI Layer 1-3** before assuming compromise; most "incidents" are misconfigurations.
- Document baseline behavior (normal latency, routes, open ports) so you can **spot deviations** quickly.
- Use **divide and conquer** during active incidents to isolate attacker position in network path.
- When troubleshooting in prod, assume **any change you make is visible to an attacker**; use test environments first.

***

## SECTION 2: I can identify tools that may be helpful in troubleshooting a network.

This section is your toolbox reference. Each tool targets specific layers and problems. Knowing which tool answers which question saves time and reveals attacker activity when behavior deviates from normal.

**Core command-line tools (cross-platform):**

- **ping**: Tests reachability (ICMP echo); measures RTT; confirms Layer 3 connectivity.
    - Usage: `ping 8.8.8.8`, `ping google.com`
    - Defensive use: Verify connectivity; detect packet loss; baseline latency.
- **traceroute / tracert**: Maps path to destination; shows each router hop and latency.
    - Usage: `traceroute 1.1.1.1` (Linux), `tracert 1.1.1.1` (Windows)
    - Defensive use: Identify where packets die; detect route hijacking or unexpected hops.
- **nslookup / dig**: Query DNS records; verify name resolution.
    - Usage: `nslookup google.com`, `dig google.com A`
    - Defensive use: Detect DNS poisoning; confirm correct IP resolution; check for malicious domains.
- **ipconfig / ifconfig / ip**: Display/configure network interfaces, IP, mask, gateway, DNS.
    - Usage: `ipconfig /all` (Windows), `ip a` (Linux), `ifconfig` (legacy Unix)
    - Defensive use: Verify correct addressing; detect rogue DHCP assignments; check for unexpected IPs.
- **netstat / ss**: Show active connections, listening ports, routing table.
    - Usage: `netstat -an`, `ss -tuln`
    - Defensive use: Identify suspicious connections; detect backdoors listening on unusual ports.
- **arp**: Display/modify ARP cache (IP-to-MAC mappings).
    - Usage: `arp -a`
    - Defensive use: Detect ARP poisoning (duplicate MACs, wrong gateway MAC).
- **route**: Display/modify routing table.
    - Usage: `route print` (Windows), `ip route` (Linux)
    - Defensive use: Detect route injection; verify default gateway.

**Advanced tools:**

- **nmap**: Port scanner; service/version detection; OS fingerprinting.
    - Defensive use: Audit open ports; detect unauthorized services; validate firewall rules.
- **tcpdump**: Packet capture at command line (Linux/Unix).
    - Defensive use: Capture traffic for offline analysis; detect anomalies in real time.
- **Wireshark**: GUI packet analyzer (covered in Section 4).

**Defensive controls:**

- Master the **five-step drill**: `ipconfig` → `ping gateway` → `ping 8.8.8.8` → `nslookup domain` → `traceroute`. Run it in under 60 seconds.
- Use `netstat/ss` + `arp` together to correlate **suspicious remote IPs with MAC addresses**; cross-reference with switch logs.
- Keep `nmap` output of your own network as a **known-good baseline**; diff against current scans to spot new services.
- When tools behave abnormally (ping works but traceroute fails; DNS resolves wrong), suspect **active interference or compromise**.

***

## SECTION 3: I understand what a test environment is and why it might be necessary.

This section explains why you never test destructive commands, risky configs, or exploit techniques in production. Test environments let you fail safely, validate changes, and rehearse incident response without breaking live systems or alerting attackers.

**What is a test environment?**

- Isolated network/system that mimics production topology, devices, and configs.
- Can be physical (separate hardware), virtual (VMs, containers), or simulated (Packet Tracer, GNS3).
- Allows safe testing of: config changes, firewall rules, routing updates, patches, exploits, and incident response procedures.

**Why test environments are necessary:**

- **Prevent production outages**: Test risky changes (new ACLs, routing, VLANs) before deploying.
- **Validate security controls**: Confirm firewall rules block what they should; test IDS/IPS detection.
- **Practice incident response**: Rehearse containment, forensics, and recovery without real consequences.
- **Develop exploits safely**: When pentesting, test payloads in a lab before using them on client networks.
- **Avoid tipping off attackers**: In compromised networks, testing detection tools in prod can alert adversaries.

**Types of test environments:**

- **Lab networks**: Physical or virtual; replicate prod topology at smaller scale.
- **Packet Tracer / GNS3**: Simulate routers, switches, firewalls for config testing.
- **Virtual machines**: Spin up target OSes (Windows, Linux) for exploit/tool testing.
- **Containers (Docker)**: Lightweight, fast, disposable environments for app/service testing.
- **Cloud sandboxes**: AWS/Azure test accounts isolated from production.

**Defensive controls:**

- **Mandatory rule**: Never test new firewall rules, route changes, or exploits in production first.
- Maintain a **minimal lab topology** that matches your prod network's key segments (DMZ, internal, management).
- Use snapshots/backups in test environments so you can **rapidly reset to known-good state** after destructive tests.
- When testing detection tools (IDS, EDR), run them in the lab first to **tune out false positives** before deploying to prod.
- During active incidents, if you need to test a containment action (e.g., blocking an IP), **replicate the scenario in a VM first** to confirm it won't break legitimate traffic.

***

## SECTION 4: I understand the uses of Wireshark.

Wireshark is your microscope for network traffic. This section covers what it does, when to use it, and how to extract defensive intelligence from packet captures. Mastering Wireshark turns invisible network behavior into evidence and indicators of compromise.

**What is Wireshark?**

- Open-source GUI packet analyzer (protocol analyzer, "sniffer").
- Captures and decodes traffic in real time or from saved `.pcap` files.
- Supports 1000+ protocols; decodes frames/packets/segments across all OSI layers.
- Cross-platform (Windows, Linux, macOS).

**Core uses of Wireshark:**

- **Troubleshooting**: See exactly what's on the wire when connectivity fails (malformed packets, retransmissions, resets).
- **Protocol analysis**: Understand how protocols behave; verify correct handshakes (TCP 3-way, TLS, DHCP DORA).
- **Security analysis**: Detect attacks (ARP spoofing, port scans, cleartext passwords, malware C2 beacons).
- **Forensics**: Reconstruct attacker actions from packet captures (what was exfiltrated, which hosts communicated).
- **Performance analysis**: Identify bottlenecks, latency sources, packet loss.

**Key Wireshark features:**

- **Capture filters**: Limit what's captured (e.g., `host 192.168.1.10`, `port 80`).
- **Display filters**: Filter captured data for analysis (e.g., `http`, `tcp.flags.syn==1`, `ip.addr==10.0.0.5`).
- **Follow streams**: Reconstruct full TCP/UDP conversations (right-click packet → Follow → TCP Stream).
- **Protocol hierarchy**: Summary of all protocols in capture.
- **Expert info**: Highlights warnings/errors (retransmissions, bad checksums).
- **Export objects**: Extract files transferred over HTTP, SMB, FTP.

**Common Wireshark workflows:**

1. **Verify connectivity**: Capture while running `ping`; confirm ICMP echo request/reply; check for packet loss.
2. **Analyze failed connections**: Filter `tcp.flags.reset==1` to find connection resets; check for `tcp.analysis.retransmission`.
3. **Detect ARP poisoning**: Filter `arp`; look for duplicate IPs with different MACs.
4. **Find cleartext credentials**: Filter `http.request.method==POST` or `ftp`; follow TCP stream to see passwords.
5. **Identify port scans**: Filter `tcp.flags.syn==1 and tcp.flags.ack==0`; look for many SYNs to different ports from one source.
6. **Spot DNS tunneling/exfil**: Filter `dns`; look for unusually long query names or high query volume to one domain.

**Defensive controls:**

- Use Wireshark to **baseline normal traffic** (capture 5 minutes of routine activity; note common protocols, ports, packet sizes).
- When investigating incidents, **capture at multiple points** (client, switch, firewall, server) to see where packets are altered or dropped.
- Always apply **display filters** before analysis; full captures are overwhelming—narrow to the protocol/host of interest.
- In live networks, use **capture filters** (`not port 22`) to avoid filling disk or capturing your own SSH session.
- Learn these **critical display filters** by heart:
    - `http.request` – all HTTP requests
    - `dns` – all DNS traffic
    - `tcp.flags.syn==1 and tcp.flags.ack==0` – SYN scans
    - `ip.addr==X.X.X.X` – all traffic to/from specific IP
    - `!(arp or icmp or dns)` – exclude noise protocols
- **Never capture in promiscuous mode on networks you don't own**; it's often illegal and always unethical without authorization.

***

## SECTION 5: I understand defensive troubleshooting and threat detection via network analysis (RECAP).

This final section ties troubleshooting methodology, tools, and Wireshark into a unified defensive workflow. The goal is to make troubleshooting simultaneously a **fault-finding process** and a **threat-hunting opportunity**. When you troubleshoot, you should always be asking: "Is this a failure, or is this an attacker?"

**Unified defensive troubleshooting checklist:**

1. **Gather symptoms**: What broke? When? What changed? Who/what is affected?
2. **Check physical/link (L1-L2)**: Cables, link lights, switch ports, VLANs, ARP cache.
3. **Check network/transport (L3-L4)**: IP config, routing, firewall rules, open ports (`ipconfig`, `ping`, `traceroute`, `netstat`).
4. **Check application/DNS (L7)**: Service status, DNS resolution, logs (`nslookup`, service status).
5. **Capture traffic if still unclear**: Use `tcpdump` or Wireshark; filter to the affected host/service.
6. **Analyze for both failure and attack**: Look for misconfigs AND suspicious patterns (scans, spoofing, unusual protocols).

**Threat indicators to watch for during troubleshooting:**

- **ARP cache anomalies**: Gateway MAC changes or duplicates → ARP poisoning.
- **Unexpected routes**: New routes in routing table → route injection or compromise.
- **Unusual open ports**: `netstat` shows listening ports you didn't configure → backdoor.
- **DNS resolution to wrong IPs**: `nslookup` returns unexpected address → DNS poisoning or malicious DNS server.
- **Traceroute path changes**: Packets routing through unexpected hops → BGP hijack or MITM.
- **High volume of SYN packets**: Wireshark shows many SYNs, few ACKs → SYN flood or port scan.
- **Cleartext credentials in captures**: Passwords visible in HTTP/FTP/Telnet → attacker may have sniffed them too.
- **DNS queries to weird domains**: Long, random subdomains or high frequency → DNS tunneling/C2.
- **Retransmissions and resets**: Excessive `tcp.analysis.retransmission` → network attack (RST injection, jamming) or overload.

**Port and service focus (integrated into troubleshooting):**

When troubleshooting connectivity to a service, immediately map the port to its attack profile:

- **22 (SSH)**: Check auth logs for brute-force; verify key-based auth enabled.
- **80/443 (HTTP/HTTPS)**: Capture with Wireshark; check for SQLi, XSS payloads in URLs; verify HTTPS cert is valid.
- **53 (DNS)**: Monitor query volume and query names; detect tunneling or DGA domains.
- **445 (SMB)**: High-risk; if connectivity issues coincide with this port, check for ransomware/worm activity.
- **3389 (RDP)**: Failed connections here often indicate brute-force; check firewall logs and auth attempts.

**Defensive workflow (troubleshooting + threat hunting combined):**

1. Run the **five-step drill** (`ipconfig` → `ping gateway` → `ping 8.8.8.8` → `nslookup` → `traceroute`).
2. Check `netstat -an` and `arp -a` for **unexpected connections or MACs**.
3. If issue persists, start **Wireshark capture** with capture filter `host [affected_IP]`.
4. Apply **display filters** to isolate the failing protocol (e.g., `http`, `dns`, `tcp.port==443`).
5. Look for **both technical failures and attack patterns** in the same capture:
    - Failures: RSTs, retransmissions, malformed packets, no responses.
    - Attacks: Scans (many SYNs), spoofing (wrong MACs/IPs), exfil (large outbound transfers), C2 (beaconing to single external IP).
6. Cross-reference Wireshark findings with **logs** (firewall, IDS, DNS, auth) to confirm hypothesis.
7. If attack confirmed, **shift to incident response**: isolate affected host, preserve capture as evidence, escalate.

**Final operational mantra:**

> "Every troubleshooting session is a threat-hunting session. Fix the problem, but also ask: could an attacker cause this? Am I seeing normal failure or active interference?"

**Defensive controls (final recap):**

- Maintain **known-good baselines** (normal routes, ARP cache, open ports, DNS servers) so deviations are obvious.
- **Capture first, filter later**: In ambiguous situations, capture everything, then narrow with display filters.
- Never assume "just a config issue" without **ruling out malicious activity** (especially for: sudden route changes, ARP shifts, DNS failures, unexpected listening ports).
- Use test environments to **validate both fixes and detections**; if you're not sure whether an ACL will block an attack, test it in the lab with that attack.
- When Wireshark shows cleartext credentials or sensitive data, assume **that data is compromised**; rotate credentials and investigate how attacker access occurred.

***

**END OF MANUAL – NETWORK TROUBLESHOOTING \& TESTING**
Operator: 22DIV / Callsign: Digger
Classification: Personal Use Only

Ready for next topic with this same template structure. Which subject next?
<span style="display:none">[^1][^2][^3][^4][^5][^6][^7][^8]</span>

<div align="center">⁂</div>

[^1]: 5_Linux_OS.md

[^2]: 5_Linux_OS.md

[^3]: Cl_FundCyberSecurity_TL_SW.docx

[^4]: 2_Computer_components.md

[^5]: 3_Virtualisation.md

[^6]: 5_Linux_OS.md

[^7]: 4_Windows_OS.md

[^8]: 1_Cybersecurity_in_Organisations.md

