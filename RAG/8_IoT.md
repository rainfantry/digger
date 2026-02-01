
FIELD OPERATIONS MANUAL
Defensive Operations Guide for INTERNET OF THINGS (IoT)
CLASSIFICATION: PERSONAL USE ONLY
Operator: 22DIV / Callsign: Digger
Purpose: Extract and structure IoT fundamentals, device types, security vulnerabilities, and connectivity technologies for defensive assessment and network segmentation planning.

***

## **TABLE OF CONTENTS**

SECTION 1: I understand what Internet of Things (IoT) is.
SECTION 2: I know which devices use IoT.
SECTION 3: I have a good understanding of the security vulnerabilities surrounding IoT.
SECTION 4: I understand the difference between narrowband Internet of Things (NB-IoT) and long range Internet of Things (LoRa).
SECTION 5: I understand IoT defensive architecture and threat mitigation strategies (RECAP).

***

## SECTION 1: I understand what Internet of Things (IoT) is.

This section defines IoT so you can quickly classify any "smart" device and understand its network footprint. IoT devices are computers first, appliances second—and they expand your attack surface by bringing IP connectivity to everything from lightbulbs to industrial sensors.

**What is IoT?**

- Network of physical devices ("things") embedded with sensors, software, and connectivity to collect and exchange data.
- Devices connect to the internet or local networks to enable remote monitoring, control, and automation.
- Ranges from consumer devices (smart home) to industrial systems (SCADA, IIoT).
- Key characteristics: always-on connectivity, often autonomous, typically resource-constrained (low CPU/memory).

**Core components of IoT systems:**

- **Sensors/actuators**: Collect data (temperature, motion, location) or perform actions (unlock door, adjust thermostat).
- **Embedded processors**: Run firmware/OS; handle local logic and communication.
- **Connectivity**: Wi-Fi, Bluetooth, Zigbee, Z-Wave, cellular (NB-IoT, LTE-M), LoRa/LoRaWAN.
- **Cloud/edge services**: Backend platforms for data storage, analytics, remote control.
- **Mobile/web apps**: User interfaces for monitoring and control.

**Common IoT use cases:**

- Smart homes: thermostats, lights, locks, cameras, speakers, appliances.
- Wearables: fitness trackers, smartwatches, medical monitors.
- Smart cities: traffic sensors, parking meters, environmental monitors.
- Industrial IoT (IIoT): manufacturing sensors, predictive maintenance, supply chain tracking.
- Healthcare: patient monitors, infusion pumps, connected medical devices.
- Agriculture: soil sensors, automated irrigation, livestock tracking.

**Defensive controls:**

- Treat every IoT device as a **potential pivot point** into your network; assume it will be compromised.
- Default mindset: IoT devices are **untrusted endpoints** until proven otherwise.
- Never place IoT on the same subnet as critical systems (workstations, servers, admin systems).
- Understand that IoT often means **permanent connectivity with weak or no authentication**—plan accordingly.

***

## SECTION 2: I know which devices use IoT.

This section gives you a categorized inventory of common IoT devices so you can rapidly identify them during network assessments and understand their typical connectivity and risk profiles.

**Consumer/smart home IoT:**

- Smart speakers: Amazon Echo, Google Home, Apple HomePod.
- Smart displays: Google Nest Hub, Echo Show.
- Smart thermostats: Nest, Ecobee, Honeywell.
- Smart lighting: Philips Hue, LIFX, smart switches.
- Smart locks: August, Yale, Schlage electronic locks.
- Security cameras/doorbells: Ring, Arlo, Nest Cam, Wyze.
- Smart TVs and streaming devices: Smart TVs, Roku, Chromecast, Apple TV.
- Smart appliances: refrigerators, ovens, washing machines, vacuums (Roomba).
- Smart plugs/outlets: TP-Link, Wemo, smart power strips.

**Wearables and personal IoT:**

- Fitness trackers: Fitbit, Garmin, Whoop.
- Smartwatches: Apple Watch, Samsung Galaxy Watch, Wear OS devices.
- Medical wearables: continuous glucose monitors, heart rate monitors, sleep trackers.

**Enterprise and commercial IoT:**

- Access control systems: badge readers, electronic locks, turnstiles.
- Environmental sensors: temperature, humidity, air quality monitors.
- Occupancy sensors: motion detectors, people counters.
- Digital signage: networked displays, interactive kiosks.
- VoIP phones and conference systems: networked voice devices.
- Printers and multifunction devices (often overlooked as IoT).

**Industrial IoT (IIoT):**

- SCADA systems: industrial control systems for utilities, manufacturing.
- Programmable Logic Controllers (PLCs): factory automation.
- Remote Terminal Units (RTUs): monitoring in oil/gas, water treatment.
- Industrial sensors: pressure, flow, vibration, temperature sensors.
- Connected heavy machinery: predictive maintenance sensors.

**Healthcare IoT (IoMT - Internet of Medical Things):**

- Patient monitors: heart rate, blood pressure, pulse oximetry.
- Infusion pumps: IV medication delivery.
- Diagnostic equipment: connected MRI, CT, X-ray machines.
- Wearable medical devices: insulin pumps, pacemakers.

**Automotive and transportation IoT:**

- Connected cars: telematics, infotainment, OTA updates.
- Fleet tracking: GPS trackers, dash cams.
- Electric vehicle chargers: networked EV charging stations.

**Defensive controls:**

- Maintain an **IoT device inventory** with: device type, manufacturer, firmware version, network connectivity, protocols used.
- Classify devices by **risk tier**: Tier 1 (low-risk: smart bulbs), Tier 2 (medium: cameras, thermostats), Tier 3 (high-risk: locks, medical devices, industrial controls).
- Prioritize segmentation and monitoring for **Tier 2-3 devices**; they can cause physical harm or data breaches.
- Assume **smart TVs, cameras, and speakers** are recording; never place them in secure spaces (conference rooms, offices with sensitive discussions).
- For industrial/medical IoT, apply **air-gapping or strict VLANs** with unidirectional data flows where possible.

***

## SECTION 3: I have a good understanding of the security vulnerabilities surrounding IoT.

This section catalogs the fundamental weaknesses that make IoT a persistent security nightmare. Understanding these vulnerabilities helps you design segmentation, monitoring, and incident response strategies before devices are deployed—not after they're compromised.

**Core IoT security vulnerabilities:**

- **Weak/default credentials**: Many devices ship with hardcoded or easily guessable passwords (admin/admin, root/root); users rarely change them.
- **No authentication**: Some devices allow unauthenticated access to web interfaces or APIs.
- **Insecure communications**: Cleartext protocols (HTTP, Telnet, unencrypted MQTT); credentials and data transmitted in the clear.
- **Lack of encryption**: Data at rest often unencrypted; firmware images and configs extractable.
- **Outdated/vulnerable firmware**: Manufacturers rarely provide updates; devices run ancient, unpatched OS/software.
- **No update mechanism**: Some devices cannot be patched; others require manual, complex update processes.
- **Insecure APIs**: Cloud/mobile APIs lack proper authentication, allow enumeration, or leak data.
- **Physical security weaknesses**: Devices easily tampered with; UART/JTAG interfaces exposed; firmware can be dumped.
- **Resource constraints**: Limited CPU/memory means no room for security agents, encryption, or proper logging.
- **Poor logging/monitoring**: Minimal or no logs; can't detect compromise or perform forensics.
- **Excessive permissions**: Apps and devices request far more access than needed; cloud services over-privileged.
- **Insecure supply chain**: Backdoors or malware pre-installed by manufacturers or compromised in transit.

**Common IoT attack vectors:**

- **Credential stuffing/brute-force**: Attackers scan for exposed IoT, try default/common passwords.
- **Exploitation of known CVEs**: Unpatched devices with public exploits (Mirai botnet targets).
- **Man-in-the-middle (MITM)**: Intercept/modify unencrypted traffic; steal credentials; inject commands.
- **Firmware extraction and reverse engineering**: Extract firmware from device or download site; find hardcoded keys, backdoors, vulnerabilities.
- **Cloud API abuse**: Enumerate devices via APIs; exploit authentication flaws to control devices remotely.
- **Physical attacks**: Open device, access debug interfaces (UART, JTAG), dump firmware, implant malware.
- **DNS rebinding**: Trick browser into commanding local IoT devices from malicious website.
- **Botnets**: Compromise thousands of IoT devices (cameras, routers) to launch DDoS attacks (Mirai, Hajime).

**Real-world IoT compromise scenarios:**

- **Smart cameras**: Default passwords → attacker views feeds, uses camera as pivot into network.
- **Smart locks**: Weak BLE encryption → attacker clones credentials, gains physical access.
- **Thermostats**: Unauthenticated API → attacker changes settings, reconnaissance of occupancy patterns.
- **Medical devices**: Unpatched vulnerabilities → attacker modifies drug dosages or disables alarms.
- **Industrial sensors**: Compromised → attacker manipulates readings to cause physical damage or hide sabotage.

**Defensive controls:**

- **Change all default credentials** immediately upon deployment; use strong, unique passwords per device.
- **Segment IoT devices** into isolated VLANs; deny lateral movement to corporate/OT networks.
- **Block internet access** for IoT devices where cloud connectivity isn't required; use local control only.
- **Whitelist communications**: Firewall rules to allow IoT only to specific IPs/ports (cloud services); deny all else.
- **Disable unnecessary services**: Turn off UPnP, Telnet, SSH, HTTP if not needed; prefer HTTPS where available.
- **Monitor IoT traffic** for anomalies: unexpected destinations, high bandwidth (DDoS participation), scanning activity.
- **Replace devices that cannot be secured**: If a device has hardcoded credentials, no updates, and is critical → replace or air-gap it.
- **Implement network access control (NAC)**: Use 802.1X to control which devices can join network; quarantine unknown MACs.
- **Regular vulnerability scanning**: Use tools like Nmap, Nessus to identify IoT devices and known CVEs.
- **Assume breach**: Plan incident response for when (not if) IoT devices are compromised; practice isolation and removal.

***

## SECTION 4: I understand the difference between narrowband Internet of Things (NB-IoT) and long range Internet of Things (LoRa).

This section clarifies two major low-power wide-area network (LPWAN) technologies for IoT. Knowing the difference helps you assess connectivity choices, understand deployment constraints, and recognize which protocol is in use when you encounter IoT in the field.

**What are LPWANs?**

- Low-Power Wide-Area Networks: designed for IoT devices that need long range, low data rate, long battery life.
- Trade high bandwidth for extended range (kilometers) and years of battery operation.
- Common use cases: smart meters, environmental sensors, asset tracking, agriculture, smart cities.

**NB-IoT (Narrowband IoT):**

- **Technology**: 3GPP standard; operates on licensed cellular spectrum (LTE bands).
- **Connectivity**: Uses existing cellular infrastructure (mobile network operators like Telstra, Optus, Vodafone).
- **Range**: 1–10 km (urban) to 35 km (rural).
- **Data rate**: Low (up to ~250 kbps downlink, ~20 kbps uplink).
- **Power**: Very low power; devices can run 10+ years on battery.
- **Latency**: Higher latency (1–10 seconds).
- **Security**: Built-in SIM authentication and encryption (cellular network security).
- **Cost**: Requires SIM/subscription; relies on carrier networks.
- **Deployment**: No need to deploy own infrastructure; leverage existing cell towers.

**LoRa/LoRaWAN (Long Range):**

- **Technology**: Proprietary PHY (LoRa) from Semtech; LoRaWAN is the open MAC protocol.
- **Connectivity**: Uses unlicensed ISM bands (915 MHz Australia, 868 MHz Europe, 433 MHz Asia).
- **Range**: 2–5 km (urban) to 15+ km (rural).
- **Data rate**: Very low (0.3–50 kbps).
- **Power**: Extremely low power; 10+ years battery life.
- **Latency**: Low to moderate; depends on network configuration.
- **Security**: AES-128 encryption at network and application layers; device authentication via keys.
- **Cost**: No subscription; you deploy your own gateways or use community/TTN networks.
- **Deployment**: Requires gateway infrastructure (LoRaWAN gateways connect devices to internet).

**Key differences (NB-IoT vs LoRa/LoRaWAN):**


| Feature | NB-IoT | LoRa/LoRaWAN |
| :-- | :-- | :-- |
| Spectrum | Licensed cellular | Unlicensed ISM |
| Infrastructure | Carrier-owned (telco) | Private/community gateways |
| Cost model | Subscription/SIM fees | Hardware cost, no subscription |
| Range | 1–35 km | 2–15+ km |
| Data rate | ~20–250 kbps | 0.3–50 kbps |
| Latency | Higher (1–10s) | Lower (sub-second capable) |
| Security | SIM-based, cellular encryption | AES-128, key-based |
| Deployment | Immediate (if carrier coverage) | Requires gateway deployment |

**When to use NB-IoT:**

- Need guaranteed coverage via existing cellular networks.
- Moderate data requirements; can tolerate latency.
- Prefer not to manage own infrastructure.
- Use cases: smart meters, asset tracking in wide areas.

**When to use LoRa/LoRaWAN:**

- Need private network control; avoid recurring fees.
- Very low data requirements; battery life critical.
- Can deploy own gateways; no carrier coverage available.
- Use cases: agriculture sensors, private industrial networks, community projects.

**Defensive controls:**

- **NB-IoT**: Security relies on carrier; ensure devices use strong SIM PINs; monitor for SIM cloning or swap attacks; validate device certificates.
- **LoRaWAN**: Security is key-based; protect **AppSKey** and **NwkSKey** (AES keys); rotate keys periodically; harden gateway security (SSH, firmware updates).
- **Both**: Segment IoT traffic; never trust device data without validation; assume devices can be physically compromised and keys extracted.
- **Monitor for rogue devices**: In LoRaWAN, watch for unauthorized devices on your network; in NB-IoT, audit SIM inventory.
- **Encrypt end-to-end**: Don't rely solely on link-layer encryption (NB-IoT cellular or LoRaWAN); add application-layer encryption for sensitive data.

***

## SECTION 5: I understand IoT defensive architecture and threat mitigation strategies (RECAP).

This final section consolidates IoT fundamentals, device types, vulnerabilities, and connectivity into a unified defensive posture. The core message: IoT devices are inherently insecure, so your defense must be **network-based segmentation, monitoring, and containment**, not device-based hardening (which is often impossible).

**IoT defensive architecture principles:**

1. **Zero trust for IoT**: Assume every IoT device is compromised from day one.
2. **Segment ruthlessly**: Dedicated VLANs/subnets for IoT; firewall between IoT and everything else.
3. **Default-deny egress**: IoT devices should only talk to explicitly allowed IPs/ports; block all else.
4. **No lateral movement**: IoT VLAN cannot reach corporate, server, or OT networks except via controlled gateways.
5. **Monitor everything**: Log all IoT traffic; alert on anomalies (new destinations, port scans, high volume).

**IoT network segmentation strategy:**

- **Tier 1 (Low-risk IoT VLAN)**: Smart bulbs, speakers, general-purpose sensors.
    - Egress: Internet only (for cloud control); no access to internal networks.
- **Tier 2 (Medium-risk IoT VLAN)**: Cameras, thermostats, smart appliances.
    - Egress: Specific cloud services only (whitelist IPs/domains); deny all other internet; no internal access.
- **Tier 3 (High-risk IoT VLAN)**: Smart locks, medical devices, industrial sensors.
    - Egress: Deny internet; local control only via jump host or secure gateway.
    - Strong access control; 802.1X or MAC whitelisting.
- **Guest IoT VLAN**: Visitor devices, BYOD IoT.
    - Fully isolated; internet-only access; no visibility into any other network.

**Common IoT ports and protocols to monitor/control:**

- **80/443 (HTTP/HTTPS)**: IoT web interfaces; cloud API calls; firmware updates.
    - Defense: Allow only to known cloud IPs; block inbound HTTP/HTTPS from internet.
- **1883/8883 (MQTT)**: Lightweight messaging protocol for IoT.
    - Defense: Use TLS (8883); enforce authentication; segment MQTT broker.
- **5683 (CoAP)**: Constrained Application Protocol for resource-limited devices.
    - Defense: Use DTLS (CoAP over DTLS); firewall to known endpoints.
- **22/23 (SSH/Telnet)**: Device management.
    - Defense: Disable Telnet; restrict SSH to management VLAN only; use key-based auth.
- **161/162 (SNMP)**: Device monitoring.
    - Defense: Use SNMPv3 with encryption; disable SNMPv1/v2c.
- **5353 (mDNS)**: Multicast DNS for local discovery.
    - Defense: Block mDNS at VLAN boundaries to prevent cross-VLAN discovery.
- **Zigbee (802.15.4), Z-Wave (proprietary)**: Low-power mesh protocols.
    - Defense: Secure pairing process; monitor for rogue coordinators; update hub firmware.

**IoT incident response playbook:**

1. **Detection**: Unusual traffic patterns; device scanning; connection to unknown IPs; high bandwidth usage.
2. **Identification**: Which device? What VLAN? What is it trying to do?
3. **Containment**:
    - **Immediate**: Disable switch port or block MAC at switch/firewall.
    - **Short-term**: Move device to quarantine VLAN; capture traffic for analysis.
4. **Eradication**:
    - Factory reset device.
    - Update firmware if available.
    - Change all credentials.
    - If device cannot be secured → **remove from network permanently**.
5. **Recovery**: Re-deploy to appropriate VLAN with stricter firewall rules.
6. **Lessons learned**: What allowed compromise? Tighten segmentation; add detection rules.

**IoT security checklist (deployment and operations):**

- [ ] Change all default credentials before connecting to network.
- [ ] Disable unnecessary services (UPnP, Telnet, unused ports).
- [ ] Update firmware to latest version; check for updates quarterly.
- [ ] Deploy to appropriate VLAN (tier 1/2/3) based on risk.
- [ ] Configure firewall rules: whitelist required destinations, deny all else.
- [ ] Disable internet access if cloud connectivity not required.
- [ ] Enable logging on firewall/switch for IoT VLANs.
- [ ] Document device in inventory: type, IP, MAC, firmware version, cloud services used.
- [ ] Test isolation: Verify IoT device cannot reach corporate/server networks.
- [ ] Schedule periodic scans (Nmap, Nessus) to detect new vulnerabilities or rogue devices.
- [ ] Review IoT traffic logs weekly for anomalies.

**Final operational guidance:**

> "IoT expands your attack surface faster than you can patch it. Segmentation and monitoring are not optional—they are the only effective controls when devices themselves cannot be trusted."

**Defensive controls (final recap):**

- **Never assume IoT devices are secure**; design network architecture to contain compromise.
- **Segment IoT into isolated VLANs** with strict firewall policies; treat IoT subnets as untrusted zones.
- **Default-deny all IoT egress**; whitelist only necessary cloud services and protocols.
- **Monitor IoT traffic continuously**; alert on: new destination IPs, port scans, protocol anomalies, high volume.
- **Inventory and classify** all IoT devices by risk; prioritize high-risk (locks, medical, industrial) for strictest controls.
- **Disable internet access** for IoT devices where possible; prefer local control via secure jump hosts.
- **Plan for compromise**: Have runbooks ready to isolate and remove devices quickly.
- For **LoRaWAN deployments**, secure gateways as critical infrastructure; protect application keys; monitor for rogue devices.
- For **NB-IoT deployments**, audit SIM inventory; monitor for SIM swap attacks; validate device certs.

***

**END OF MANUAL – INTERNET OF THINGS (IoT)**
Operator: 22DIV / Callsign: Digger
Classification: Personal Use Only

