FIELD OPERATIONS MANUAL
Defensive Operations Guide for NETWORKING FUNDAMENTALS
CLASSIFICATION: PERSONAL USE ONLY
Operator: 22DIV / Callsign: Digger
Purpose: Extract and structure core networking knowledge for defensive operations, rapid troubleshooting, and pentesting/exam reference, with ports and exposure integrated into recap.

***

## **TABLE OF CONTENTS**

SECTION 1: I understand what a network is.
SECTION 2: I can recognise the types of networks.
SECTION 3: I can recognise the types of network topologies.
SECTION 4: I can distinguish among the bus, star, mesh, and ring topologies.
SECTION 5: I understand the ethernet protocols.
SECTION 6: I know and understand the OSI layers.
SECTION 7: I understand IPv4 addressing and subnetting.
SECTION 8: I understand IPv6 addressing and subnetting.
SECTION 9: I understand conversions among binary, decimal, and hexadecimal numbers.
SECTION 10: I can describe the Cisco Packet Tracer is and its uses.
SECTION 11: I understand what network devices are.
SECTION 12: I understand wireless networking and its vulnerabilities.
SECTION 13: I understand security issues of the client/server and client/client systems.
SECTION 14: I understand the core cyber exposure via common ports and services (RECAP).

***

## SECTION 1: I understand what a network is.

This section gives you the minimum mental model for "what a network really is" so you can reason fast in the field instead of memorising vendor diagrams. It focuses on the four moving parts every path has: devices, links, protocols, and security controls. If you can quickly identify those four for any connection, you can both break and defend it under time pressure.

- Network = devices + links + protocols + security moving data between endpoints.
- Devices: PCs, servers, phones, IoT, switches, routers, firewalls.
- Links: wired (UTP, fiber), wireless (Wi‑Fi, cellular).
- Protocol stacks: OSI (7‑layer model), TCP/IP (4‑layer, real world).
- Security layer: firewalls, VPN, IDS/IPS, segmentation.

**Defensive controls (on ops):**

- Always ask: "Which devices? What link? Which protocol? What security?" for any path.
- Treat any path without explicit security (firewall/VPN/ACL) as untrusted.
- Prefer simple, well‑understood paths you can fully map and monitor.

***

## SECTION 2: I can recognise the types of networks.

This section is about scale and trust boundaries. Knowing whether you're dealing with PAN, LAN, MAN, or WAN tells you how much you can realistically control and where to put your defensive effort. It also frames centralisation vs ad‑hoc as a control question: who is in charge of the data plane?

- **PAN** – Personal, very short range (Bluetooth, tethering).
- **LAN** – Local, single site (home/office/campus). Core battlefield.
- **MAN** – City/regional, usually provider‑owned, links multiple LANs.
- **WAN** – Long‑haul, connects cities/countries; internet is the biggest WAN.

**Defensive controls:**

- Treat **LAN** as the main enforcement domain; lock it down hard.
- Assume **WAN/MAN** are hostile; encrypt everything that crosses them (VPN/TLS).
- Treat **PANs** as fragile edges; minimise sensitive data exposure over Bluetooth/etc.

***

## SECTION 3: I can recognise the types of network topologies.

Topology tells you where traffic can go and where it will bottleneck or die. Physical shows where cables actually run; logical shows how frames and packets flow. This section helps you quickly visualise a site so you can pick choke points, pivots, and SPoFs without needing diagrams.

- **Physical** – how cables/devices are wired.
- **Logical** – how traffic actually flows.

Key shapes:

- **Star** – central switch/AP; modern default; easy to segment/monitor.
- **Bus** – one long cable; legacy, noisy, sniffable.
- **Ring** – loop; legacy; one break = outage (unless dual ring).
- **Mesh** – many interlinks; resilient, complex; used for critical infra.
- **Tree** – hierarchical mix (core–distribution–access).

**Defensive controls:**

- For any site, mentally sketch the star/tree; mark choke points for sensors/firewalls.
- Avoid hidden SPoFs at the core (single switch/router with no backup).
- Use tree/star for predictable control; deploy mesh only where you really need resilience.

***

## SECTION 4: I can distinguish among the bus, star, mesh, and ring topologies.

This section sharpens your pattern recognition on the four classic shapes so you can quickly reason about resilience, cost, and sniffability.

- **Bus topology**
    - Single backbone cable with all nodes tapped in.
    - Half‑duplex; collisions; trivial to sniff; largely legacy.
- **Star topology**
    - All nodes connect to a central hub/switch/AP.
    - Simple to manage; core device is a SPoF; default in modern LANs.
- **Mesh topology**
    - Nodes have multiple paths between each other (full or partial mesh).
    - High resilience and redundancy; complex and expensive.
- **Ring topology**
    - Each node connects to two neighbours in a loop.
    - One break can disrupt unless dual ring; mostly legacy now.

**Defensive controls:**

- Prefer **star/tree** with managed switches for visibility and control.
- Use **mesh** where uptime is critical and you can afford monitoring overhead.
- Assume **bus/ring** segments are fragile and easy to sniff; treat them as high‑risk.

***

## SECTION 5: I understand the ethernet protocols.

Ethernet is the dominant LAN technology. This section compresses what you need about speeds, media, and frame structure to read interfaces and captures without digging through RFCs.

- Common standards:
    - 10BASE‑T (10 Mbps), 100BASE‑TX (100 Mbps), 1000BASE‑T (1 Gbps), 10GBASE‑T (10 Gbps).
    - Fiber variants (e.g. 1000BASE‑SX, 10GBASE‑SR) for longer runs.
- Ethernet II frame: `Preamble | SFD | Destination MAC | Source MAC | EtherType | Payload | FCS`.
- EtherType identifies payload protocol (IPv4, IPv6, ARP, etc.).
- MAC addresses: 48‑bit; vendor + device identifier.

**Defensive controls:**

- Use managed switches: enable port security, DHCP snooping, Dynamic ARP Inspection.
- Watch for abnormal EtherTypes or frame sizes in packet captures.
- Keep critical links on stable, modern standards; avoid legacy segments where possible.

***

## SECTION 6: I know and understand the OSI layers.

OSI is your universal language for networking problems. This section gives you a concise layer map so you can localise faults and attacks quickly (e.g., "this is L2 ARP poison" vs "L7 web vuln"). Being able to walk OSI up or down from memory saves massive time in triage.

Remember **"APSTNDP"** (7 → 1):
7. Application – user protocols (HTTP, SMTP, DNS).
6. Presentation – formats, crypto (TLS).
5. Session – sessions, checkpoints.
4. Transport – TCP/UDP, ports.
3. Network – IP routing, ICMP.
2. Data Link – MAC, frames, ARP, switches.

1. Physical – bits, cables, RF.

Ops mapping:

- L1/2 – cables, Wi‑Fi, VLANs, ARP.
- L3 – IPs, subnets, routing.
- L4 – ports, TCP vs UDP.
- L7 – app vulns (web, email, DNS).

**Defensive controls:**

- Troubleshoot **bottom‑up**: 1→7; don't chase app bugs before checking link and IP.
- Tag each issue by layer; this narrows tool choice and playbook fast.
- Map attacks to layers (e.g., ARP spoof = L2; SQLi = L7) so you intercept at the right point.

***

## SECTION 7: I understand IPv4 addressing and subnetting.

IPv4 is still the operational default. This section gives you enough addressing and subnetting to design segments, understand attack surface size, and survive exam questions. The goal is pattern recognition, not longhand arithmetic while under pressure.

- IPv4 = 32 bits, dotted decimal (e.g., 192.168.1.10).
- Private ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- CIDR: `/mask` notation (e.g., `/24` = 255.255.255.0, 254 hosts).

Key formulas:

- Hosts per subnet = `2^(host bits) − 2`.
- New mask when splitting: borrow bits from host side.

Example:

- `/24` → 256 IPs → 254 usable.
- Borrow 2 bits → `/26` → 4 subnets → 62 usable each.

**Defensive controls:**

- Subnet by **function** (users, servers, management, IoT) to contain compromise.
- Keep high‑risk devices (e.g., guest Wi‑Fi, BYOD, IoT) in small dedicated subnets.
- Design so that lateral movement requires crossing a routed boundary where you can enforce ACLs.

***

## SECTION 8: I understand IPv6 addressing and subnetting.

IPv6 is the other half of dual‑stack networks and a frequent blind spot. This section gives you just enough to recognise IPv6, understand its scale, and not ignore it when attackers use it to bypass IPv4‑only defenses.

- IPv6 = 128 bits, hex, 8 groups: `2001:db8:85a3::8a2e:370:7334`.
- No broadcast; uses multicast.
- Common prefix: `/64` for LANs.
- Types: global unicast, link‑local (`fe80::/10`), unique local (`fc00::/7`).

Ops risks:

- Dual‑stack = two parallel networks; IPv6 often unmonitored.
- NDP replaces ARP and can be spoofed.

**Defensive controls:**

- If you're not using IPv6 deliberately, **disable** it to reduce attack surface.
- If you are using it, mirror IPv4 protections: firewalls, logging, IDS, ACLs.
- Watch for tunneled IPv6 (Teredo, 6to4) and block if not needed.

***

## SECTION 9: I understand conversions among binary, decimal, and hexadecimal numbers.

Number systems sit behind addressing, masks, and protocol fields. This section focuses on enough binary/decimal/hex fluency to sanity‑check configs, subnets, and dumps on the fly.

- Decimal ↔ Binary:
    - 8‑bit octets (0–255) to/from 8‑bit binary.
- Binary ↔ Hex:
    - Group bits in 4s; each nibble = 1 hex digit (e.g. 1111₂ = F₁₆).
- Masks via bits:
    - /24 = 11111111.11111111.11111111.00000000 → 255.255.255.0.
    - /26 = 11111111.11111111.11111111.11000000 → 255.255.255.192.

**Defensive controls:**

- Use quick binary/hex checks to spot bad masks or off‑by‑one errors that overexpose hosts.
- Recognise MACs and IPv6 chunks in hex when reading raw outputs.
- Confirm CIDR boundaries mentally before applying network changes.

***

## SECTION 10: I can describe the Cisco Packet Tracer is and its uses.

Packet Tracer is your safe range for networking drills. This section locks in what it is and when to use it so you can rehearse before touching live environments.

- Network simulation tool used in Cisco/TAFE labs.
- Emulates routers, switches, PCs, servers, IoT, with CLI and basic GUIs.
- Modes: real‑time (normal operation) and simulation (step‑through packet flow).
- Supports core protocols: IP, DHCP, DNS, HTTP, routing, VLANs, ACLs, NAT.

**Defensive controls:**

- Prototype risky changes in Packet Tracer before production deployment.
- Use simulation mode to understand exactly how packets traverse your design.
- Maintain lab topologies as reference playbooks to adapt under pressure.

***

## SECTION 11: I understand what network devices are.

Devices are where theory meets hardware. This section is a compressed lookup for what each device does, which OSI layer it lives in, and what that means for control and visibility.

- **Hub (L1)** – repeats to all; legacy; ignore except in old sites.
- **Switch (L2)** – forwards by MAC; VLANs; core access control.
- **Router (L3)** – routes between nets; default gateway; NAT.
- **Firewall (L3–7)** – enforces policy; packet/stateful/app/NGFW.
- **AP (L2)** – Wi‑Fi bridge; enforces Wi‑Fi auth/encryption.

**Defensive controls:**

- Replace any remaining hubs with switches to stop blind broadcast sniffing.
- Use managed switches with VLANs, port security, and 802.1X where possible.
- Lock router and firewall admin planes (strong auth, VPN‑only mgmt, logging enabled).
- Treat APs as semi‑trusted; isolate wireless networks from core via routing and ACLs.

***

## SECTION 12: I understand wireless networking and its vulnerabilities.

Wi‑Fi expands the network into the air, which makes it convenient for users and attackers. This section gives just enough RF, protocol, and crypto context to decide when a wireless segment is trustworthy.

- Bands: 2.4 GHz (range, noisy), 5 GHz (speed), 6 GHz (Wi‑Fi 6E).
- Security stack:
    - WEP/WPA – broken; never use.
    - WPA2 – current baseline; strong passphrases or 802.1X.
    - WPA3 – improved protections; best where supported.
- Attacks: rogue/evil twin APs, deauth floods, WPS brute‑force, sniffing.

**Defensive controls:**

- For orgs, target **WPA2‑Enterprise or WPA3‑Enterprise + 802.1X**; kill WEP/WPA.
- Turn off WPS; segment guest Wi‑Fi into its own VLAN with limited access.
- Run periodic wireless surveys to detect rogue and evil‑twin APs.

***

## SECTION 13: I understand security issues of the client/server and client/client systems.

This is about **who controls what**. If you know where the "brain" of the network is, you know where to defend hardest and what to distrust if there is no brain.

- **Client/server**: central auth, logging, backups; server is the crown jewel.
- **Client/client (P2P)**: each node is both client and server; hard to manage and secure.

**Defensive controls:**

- For anything valuable, prefer client/server with central auth and logging.
- Isolate P2P and consumer‑grade sharing apps to low‑trust segments.
- Enforce least privilege on servers and monitor for abnormal client behaviour.

***

## SECTION 14: I understand the core cyber exposure via common ports and services (RECAP).

This final recap locks the whole networking picture onto what most attacks actually hit: exposed services and their ports. It is your mental "ports first" checklist for any engagement: see which ports are open, map them to services and protocols, then decide how to defend or exploit.

Common high‑value ports and services:

- **22/TCP – SSH**: secure remote admin; brute‑force and key theft target.
- **21/20/TCP – FTP**: cleartext file transfer; credentials and data in the clear; prefer SFTP/FTPS.
- **23/TCP – Telnet**: cleartext remote shell; should be disabled everywhere.
- **53/UDP,TCP – DNS**: name resolution; used for tunnelling, exfil, and amplification.
- **80/443/TCP – HTTP/HTTPS**: web; main app‑layer attack surface (XSS, SQLi, auth bypass).
- **25/587/TCP – SMTP**: mail transfer/submission; spam, phishing, relay abuse.
- **110/143/995/993/TCP – POP3/IMAP(+SSL)**: mailbox access; credential and content theft.
- **445/TCP – SMB**: Windows file/print and many ransomware worms; high‑risk if exposed.
- **3389/TCP – RDP**: remote desktop; brute‑force and exploit magnet.

**Defensive controls (ports‑first checklist):**

- Default‑deny inbound; open only the ports you can justify.
- Prefer encrypted variants (SSH, HTTPS, SFTP, IMAPS, SMTPS) and disable legacy cleartext services.
- Hide admin ports (SSH, RDP, VPN) behind VPN and MFA; never expose them naked to the internet.
- Continuously monitor for scans, brute‑force attempts, and unusual DNS/HTTP patterns.
- In any new environment, enumerate open ports first, then walk back through these sections (network types, topologies, OSI, addressing, devices, wireless) to understand and harden the context.

***

**END OF MANUAL – NETWORKING FUNDAMENTALS**
Operator: 22DIV / Callsign: Digger
Classification: Personal Use Only

Ready for next topic with this same template structure. Which subject do you want next?
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

