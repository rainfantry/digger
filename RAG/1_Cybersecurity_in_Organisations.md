**FIELD OPERATIONS MANUAL**  
Defensive Cyber Operations Guide  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Rapid containment and recovery protocol for cyber incidents under time pressure
**FIELD OPERATIONS MANUAL**  
Defensive Cyber Operations Guide  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Defensive cyber protocol in high-threat digital environment  

 LESSON SELF-ASSESSMENT – CYBER SECURITY IN ORGANISATIONS**  
-----------------------------------------------------  

**Quick paragraph summary (30-second read)**  
You have finished the "Cyber security in organisations" lesson. This checklist lets you self-assess your confidence in 13 key learning outcomes. Tick each item you feel you can confidently explain or apply in an exam or real scenario. If any remain unticked, return to the relevant lesson content or this manual's matching sections for quick review. This step confirms mastery of the module and identifies any gaps before moving on or taking assessments. Bottom line: be honest — confidence means you can use the knowledge under pressure, not just memorise it.

**Self-Assessment Checklist**  
Check (✓) each box if you feel confident you can complete the task. If not, review the lesson or manual section.

**I can identify attacks, concepts, and techniques.**  
[ ] Tick if confident.  
Summary: You can name and explain common cyber attacks (malware, DoS/DDoS, social engineering, MITM, injection, zero-days), core concepts (exploit, vector, TTP), and techniques (phishing, ARP poisoning, credential dumping).

**I can protect my data and privacy.**  
[ ] Tick if confident.  
Summary: You can apply personal protection steps: strong unique passphrases + password manager, MFA everywhere, offline backups, VPN + tracker/ad blockers, HTTPS verification, avoid public Wi-Fi for sensitive tasks, limit social media PII, separate emails, regular updates, antivirus/firewall.

**I understand the firewalls and behaviour approach to cyber security.**  
[ ] Tick if confident.  
Summary: Firewalls inspect packets to allow/block traffic (stateless = fast/no memory, stateful = tracks sessions, NGFW = DPI + IPS). Behaviour-based uses ML to learn "normal" and flag anomalies early (recon phase), proactive vs reactive.

**I can recognise the effects of a cyber breach.**  
[ ] Tick if confident.  
Summary: Cyber harm has 5 themes: physical/digital (asset damage), economic (revenue/fines), psychological (stress/anxiety), reputational (trust loss), societal (service disruption). Exposed data includes PII, financials, IP. Australia NDB requires reporting serious harm breaches to OAIC + individuals.

**I can identify threat actors, vectors, and threat goals.**  
[ ] Tick if confident.  
Summary: Actors: state-sponsored (espionage), cybercriminals (financial), script kiddies (ego), hacktivists (ideology), insiders (revenge), cyber terrorists (disruption). Vectors: exploits, phishing, malware, insider access, supply-chain. Goals: money, secrets, downtime, publicity, revenge.

**I understand incident response standards.**  
[ ] Tick if confident.  
Summary: IR standards minimise impact (ACSC plan, NIST SP 800-61 lifecycle: preparation → detection → containment → eradication → recovery). Australia: 12-hour reporting for critical incidents, 72-hour for others to ACSC.

**I understand cyber security frameworks and standards.**  
[ ] Tick if confident.  
Summary: Frameworks: Essential Eight (ACSC, 8 controls, 4 maturity levels), NIST CSF (6 functions wheel), ISM (ACSC manual), ISO 27000 (ISMS), GDPR (EU privacy). Standards guide risk management and compliance.

**I understand the fundamentals of the National Institute of Standards and Technology Cyber Security Framework.**  
[ ] Tick if confident.  
Summary: NIST CSF has 6 functions: Govern (policy), Identify (risks), Protect (safeguards), Detect (monitoring), Respond (incident handling), Recover (restoration). Includes profiles (current/target posture) and tiers (maturity 1–4).

**I understand the Essential Eight strategies from the Australian Cyber Security Centre to mitigate cyber security incidents.**  
[ ] Tick if confident.  
Summary: 8 controls: application control, patch apps/OS, macro settings, app hardening, restrict admin privileges, MFA, regular backups. Maturity 0–3 (Level 2 mandatory for many government entities). Focuses on Windows networks.

**I understand the Centre for Internet Security (CIS) controls for cyber security protection.**  
[ ] Tick if confident.  
Summary: 18 practical controls: asset inventory (hardware/software), data protection, secure configuration, access management, vulnerability scanning, logging, email/browser protection, malware defence, backups, network monitoring, training, incident response, penetration testing.

**I can identify the network and cyber types of security.**  
[ ] Tick if confident.  
Summary: Network security protects data in transit (firewalls, VPNs, access control, antivirus). Cyber security is broader — protects networks, devices, apps, data (in transit/at rest), operations, disaster recovery, end-user education.

**I understand the importance of policies and procedures in protecting organisations.**  
[ ] Tick if confident.  
Summary: Policies set rules (acceptable use, data handling, passcode strength), procedures show steps. Reduce human error. Examples: 3-2-1 backups, MFA, application control. Tools support policies; NIST guides implementation.

**I understand the MITRE TTP and ATT&CK cyber security frameworks.**  
[ ] Tick if confident.  
Summary: MITRE ATT&CK = 14 tactics (goals) + techniques (methods) from real attacks, non-linear, for detection/hunting. Cyber Kill Chain = 7 linear stages for attack flow/prevention. ATT&CK complements Kill Chain with detailed TTPs.

**Bottom line – quick deploy**  
Tick honestly — if you can explain each in your own words or apply it, mark confident.  
Unticked? Review the matching manual section or lesson notes.  
Prioritise Australian TAFE topics: Essential Eight (Level 2), ISM, incident reporting (12/72 hours), NIST CSF (6 functions), ATT&CK (14 tactics).  
These are exam favourites.  
All ticked = strong lesson mastery.  
Ready for next module or exam — let me know what to drill.  

This section teaches: self-assessment locks in learning.  
Confidence = exam-ready application.  
Review gaps now — it saves time later.


**TABLE OF CONTENTS**  
SECTION 1: ATTACK VECTOR CLASSIFICATION ..................................................... 
SECTION 2: MALWARE DELIVERY OPERATIONS ................................................ 
SECTION 3: DENIAL OF SERVICE & BANDWIDTH ATTACKS ............................ 
SECTION 4: SOCIAL ENGINEERING VECTORS ................................................... 
SECTION 5: MAN-IN-THE-MIDDLE INTERCEPT ................................................. 
SECTION 7: ZERO-DAY WEAPONIZATION .......................................................
SECTION 8: PERSONAL ASSET DEFENSE PROTOCOLS .................................. 
SECTION 9: THE FIVE LAWS OF CYBER OPERATIONS ................................... 
SECTION 10: FIREWALL & BEHAVIOURAL DEFENSE LAYERS ....................... 
SECTION 11: BREACH IMPACT ASSESSMENT ............................................... 
SECTION 12: THREAT ACTOR PROFILES & OBJECTIVES ............................... 
SECTION 13: INCIDENT RESPONSE STANDARDS ........................................ 
SECTION 14: KEY INCIDENT RESPONSE FRAMEWORKS .............................. 
SECTION 15: CYBER SECURITY FRAMEWORKS & STANDARDS ................... 
SECTION 16: IMPORTANCE OF POLICIES AND PROCEDURES ........................ 
SECTION 16: CYBER KILL CHAIN & ATTACK INTRODUCTION ........................ 


**SECTION 1: ATTACK VECTOR CLASSIFICATION**  
-----------------------------------------------  

Primary attack surfaces identified:  
• Malware delivery (ransomware, trojans, worms)  
• Denial of service (DoS / DDoS)  
• Social engineering (phishing, whaling, spear-phishing)  
• Man-in-the-middle interception (MITM)  
• Input injection (XSS, SQLi, OS command)  
• Zero-day exploitation  

**SECTION 2: MALWARE DELIVERY OPERATIONS**  
--------------------------------------------  

**Malware Attacks - Ultra Concise**  
- **Malware**: Malicious software for data theft, ransom, or damage. Most common attack. Types: ransomware, trojans, worms.  

**Ransomware**  
- Locks/encrypts data, demands payment.  
- Ex: Colonial Pipeline (2021) – offline days, disrupted 45% East Coast fuel, $4.4M ransom ($2.3M recovered).  

**Trojans**  
- Fake legit apps delivering payload.  
- Types: Backdoor (access), Downloader (more malware), Exploit (vulnerabilities).  
- Ex: Zloader – hidden in fake Zoom/Atera installers.  

**Worms**  
- Self-replicating, spread via networks/files/USB/social engineering.  
- Slow networks by bandwidth theft.  
- Ex: ILOVEYOU (2000) – email attachment, overwrote files, self-mailed, infected millions.  

**SECTION 3: DENIAL OF SERVICE & BANDWIDTH ATTACKS**  
-----------------------------------------------------  

**DoS/DDoS Attacks - Ultra Concise**  
- **Core mechanism**: Flood target with fake requests to disrupt/overwhelm service, denying legitimate access.  
- **DoS**: Single source.  
- **DDoS**: Multiple sources (botnet of compromised devices) → harder to block.  

**Example: GitHub (28 Feb 2018)**  
- Memcached amplification attack (spoofs target IP, exploits vulnerable servers → up to 51,200x amplification).  
- Peak: 1.35 TB/s traffic.  
- Impact: Fully unavailable 5 min, intermittent another 5 min.  
- Mitigation: Recovered in ~10 min using Akamai Prolexic (rerouted traffic through scrubbing centers).  

**SECTION 4: SOCIAL ENGINEERING VECTORS**  
----------------------------------------  

**Social Engineering Attacks - Ultra Concise**  
- **Core**: Exploits human psychology (not tech vulnerabilities); tricks users into actions (e.g., reveal info/access) via emotions or money.  

**Phishing**  
- Mass/indiscriminate; impersonates trusted sources (gov, banks, tech firms).  
- Tactics: Malicious links/attachments to steal info or deliver malware.  
- Ex: Fake Microsoft emails/SMS with bad links.  

**Spear Phishing**: Targeted at specific person/group (e.g., finance dept urgent "contract changes").  

**Whaling**  
- Targets high-value execs (e.g., CEOs); more tailored effort, higher rewards.  
- Ex: Fake CEO messages asking employees to buy gift cards or transfer funds.  

**SECTION 5: MAN-IN-THE-MIDDLE INTERCEPT**  
------------------------------------------  

**Man-In-The-Middle (MITM) Attacks - Ultra Concise**  
- **Core**: Attacker intercepts communication between two parties to eavesdrop, steal data/passwords, or modify traffic. Victims often unaware as flow appears normal.  

**Example: DigiNotar Attack**  
- Hackers compromised certificate authority, issued hundreds of fake SSL certs (e.g., for Google).  
- Enabled decryption/eavesdropping on encrypted traffic (email, browsing).  
- Result: Company bankruptcy.  

**ARP Poisoning/Spoofing (LAN MITM)**  
- Attacker sends fake ARP messages linking their MAC address to a legitimate device's IP.  
- Redirects traffic intended for victim to attacker.  
- Background: ARP tables map IP → MAC for local communication.  
- Can also enable DoS by blocking device communication.  

**SECTION 6: INPUT INJECTION EXPLOITS**  
--------------------------------------  

**Injection Attacks - Ultra Concise**  
- **Core**: Malicious code injected via unvalidated/unsanitized user input. OWASP ranks as 3rd most common cyberattack.  

**XSS (Cross-Site Scripting)**  
- Injects malicious scripts into trusted websites.  
- Enables: Steal cookies/session tokens, sensitive data, HTML rewriting.  

**SQL Injection**  
- Inserts malicious SQL queries into input.  
- Enables: Read/modify data, admin ops, file recovery, OS commands.  
- Mitigation: Parameterized queries (avoid string concatenation), input sanitization.  

**OS Command Injection (Shell Injection)**  
- Executes arbitrary OS commands on server via vulnerable app.  
- Risk: Full server compromise, lateral attacks on infrastructure.  

**SECTION 7: ZERO-DAY WEAPONIZATION**  
-------------------------------------  

**Zero-Day Exploits - Ultra Concise**  
- **Core**: Attacks exploiting unknown (zero-day) software vulnerabilities; often undetected by AV/security tools as they are new/undocumented.  
- **Zero-Day Vulnerability**: Undiscovered software flaw.  
- **Zero-Day Exploit**: Method to abuse it.  

**Example: Stuxnet (2010)**  
- Worm using 4 Windows zero-days.  
- Targeted Iranian uranium enrichment centrifuges.  
- Physically damaged equipment via PLC infection.  
- Widely attributed to US-Israel joint operation.  

**SECTION 8: PERSONAL ASSET DEFENSE PROTOCOLS**  
------------------------------------------------  

**Cybersecurity Guide - Ultra Concise (Structured by Headings)**  

**Why should personal devices be protected?**  
- Devices store sensitive data (contacts, emails, finances, browsing history).  
- Rising cyberattacks (mainly malware & phishing) → identity theft, financial fraud, stress.  

**Methods and tools to safeguard personal privacy**  

**Keep offline backups**  
- Store disconnected from network; update regularly.  
- Protects against ransomware & data loss.  

**Use strong passwords, password managers and MFA**  
- Long passphrases (4+ words) or lengthy strings; avoid reuse/weak.  
- Password manager: stores unique complex passwords securely.  
- Enable MFA everywhere (password + app code/biometrics/token).  

**Protect web browsing activities**  
- Tracker blockers (extensions).  
- VPN: hides IP, encrypts traffic.  
- Ad blockers: reduce trackers/malvertising, faster pages.  
- Private search (e.g., DuckDuckGo): no tracking/history.  

**Avoid using untrusted Wi-Fi networks**  
- Use VPN or mobile data for sensitive tasks.  
- Verify HTTPS/padlock; avoid personal/financial info.  
- Disable auto-connect & file sharing; log out; heed warnings.  

**Make secure payments online**  
- HTTPS only (padlock).  
- Prefer third-party (e.g., PayPal).  
- Avoid wire transfers; use MFA.  
- Enable banking alerts; use mobile data if Wi-Fi risky.  

**Be alert to unsolicited communication**  
- Ignore suspicious links/attachments (email/SMS/calls).  
- Verify directly via official contacts (phishing defense).  

**Keep track of online presence**  
- Avoid posting location, birthday, address.  
- Use nicknames/fake details; separate emails by purpose.  
- Unique passwords per account; disable location tracking.  
- Limit audience; sign in with email, not social logins.  

**Techniques to protect personal devices (ACSC)**  
- Regular trusted updates.  
- Multiple backups (offline + online).  
- Lock screen (strong password/biometrics + auto-lock).  
- Physical security (never unattended).  
- Updated antivirus (e.g., Windows Defender).  
- Enable firewall.  
- Uninstall unused software.  
- Trusted sources only for downloads.  
- Avoid unowned devices for logins.  
- Sandbox/virtualisation for risky sites/apps.  

**SECTION 9: THE FIVE LAWS OF CYBER OPERATIONS**  
------------------------------------------------  

**The 5 Laws of Cybersecurity (Nick Espinosa TEDx Talk)**  

**Law 1: If there is a vulnerability, it will be exploited**  
- Universal truth: From banks to computers, anything valuable gets targeted.  
- Historical: Hackers exploit since first "bugs"; examples include toll evasion hacks and mid-2000s cyber sabotage of illegal nuclear programs (Stuxnet allusion).  
- "Life finds a way" — vulnerabilities always get used.  

**Law 2: Everything is vulnerable in some way**  
- No system is safe; nothing is off-limits.  
- Even billion-dollar companies (retailers, insurers) with compliance get breached.  
- 2018 CPU/chip flaws exposed virtually everyone.  

**Law 3: Humans trust even when they should not**  
- Live demo: "Look under your seat" prank → audience trusts blindly (laughter).  
- "Trust sucks" but necessary for society.  
- Examples: Falling for phishing, fake antivirus scams, filling illegitimate online forms.  
- Always question infrastructure and people online.  

**Law 4: With innovation comes the opportunity for exploitation**  
- Innovators (Bell, Gates, Zuckerberg) create conveniences → immediate risks.  
- IoT explosion: Smart devices add attack surface.  
- 2016 Mirai botnet: Infected millions of devices → record-breaking DDoS attacks.  

**Law 5: When in doubt, see Law #1**  
- Not a cop-out; all cyber issues stem from exploitable vulnerabilities.  
- Laws are immutable due to human nature.  
- Best defense: Learn to **think like a hacker** → builds shared cybersecurity language for safety.  

**SECTION 10: FIREWALL & BEHAVIOURAL DEFENSE LAYERS**  
--------------------------------------------------------  

**Firewalls & Behaviour-Based Security – Consolidated Ultra Concise Summary**  

**Firewalls – Core Role**  
First line of network defense  
Inspects packet headers (source/destination IP/port/protocol) → allow or block  
Software (endpoint) or hardware (appliance/router)  

**Official Definition (Fithen et al.)**  
Hardware/software combo enforcing security policy between controlled & uncontrolled networks  
Blocks external threats + segments internal networks (limits insider risk)  

**Classification**  
- **Stateless** → per-packet only (no memory)  
- **Stateful** → tracks session context (remembers conversation)  

**Main Commercial Types**  
- **Packet Filtering** → basic ACLs (IP, port, protocol, interface) – fast, simple  
- **Stateful Inspection** → tracks connection state – detects spoofing/hijacking  
- **Application-Level Gateway / Proxy** → full proxy, authenticates app-layer traffic  
- **Circuit-Level Gateway / Proxy** → creates trusted tunnel, no content inspection  
- **Next-Generation Firewall (NGFW)** → all above + DPI, app-ID, IPS, malware scanning  

**Stateless vs Stateful – Quick Comparison**  
| Aspect          | Stateless                          | Stateful                              |  
|-----------------|------------------------------------|---------------------------------------|  
| Memory          | None                               | Tracks sessions                       |  
| Speed           | Very fast, low resource            | Slower, higher memory                 |  
| Detection       | Basic header rules only            | Spots anomalies, hijacks, scans       |  
| Best for        | High-speed filtering               | Modern threat detection               |  

**Behaviour-Based Cybersecurity**  
**Shift**  
Reactive → proactive (detect anomalies before breach)  

**Names**  
BTA / BAD / BTD  

**How it works**  
ML analyzes massive logs → builds “normal” baseline → flags deviations in real time  

**Key Benefits**  
- Early detection (recon phase)  
- Real-time monitoring  
- Reduces forensic hunting  
- Auto-blocks via IPS integration  

**Bottom line**  
Firewalls = gatekeepers (rule-based)  
Behaviour-based = smart watchdog (learning-based)  
Best protection = combine both  

**SECTION 11: BREACH IMPACT ASSESSMENT**  
---------------------------------------  

**Effects of a Cyber Breach – Professional Summary**  

**Definition of Cyber Harm**  
Damage resulting directly from an attack via digital infrastructure, devices, data, or software (Agrafiotis et al., 2018).  

**Immediate & Long-Term Costs**  
- Direct: fines, notification costs, PR response, remediation  
- Hidden / Intangible: reputation erosion, operational disruption, loss of IP/competitive advantage, lasting strategic damage (Mossburg et al., 2017)  

**Five Key Themes of Cyber Harm**  
- **Physical / Digital**  
Destruction, theft, compromise, infection, or exposure of assets (servers, devices, data).  
- **Economic**  
Revenue loss, customer churn, stock price decline, regulatory penalties, increased insurance premiums.  
- **Psychological**  
Anxiety, stress, depression, or in extreme cases loss of life among affected individuals (customers, employees).  
- **Reputational**  
Loss of stakeholder trust → damaged supplier/vendor relationships, talent attrition, reduced business opportunities.  
- **Social & Societal**  
Disruption to critical services, national infrastructure impacts, widespread public inconvenience or harm.  

**Information Commonly Exposed**  
- Customer personal & financial data  
- Employee records (PII: DOB, addresses, etc.)  
- Email archives  
- Intellectual property, patents, product designs  
- Business plans, marketing strategies, new ideas  

**Australian Legal Obligation – Notifiable Data Breaches (NDB) Scheme**  
Under the Privacy Act 1988 (Cth), if a breach is likely to cause **serious harm** to individuals:  
- Notify the Office of the Australian Information Commissioner (OAIC)  
- Notify affected individuals directly  
- Provide recommended protective actions in the notification  

**SECTION 12: THREAT ACTOR PROFILES & OBJECTIVES**  
-------------------------------------------------  

**Threat Actors, Vectors & Goals – Ultra Concise Summary**  

**Core Elements of a Cyber Attack**  
- **Threat Actor** — Person/group intentionally causing harm via technology.  
- **Threat Vector / Attack Vector** — The path or method used to deliver the attack (e.g., exploit, phishing, malware).  
- **Threat Goal** — Desired end result (financial gain, espionage, disruption, publicity, etc.).  

**Types of Threat Actors**  
| Type                | Primary Motivation              | Description & Typical Tactics                                                                 |  
|---------------------|---------------------------------|-----------------------------------------------------------------------------------------------|  
| State-sponsored     | Political / Strategic           | Nation-state backed; highly resourced APT groups; long-term espionage, sabotage, supply-chain attacks (e.g., spying on governments, critical infrastructure, corporations). |  
| Cybercriminals      | Financial                       | Organized/professional; profit-focused; ransomware, phishing campaigns, banking trojans, credential stuffing, data theft for resale/extortion. |  
| Script kiddies      | Curiosity / Bragging / Ego      | Inexperienced beginners; rely on pre-built tools/scripts (Metasploit, leaked exploits); defacements, low-skill DDoS, testing/learning attacks. |  
| Hacktivists         | Ideological / Political / Social| Cause-driven groups/individuals; Anonymous-style ops; leaks/doxxing, website defacement, DDoS protests against governments, corporations, or policies. |  
| Insiders            | Financial / Revenge / Personal  | Current/former employees, contractors; privileged access abuse; data exfiltration, sabotage, selling secrets, credential misuse (coerced or malicious). |  
| Cyber terrorists    | Ideological / Political / Criminal | Extremist groups/individuals; aim for maximum disruption/destruction; target critical infrastructure (power grids, hospitals, transport) to cause panic, economic harm, or ideological impact. |  

**Common Threat Goals by Actor Type**  
- Financial → ransom, stolen data sales, fraud (cybercriminals, some insiders).  
- Espionage / Intelligence → steal secrets/IP (state-sponsored).  
- Disruption / Destruction → downtime, infrastructure damage (cyber terrorists, hacktivists).  
- Publicity / Protest → media attention, leaks, embarrassment (hacktivists, script kiddies).  
- Personal gain / Revenge → credential theft, sabotage (insiders).  

**Threat Vectors (Examples)**  
- Technical: unpatched vulnerabilities, malware (ransomware, trojans, worms).  
- Human: social engineering (phishing, spear-phishing, pretexting).  
- Physical: USB drops, insider access.  
- Supply-chain: compromised software updates, third-party vendors.  

**Bottom line**  
Understand the actor → anticipate their likely vectors and goals → prioritize defenses accordingly.


**SECTION 13: INCIDENT RESPONSE STANDARDS**  
--------------------------------------------  

**Incident Response (IR) standards**  
Guidelines, best practices and procedures organisations use to prepare for, respond to and recover from cyber security incidents  

**Goal**  
Minimise impact of incident on organisation’s operations, reputation and bottom line  

**Mandatory Reporting – Security of Critical Infrastructure Act 2018 (Cth)**  
Regulated entities (carriers, service providers)  

• **Critical cyber security incidents**  
Significant impact on asset availability  
Notify Australian Cyber Security Centre (ACSC)  
Time limit: within 12 hours after becoming aware  

• **Other cyber security incidents**  
Relevant impact on entity’s assets  
Notify ACSC  
Time limit: within 72 hours after becoming aware  

Reporting channel: ACSC Report and Recover page  

**SECTION 14: KEY INCIDENT RESPONSE FRAMEWORKS**  
-----------------------------------------------  

**ACSC Cyber Incident Response Plan**  
Guide from ACSC  
• Creating plan to defend against cyber incidents  
• Downloadable plan template  
• Readiness checklist  

**Guidelines for cyber security incidents**  
Chapter in Australian Cyber Security Centre (ACSC) Information Security Manual (ISM)  
• Helps defenders recognise cyber security events and incidents  
• Provides guidelines for detection and response  

**NIST SP 800-61**  
Guidelines developed by National Institute of Standards and Technology (NIST)  
Systematic approach to incident response  
Covers:  
• Incident preparation  
• Detection and analysis  
• Containment  
• Eradication  
• Recovery  

**ISO 27035**  
Standard developed by International Organisation for Standardisation (ISO)  
Guidelines for incident management  
Includes:  
• Incident response  
• Incident handling  
• Incident recovery  

**COBIT**  
Framework developed by ISACA (Information Systems Audit and Control Association)  
Guidelines for IT governance and management  
Includes incident response  

**PCI DSS**  
Security standards developed by Payment Card Industry Security Standards Council (PCI SSC)  
Organisations must comply to protect cardholder data  
Includes incident response requirements as part of overall security  

**SOC 2**  
Standards developed by American Institute of Certified Public Accountants (AICPA)  
Guidelines for managing and maintaining security and availability of IT systems  

**Bottom line**  
Adopt structured IR lifecycle (NIST SP 800-61 preferred)  
Meet mandatory 12/72-hour ACSC reporting deadlines  
Maintain current plan, test regularly, document every action



**SECTION 15: CYBER SECURITY FRAMEWORKS & STANDARDS**  
-----------------------------------------------------  

**Quick-deploy overview – what this section teaches**  
Organisations use structured frameworks to systematically reduce cyber risk instead of random fixes.  
These are proven checklists and maturity models — like military doctrine for cyber defence.  
Australian context prioritises **Essential Eight** + **NIST CSF** + **ISM**.  

Cyber security frameworks are ready-made playbooks organisations follow to systematically protect systems and data instead of guessing. In Australia, start with the Essential Eight (8 must-do controls from ACSC) to block most common attacks on Windows networks. Measure how strong your defences are using 4 maturity levels (Level 2 is mandatory for many government entities). Add the NIST CSF for a full lifecycle view (Govern → Identify → Protect → Detect → Respond → Recover). Use the ISM (ACSC manual) for detailed Australian government rules. ISO 27000 family is the international standard for building a formal security system. GDPR applies only if you handle EU personal data. Bottom line: follow these proven structures — Essential Eight first, layer NIST and ISM — assess your current level, fix gaps, test regularly.

**Essential Eight (ACSC) – the Australian minimum baseline**  
8 high-impact controls to stop most real-world attacks on Windows networks.  
Maturity measured in 4 levels (0 = wide open → 3 = very hard to breach).  
Commonwealth non-corporate entities must reach **Level 2**.  

**Level 1 controls (baseline you can deploy fast)**  
1. **Application control** – only approved software runs  
2. **Patch applications** – fix known bugs quickly  
3. **Patch operating systems** – same for OS  
4. **Disable dangerous macros** – block malicious Office macros  
5. **Harden user apps** – block ads, Flash, Java in browsers  
6. **Restrict admin rights** – normal users can't install or change system  
7. **Multi-factor authentication** – add second factor everywhere possible  
8. **Daily backups** – offline, tested restores  

**NIST Cybersecurity Framework (CSF) – the big-picture wheel**  
6 core functions (wheel diagram) – cover everything from prevention to recovery.  

Quick one-liner per function:  
• **Govern** – set policy, assign responsibility, track progress  
• **Identify** – know what you have (assets), what can go wrong (risks)  
• **Protect** – put locks on everything (access control, training, backups)  
• **Detect** – watch continuously for weird activity  
• **Respond** – when something bad happens: contain, analyse, notify  
• **Recover** – get back to normal + learn from it  

**Implementation Tiers** – how mature is your defence?  
• Tier 1: Informal, ad-hoc  
• Tier 2: Risk-aware but inconsistent  
• Tier 3: Repeatable, documented processes  
• Tier 4: Adaptive, constantly improving  

**ISM (Australian Cyber Security Centre manual)**  
Official Australian government cyber defence bible.  
Long list of controls across many areas (physical, personnel, system hardening, crypto, email, networking, etc.).  
Risk management follows 6 NIST-based steps:  
1. Define system  
2. Select controls  
3. Implement  
4. Assess  
5. Authorise  
6. Monitor continuously  

**ISO 27000 family**  
International gold standard for building an Information Security Management System (ISMS).  
27001 = main certifiable standard  
27002 = practical control catalogue  
Others are sector-specific or supporting  

**GDPR**  
EU privacy law – not Australian, but applies if you handle EU citizens' data.  
Focus: individual rights over personal data, consent, breach notification within 72 hours.  

**Bottom line – quick deploy takeaway**  
1. Start with **Essential Eight Level 1** – it's the fastest Australian baseline.  
2. Use **NIST CSF** as your overall strategy wheel.  
3. Refer to **ISM** for detailed Australian government controls.  
4. Assess your current maturity → pick gaps → fix highest-impact items first.  
5. Test everything regularly — paper plans mean nothing without drills.  

This section is saying:  
Don't guess what to secure — follow these proven frameworks.  
Pick the Australian ones first (Essential Eight + ISM), layer NIST for structure, and comply if you're regulated.


**SECTION 16: CIS CONTROLS**  
---------------------------  

**Quick paragraph summary (30-second read)**  
The Centre for Internet Security (CIS) provides 18 practical, prioritized controls that organisations can implement to significantly reduce cyber risk. These are actionable best practices focused on asset visibility, access control, incident response, and continuous monitoring. They are vendor-neutral, widely adopted globally, and designed to protect against the most common attack techniques. Controls are grouped into three categories: asset management, incident response, and access control. Bottom line: use the CIS Controls as a checklist — start with the first few (inventory, patching, access management) for the biggest immediate impact, then build toward all 18.

**The 18 CIS Critical Security Controls**  
1. **Inventory and control of enterprise assets**  
Continuously manage assets and IT infrastructure to identify unauthorised or unmanaged devices.

2. **Inventory and control of software assets**  
Regularly monitor authorised software and remove any unmanaged or unauthorised applications.

3. **Data protection**  
Employ processes and controls to identify, classify, and protect sensitive data; remove unnecessary copies.

4. **Secure configuration of enterprise assets and software**  
Keep all configurations and software up to date to eliminate known weaknesses.

5. **Account management**  
Use authorised tools to manage access to accounts, assets, or software.

6. **Access control management**  
Implement processes and tools to monitor and control access credentials for assets and applications.

7. **Continuous vulnerability management**  
Regularly scan for vulnerabilities in infrastructure and mitigate them quickly.

8. **Audit log management**  
Collect, store, and review audit logs to support detection, response, and recovery.

9. **Email and web browser protection**  
Harden email and browsers to prevent attacks via phishing, malicious sites, or drive-by downloads.

10. **Malware defenses**  
Deploy and maintain anti-malware tools (e.g., antivirus, EDR) to detect and block malicious software.

11. **Data recovery**  
Develop and test data backup and restoration processes to recover from compromise.

12. **Network infrastructure management**  
Continuously monitor and secure network devices (routers, firewalls, switches).

13. **Network monitoring and defense**  
Establish tools and processes to detect and defend against network-based threats.

14. **Security awareness and skill training**  
Train staff to recognise cyber threats and follow secure practices.

15. **Service provider management**  
Evaluate and monitor third-party providers handling sensitive information.

16. **Application software security**  
Manage the software development lifecycle to identify and fix vulnerabilities early.

17. **Incident response and management**  
Develop and maintain incident response capability to handle attacks effectively.

18. **Penetration testing**  
Regularly test systems and networks to identify weaknesses before attackers do.

**Bottom line – quick deploy**  
Start with Controls 1–6 (asset visibility + access control) — they give the biggest risk reduction.  
Move to 7–10 (vulnerability management, logging, malware, email/browser protection).  
Build incident response (17) and backups (11) next.  
Test regularly (18).  
Use CIS Controls as your practical checklist — they map well to Essential Eight and NIST CSF.  
No need to implement all 18 at once — prioritise based on your environment and threats.  

This section teaches: CIS Controls are a realistic, step-by-step list of what actually stops attacks.  
Implement in order of impact (asset inventory first), then build maturity over time.

**FIELD OPERATIONS MANUAL**  
Defensive Operations Guide for Cyber Defense  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Defensive cyber protocol in high-threat digital environment  

**SECTION 16: IMPORTANCE OF POLICIES AND PROCEDURES**  
-----------------------------------------------------  

**Quick paragraph summary (30-second read)**  
Cyber security is not just technology — it requires clear policies and procedures that everyone in the organisation follows to reduce human error and misuse. Policies create shared rules so employees understand their role in protecting information from attackers. They guide responsible data handling, acceptable device/software use, and secure storage practices. When built inside a framework like the ISM, policies become a consistent, enforceable defence layer. Tools like MFA, antivirus, and application control support these rules, but without policies, tools alone can be bypassed. Bottom line: policies tell people what to do, procedures show how, tools make it enforceable — combine them for real protection.

**Core requirement**  
Organisations must implement a comprehensive security strategy that includes both policies and tools.  
Cyber security policies establish understanding among executives and employees about their role in guarding company information against malicious attackers.

**How policies and procedures protect**  
They guide employees on:  
responsible information sharing and transfer  
acceptable uses of devices, software, and other technologies  
proper ways to handle and store sensitive devices and information.

**Framework foundation**  
Use cyber security frameworks such as the Information Security Manual (ISM) to establish guidelines.  
Aim: safeguard systems and data from attacks.

**Common security-related policies**  
**3-2-1 data backup policy**  
Maintain 3 copies of data.  
Use 2 different types of media.  
Store 1 copy offline.  
This survives ransomware (offline copy intact) and allows clean system restore after rootkits or compromise.

**Device and network security policy**  
Manage regular updates.  
Deploy firewalls and spam filters.  
Encrypt network data so intercepted information is unreadable.  
These reduce risks from vulnerable software and protect data in transit or breach.

**Passcode management policy**  
Enforce strong rules: minimum length, complexity, regular expiry.  
Prevents brute-force attacks on default or weak passcodes.  
Blocks credential theft attempts.

**Supporting security tools**  
Multi-Factor Authentication (MFA) – requires multiple identity proofs, blocks stolen credential use.  
Email scanners and antivirus – detect malware in attachments and links.  
Application control (e.g. Windows Defender) – only allow approved software, prevents infected files from running.

**NIST Cybersecurity Framework role**  
Provides systematic guidance for implementing policies, tools, and procedures.  
Helps align with risk management and regulatory requirements.

**Bottom line – quick deploy**  
Policies = rules everyone follows.  
Procedures = step-by-step instructions.  
Tools = what makes rules work.  
Start with: 3-2-1 backups, MFA, strong passcodes, firewalls, application control.  
Build inside ISM or NIST CSF.  
Train staff and audit compliance — human error is the biggest vulnerability.  

This section teaches: security fails without clear rules.  
Policies turn technology into effective defence.  
Make them simple, enforce them, test regularly.
**SECTION 17: MITRE ATT&CK & CYBER KILL CHAIN**  
------------------------------------------------  


**SECTION 17: CYBER KILL CHAIN & ATT&CK INTRODUCTION**  
-----------------------------------------------------  

**Quick paragraph summary (30-second read)**  
Cyberattacks follow predictable patterns that defenders can map and disrupt. The **Cyber Kill Chain** (Lockheed Martin, 2011) describes 7 linear stages attackers typically go through, from initial scouting to final objective — giving defenders clear points to prevent, detect, or stop the attack early. **MITRE ATT&CK** is a detailed, real-world catalog of adversary tactics, techniques, and procedures (TTPs) observed in actual attacks, helping defenders build detection rules and understand attacker behavior. Both frameworks help shift from reactive to proactive defense by showing what attackers do and where to intervene. Bottom line: use Kill Chain to understand attack flow and break it early; use ATT&CK to know exactly what to look for in logs and alerts.

**Cyber Kill Chain – Lockheed Martin (2011)**  
Military-inspired model adapted to cyber.  
Shows 7 stages attackers usually follow.  
Goal: identify and interrupt the chain before damage occurs.  
Not every attack completes all stages — depends on objective (e.g., DDoS stops at delivery, espionage continues to actions).  

**7 Stages of the Cyber Kill Chain**  
1. **Reconnaissance**  
Attacker gathers intel on target.  
Difficult for defenders to detect, but prevention possible.  
Activities include: harvesting email addresses, identifying employees, discovering internet-facing servers, using insiders, considering BYOD or USB vectors.  
Defender action: if recon detected, build targeted defences (tech + people).

2. **Weaponisation**  
Attacker prepares payload (e.g., custom malware, exploit kit).  
Defender action: build detection mechanisms and analysis to identify weaponisation signatures.

3. **Delivery**  
Attacker launches the attack — payload reaches target.  
First point defenders can actively block.  
Defender action: focus on blocking delivery vectors (email filters, web blocks, USB restrictions).

4. **Exploitation**  
Payload exploits a vulnerability (human, software, hardware).  
Defender action: preventive measures including training, vulnerability scanning, email scanning, behavioural analysis.

5. **Installation**  
Attacker installs payload (backdoor, web shell, persistence).  
Defender action: application control to block unknown software, log and analyse installations, create new mitigations.

6. **Command & Control (C2)**  
Malware phones home — attacker gains remote control.  
Defender's last chance to stop the attack.  
Defender action: block C2 channels (network monitoring, DNS filtering, firewall rules).

7. **Actions on Objectives**  
Attacker achieves goal (data theft, encryption, destruction).  
Defender goal: minimise damage, regain control quickly.  
Longer this stage lasts → greater harm.  
Defender action: rapid containment, eradication, recovery.

**MITRE ATT&CK Framework**  
Living knowledge base of real-world adversary TTPs (tactics, techniques, procedures).  
Non-linear — attackers can skip, repeat, or combine stages.  
Used for threat hunting, detection engineering, incident response, and mapping observed activity.  
Key matrices: Enterprise, Mobile, ICS, PRE-ATT&CK (pre-compromise).  

**Bottom line – quick deploy**  
Cyber Kill Chain = 7-step linear map — great for understanding attack progression and early blocking (focus on recon → delivery).  
MITRE ATT&CK = detailed TTP catalog — great for detection rules and knowing exactly what adversaries do in the wild.  
Use both: Kill Chain for big-picture strategy, ATT&CK for precise indicators and hunting.  
For TAFE: memorise the 7 Kill Chain stages (exam favourite) and understand ATT&CK as the "real-world attacker playbook" used by professionals.  
Deploy tip: map your alerts/incidents to ATT&CK techniques → see where they sit in Kill Chain → prioritise defence accordingly.  

This section teaches: attackers follow patterns — map them with Kill Chain (flow) and ATT&CK (details) to predict, detect, and stop attacks early.  
Know the 7 stages cold.  
ATT&CK shows you what to actually look for in logs and behaviour.

**SECTION 17A: MITRE ATT&CK & CYBER KILL CHAIN**  
------------------------------------------------  

**Quick paragraph summary (30-second read)**  
MITRE ATT&CK is a detailed, real-world knowledge base of how attackers actually operate — it lists 14 major tactics (goals) and hundreds of techniques (methods) they use across the attack lifecycle. Unlike the linear Cyber Kill Chain, ATT&CK is non-linear and focuses on observed adversary behaviour, making it better for detection, threat hunting, and response. The 14 tactics describe the "why" (e.g., gain initial access, maintain persistence), while techniques describe the "how" (e.g., phishing emails, credential dumping). Both frameworks help defenders understand attacker methods and build stronger defences. Bottom line: use Cyber Kill Chain for attack flow and early prevention; use MITRE ATT&CK for precise detection of what attackers are doing right now.

**MITRE ATT&CK Framework**  
Robust way to categorise and understand cyberattacks.  
Uses matrices of tactics and techniques.  
Tactics = high-level attacker goals.  
Techniques = specific methods used to achieve each tactic.  
Better than linear models like Cyber Kill Chain because attacks don't always follow a fixed order.

**The 14 Tactics (Enterprise Matrix)**  
**Reconnaissance**  
Attackers collect data to plan the attack (e.g., OSINT, scanning).  

**Resource Development**  
Attackers build or acquire resources to support the attack (e.g., buy domains, develop tools).  

**Initial Access**  
Attackers gain first foothold in the target environment (e.g., phishing, exploit public-facing apps).  

**Execution**  
Attackers run malicious code on victim systems (e.g., PowerShell, rundll32).  

**Persistence**  
Attackers maintain access even after reboots or credential changes (e.g., registry run keys, scheduled tasks).  

**Privilege Escalation**  
Attackers gain higher permissions (e.g., exploit vulnerabilities, token impersonation).  

**Defence Evasion**  
Attackers avoid detection (e.g., obfuscation, disabling security tools).  

**Credential Access**  
Attackers steal account names and passwords (e.g., LSASS dumping, keylogging).  

**Discovery**  
Attackers learn about the internal environment (e.g., network scanning, account enumeration).  

**Lateral Movement**  
Attackers move through the network to reach high-value assets (e.g., RDP, pass-the-hash).  

**Collection**  
Attackers gather data relevant to their objective (e.g., screen capture, file staging).  

**Command and Control**  
Attackers establish and maintain remote control over compromised systems (e.g., C2 channels, DNS tunnelling).  

**Exfiltration**  
Attackers move collected data out of the target (e.g., over C2, cloud storage).  

**Impact**  
Attackers disrupt availability or integrity (e.g., ransomware encryption, data destruction).  

**Using MITRE ATT&CK**  
Build detection rules based on techniques.  
Map observed activity (logs, alerts) to specific tactics/techniques.  
Improve threat hunting, incident response, and defensive gap analysis.  
Regularly updated with new real-world observations.

**Comparison with Cyber Kill Chain**  
Cyber Kill Chain: linear 7-stage model (recon → weaponisation → delivery → exploitation → installation → C2 → actions).  
Good for understanding attack progression and early prevention.  
MITRE ATT&CK: non-linear, behaviour-focused matrix.  
Better for detection of advanced or non-standard attacks that skip stages.  
Use both: Kill Chain for strategy, ATT&CK for tactics/techniques details.

**Bottom line – quick deploy**  
Memorise the 14 tactics — they are the attacker’s main goals.  
When you see suspicious activity, map it to an ATT&CK tactic/technique.  
Build detections and hunting queries around high-risk techniques (e.g., credential access, lateral movement).  
For TAFE: know ATT&CK is a living matrix of real attacker methods (not theoretical), and it complements the Cyber Kill Chain by being more flexible and detailed.  
Quick memory aid: Recon → Resource → Initial Access → Execution → Persistence → Privilege Escalation → Defence Evasion → Credential Access → Discovery → Lateral Movement → Collection → C2 → Exfiltration → Impact.  

This section teaches: attackers use repeatable patterns — MITRE ATT&CK documents them so you can detect and stop them.  
It's the industry standard for understanding adversary behaviour.  
Know the 14 tactics — they appear in exams and real incident reports.
