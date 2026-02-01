FIELD OPERATIONS MANUAL  
Defensive Operations Guide for VIRTUALISATION TECHNOLOGIES  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Deliver field-ready reference for understanding, deploying, and securing virtualisation environments to support isolation, testing, and rapid recovery while mitigating hypervisor and VM escape risks.



FIELD OPERATIONS MANUAL  
Defensive Operations Guide for VIRTUALISATION READINESS ASSESSMENT  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Map operator self-assessed knowledge statements to defensive virtualisation competencies, verify coverage, and highlight actionable next steps for mission-critical application.

**Quick paragraph summary (30-second read)**  
Operator has declared operational understanding across nine core virtualisation domains critical for secure deployment and defence. All listed statements align with defensive priorities: isolation, resilience, recoverability, and controlled exposure. This manual structures the self-assessment under exact headings provided, confirms defensive relevance, and flags any implicit gaps requiring field validation through hands-on execution.

SECTION 1: BENEFITS AND CHALLENGES OF VIRTUALISATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator confirms comprehension of virtualisation’s dual nature: efficiency, cost reduction, isolation, and flexibility versus added complexity, performance overhead, and new attack vectors. Defensive value lies in strong isolation outweighing most risks when properly configured.

- **Defensive benefit emphasis** – containment of compromise, rapid provisioning, snapshot rollback  
- **Key challenge awareness** – hypervisor becomes single point of catastrophic failure if breached  

SECTION 2: TYPES OF VIRTUALISATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator knows major virtualisation categories (server, desktop, network, storage, application/container). Defensive operators primarily leverage server/desktop virtualisation for isolation and containerisation for lightweight, ephemeral workloads.

- Server/desktop virtualisation → primary defensive use (full VM isolation)  
- Container/virtualisation (Docker, Podman) → secondary, higher density but weaker isolation  

SECTION 3: DIFFERENCE BETWEEN TYPE 1 AND TYPE 2 HYPERVISORS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator understands Type 1 (bare-metal) runs directly on hardware for maximum performance and security, while Type 2 (hosted) runs atop a general-purpose OS and inherits its vulnerabilities. Type 1 remains the defensive standard for production and high-threat environments.

**Defensive priority**  
- Prefer **Type 1** (ESXi, Hyper-V, KVM) for hardened, minimal-attack-surface deployments  
- Restrict **Type 2** (VirtualBox, Workstation) to lab/testing only  

SECTION 4: SNAPSHOTS AND BACKUPS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator differentiates snapshots (fast, point-in-time VM state capture for rollback) from backups (durable, offline copies for disaster recovery). Both are essential defensive tools for rapid incident response and data protection.

- **Snapshots** – tactical, short-term revert (malware testing, patch rollback)  
- **Backups** – strategic, long-term recovery (ransomware, hardware failure)  

SECTION 5: BENEFITS OF HIGH AVAILABILITY IN VIRTUALISATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator recognises HA delivers automatic failure detection, VM migration, and near-zero unplanned downtime. In defensive operations, HA ensures continuity during host compromise, maintenance, or attack-induced failure.

**Core HA defensive values**  
- Automatic failover preserves operational capability  
- Live migration enables host evacuation without service loss  
- Reduced dependency on single hardware point  

SECTION 6: NESTING OF VIRTUALISATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator knows nested virtualisation allows VMs to run inside other VMs, enabling complex test/dev scenarios. Defensive trade-off is increased performance penalty and expanded attack surface—enable only when mission requires.

**Defensive control**  
- Disable nested virtualisation by default  
- Enable only for specific lab/pentest VMs with strict network isolation  

SECTION 7: SECURITY MONITORING OF VIRTUAL MACHINES  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator understands VM monitoring is mandatory due to expanded threat surface (malware, escape attempts, lateral movement). Effective monitoring detects anomalies across host, hypervisor, and guest layers.

**Monitoring priorities**  
- Centralised log collection (hypervisor + guests)  
- Anomaly detection on resource usage (CPU spikes, unexpected network)  
- Integrity checks on VM configurations and snapshots  

SECTION 8: SETTING UP A VIRTUAL MACHINE ON LOCAL COMPUTER  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator knows the practical steps to deploy a local VM using Type 1 or Type 2 hypervisors. Defensive setup demands hardened defaults, minimal attack surface, and isolation from production networks.

**Hardened local VM creation checklist**  
1. Select Type 1 when possible (Hyper-V, KVM)  
2. Use verified OS images only  
3. Disable clipboard sharing, drag-drop, USB passthrough  
4. Assign NAT or host-only networking  
5. Enable guest encryption and Secure Boot  
6. Patch guest immediately post-install  

SECTION 9: IMPORTANCE OF VIRTUAL MACHINE NETWORKING  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Operator grasps that virtual networking controls communication paths between VMs, host, and external networks. Proper configuration enforces segmentation, prevents lateral movement, and limits breach scope.

**Defensive networking principles**  
- Default to **NAT** or **host-only** for testing/malware analysis  
- Use **bridged** only when external exposure required  
- Apply virtual firewalls and micro-segmentation  
- Monitor east-west traffic for unexpected VM-to-VM communication  

SECTION 10: OVERALL READINESS & NEXT OPERATIONAL STEPS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Self-assessment indicates high theoretical readiness across all assessed domains. Defensive maturity now depends on practical validation: deploy, harden, test compromise scenarios, and recover using documented procedures.

**Immediate field actions**  
1. Build one hardened test VM using preferred hypervisor  
2. Implement full isolation (host-only network, no shared folders)  
3. Take snapshot → introduce controlled “compromise” → revert  
4. Simulate backup/restore cycle  
5. Validate monitoring detects anomalous guest behavior  

End of manual section – virtualisation readiness assessment complete. Operator cleared for practical application phase.



**Quick paragraph summary (30-second read)**  
Virtualisation abstracts physical hardware via hypervisors to run multiple isolated VMs on one host, improving resource efficiency, enabling testing, and supporting cloud services (IaaS/PaaS/SaaS). Type 1 (bare-metal) hypervisors offer better performance and security than Type 2 (hosted). Key defensive advantages include strong isolation, snapshots for rollback, and high availability; risks include hypervisor compromise, VM escape, and nested virtualisation complexity. Proper configuration and monitoring are critical to prevent lateral movement or data exfiltration.

SECTION 1: VIRTUALISATION CORE CONCEPTS & USE CASES  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Virtualisation creates isolated compute environments (VMs) that emulate full hardware stacks. Primary drivers are cost reduction, flexibility, and security via isolation. Defensive operators use VMs for malware analysis, pentesting, OS experimentation, and secure development without risking host integrity.

**Primary operational uses**  
- Safe testing of untrusted code or malware  
- Multi-OS development and compatibility testing  
- Isolated network segments for sensitive data  
- Rapid rollback via snapshots  
- Pentesting tool deployment without host contamination  
- Resource optimisation on single hardware  

SECTION 2: HYPERVISOR TYPES – TYPE 1 vs TYPE 2  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Type 1 hypervisors run directly on hardware (bare-metal), providing superior performance, isolation, and security. Type 2 hypervisors run as applications atop a host OS, offering easier setup but larger attack surface. Type 1 is preferred for production and high-security environments.

**Comparison table**

| Characteristic       | Type 1 (Bare-metal)                  | Type 2 (Hosted)                     |
|----------------------|--------------------------------------|-------------------------------------|
| Installation         | Directly on hardware                 | On top of host OS                   |
| Performance          | Higher (direct hardware access)      | Lower (OS scheduling overhead)      |
| Security             | Stronger isolation                   | Weaker (host OS compromise → all VMs) |
| Attack surface       | Smaller (no host OS)                 | Larger (host OS + hypervisor)       |
| Common products      | VMware ESXi, Microsoft Hyper-V, Xen  | VirtualBox, VMware Workstation, Parallels |

**Defensive recommendation**  
Prioritise Type 1 for production and security-sensitive deployments. Minimise Type 2 usage to lab/testing only.

SECTION 3: VIRTUALISATION SECURITY BENEFITS & RISKS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Isolation is the cornerstone defensive benefit—VM escape remains rare but catastrophic. Additional risks include misconfigured networking, shared storage vulnerabilities, and hypervisor exploits. Snapshots and backups enable rapid recovery but can also preserve malware if not handled correctly.

**Key defensive advantages**  
- Strong VM isolation prevents lateral movement  
- Snapshots allow instant rollback from compromise  
- High availability features reduce single points of failure  
- Easy replication for disaster recovery  

**Major risks**  
- Hypervisor exploits → full host compromise  
- VM escape (rare, high-impact)  
- Shared resource side-channels (cache, network)  
- Nested virtualisation → increased complexity & escape paths  
- Snapshot retention of sensitive data or malware  

SECTION 4: SNAPSHOTS, BACKUPS & HIGH AVAILABILITY  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Snapshots capture point-in-time VM states for fast rollback. Backups provide offline, durable copies for disaster recovery. High availability clusters detect failures and automatically migrate VMs. Defensive use requires immutable backups and controlled snapshot management.

**Operational distinctions**  
- **Snapshot** – quick, disk-space efficient, revertible state (use for testing)  
- **Backup** – full/offline copy, slower restore, essential for recovery  

**High availability features**  
- Automatic failure detection & VM migration  
- Live migration (vMotion / live migration)  
- Redundant hosts & shared storage  

SECTION 5: NESTED VIRTUALISATION & CLOUD INTEGRATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Nested virtualisation runs VMs inside VMs—useful for dev/test but increases performance penalty and attack surface. Cloud IaaS (AWS EC2, Azure VMs) delivers virtualisation at scale with managed hypervisors. Defensive operators use cloud VMs for disposable analysis environments.

**Defensive considerations**  
- Enable nested virtualisation only when required (VT-x/AMD-V + EPT)  
- Use cloud VMs for high-risk tasks to avoid local contamination  
- Monitor for unexpected nested layers (potential evasion technique)  

SECTION 6: VIRTUAL NETWORKING & ISOLATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Virtual networks emulate switches, routers, and firewalls in software. Proper segmentation prevents VM-to-VM and VM-to-host attacks. Common modes include bridged (direct LAN), NAT (isolated outbound), host-only (lab isolation).

**Defensive network modes**  
- **Host-only** – maximum isolation, no external access  
- **NAT** – outbound internet, inbound blocked (default safe)  
- **Bridged** – VM appears on physical LAN (use with caution)  
- **Internal** – VM-to-VM only, no host access  

**Security controls**  
- Enable MAC address filtering  
- Use virtual firewalls (e.g., pfSense VM)  
- Disable promiscuous mode unless required  
- Segment via VLANs or SDN policies  

SECTION 7: VM SECURITY MONITORING & HARDENING CHECKLIST  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Monitor VMs like physical hosts: patch OS/apps, restrict services, log centrally. Watch hypervisor logs for anomalies. Harden by disabling unused devices, enforcing least privilege, and using immutable templates.

**Priority hardening steps**  
1. Keep hypervisor & guest OS fully patched  
2. Enable Secure Boot in guests where supported  
3. Disable copy-paste / drag-drop between host & guest  
4. Use dedicated management network for hypervisor  
5. Centralise logs (SIEM) from hypervisor & guests  
6. Regularly scan for rogue VMs / snapshots  
7. Restrict USB / removable media passthrough  
8. Implement mandatory VM encryption (at rest & in transit)  

End of manual section – virtualisation reference complete.
