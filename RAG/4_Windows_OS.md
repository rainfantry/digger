SECTION 1: INSTALLATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Installation begins with verifying hardware meets Windows 11 minimums like 64-bit CPU (1GHz, 2+ cores), 4GB RAM, 64GB storage, DirectX 12 graphics, and 720p display—aim higher for performance. Hardening per ACSC includes enabling Defender AV, MFA, firewall, patches, logging, and BitLocker to reduce threats. Methods: upgrade from eligible Windows 10 via Settings > Update & Security > Windows Update; download ISO from Microsoft for media/VM; or use Media Creation Tool for bootable USB/DVD, with license purchase, backups, BIOS boot config, and guided setup.

**Hardware requirements**  
Windows 11: 64-bit processor ≥1GHz with 2+ cores, ≥4GB RAM, ≥64GB storage (HDD/SSD), DirectX 12/WDDM 2.x graphics, ≥720p display.  
Windows 10: ≥1GHz processor/SoC, 1GB RAM (32-bit)/2GB (64-bit), 16GB storage (32-bit)/20GB (64-bit), DirectX 9/WDDM 1.0 graphics, ≥800x600 display. Exceed minimums; app-specific needs may apply.

**Hardening measures**  
- Enable Defender or third-party AV  
- Strong passwords + MFA  
- Disable unused services/protocols/features  
- Configure firewall  
- Apply patches/updates  
- Set event logging/monitoring  
- Enable BitLocker encryption  

**Installation methods**  
1. Upgrade: Check eligibility in Settings > Update & Security > Windows Update.  
2. ISO download: Multi-edition from Microsoft; create bootable media or VM.  
3. Media creation: Download tool; select "Create installation media"; choose language/edition/architecture; USB/DVD option (burn ISO if DVD).  

**Setup steps**  
- Purchase license (volume/retail/education).  
- Backup files (install wipes drive).  
- Set BIOS to boot from media; disable Secure Boot if needed.  
- Insert USB/DVD, restart, select language/time/keyboard.  
- Click Install; OS deploys.

SECTION 2: FILE SYSTEM  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
NTFS serves as Windows' default file system since 2001, organising all data through a central Master File Table (MFT) that tracks file attributes including type, size, creation date, memory location, and access permissions. This differs from Unix-like systems where everything is treated as a file, as NTFS embeds all information within files themselves. Key objectives include enhanced reliability via journaling and error detection, stronger security through permissions and encryption support, and scalability for massive volumes up to 8 petabytes. Cluster sizes define the minimum disk allocation unit, balancing efficiency for large files against potential slack space waste. Operators should select cluster configurations based on typical file sizes to optimise storage without excess fragmentation.

**Core structure**  
NTFS assumes everything exists within files; MFT acts as the master index for all metadata.

**Key improvements over prior systems**  
- **Reliability**: Employs log files and checkpoints for automatic file restoration after system failures; continuously scans and relocates data from corrupted clusters.  
- **Security**: Applies granular permissions and ACLs to files/folders; integrates with BitLocker for full-disk encryption to protect sensitive data.  
- **Scale**: Supports adjustable cluster sizes enabling files up to 8PB, accommodating enterprise-level storage needs.

**Cluster mechanics**  
Clusters represent the smallest allocatable disk space; larger sizes (e.g., 4KB) facilitate huge files but generate slack (unused space within clusters).  
Example: A 1KB file in a 4KB cluster occupies the full cluster, wasting 3KB; a 1KB cluster wastes nothing but limits max file size.  
Defensive tip: Tune clusters to workload—small for numerous tiny files, larger for bulk data to minimise waste and maintain performance.

SECTION 3: SYSTEM TOOLS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Windows provides built-in tools accessible primarily through GUI interfaces like Start menu, Settings, or Control Panel to minimise direct file system navigation risks in C:\Windows\System32. Security category includes Windows Security app for centralised threat, firewall, and device health monitoring with scan capabilities; optional Kali Linux integration via WSL2 or VMs for advanced pentesting; and Microsoft Defender Antivirus using machine learning for constant background threat detection and response. Memory tools feature Windows Memory Diagnostic for RAM fault testing and Disk Cleanup to remove temporary and unnecessary system files. Performance monitoring encompasses Task Manager for real-time CPU, memory, and process management; Resource Monitor for detailed service and process resource usage; and Performance Monitor for visualising current system issues. Defensive operators should prioritise GUI access to reduce exposure and integrate tools into regular endpoint monitoring workflows for early anomaly detection.

**Security and scanning**  
- **Windows Security app**: Serves as dashboard aggregating virus protection, account security, firewall status, app/browser controls, device performance, and usage management; flags required actions and initiates system scans.  
- **Kali Linux**: Not native but addable via separate install, VM (Hyper-V/VirtualBox/VMware), or WSL2 (enable feature in Windows, install from Microsoft Store); access through terminal for security scanning and testing tools.  
- **Microsoft Defender Antivirus**: Employs big data and ML for automated threat scanning and response; runs persistently in background; supplement with third-party AV for enhanced detection if mission requires.

**Memory management**  
- **Windows Memory Diagnostic**: Executes RAM integrity tests to identify hardware faults causing erratic behavior.  
- **Windows Disk Cleanup**: Targets and removes temporary files, system caches, and obsolete data to reclaim storage space efficiently.

**Performance management**  
- **Resource Monitor**: Delivers real-time breakdowns of processes and services consuming system resources.  
- **Performance Monitor**: Provides graphical views of operational metrics to spot performance bottlenecks or anomalies.  
- **Windows Task Manager**: Monitors CPU, memory, disk, and network usage; enables viewing and terminating resource-heavy processes or applications.


SECTION 4: MANAGING USERS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Windows administrators manage users through Settings > Accounts > Family & other users, creating accounts linked to existing Microsoft credentials, new Microsoft registrations via email, or local device-only profiles without Microsoft ties. Account types default to standard for daily use with elevated admin options available, alongside permission controls to enforce least privilege. Management includes editing types/names, deletions, disables/enables. In enterprise environments, Active Directory centralises authentication for domain accounts controlling network resources like files/printers/apps; Azure AD extends to cloud services with hybrid on-prem integration for unified access. Defensive strategy emphasises standard accounts, MFA enforcement, and auditing to prevent privilege escalation.

**Account creation methods**  
- Link to existing Microsoft account.  
- Create new Microsoft account via email registration.  
- Set up local account unlinked to Microsoft.

**Management controls**  
- Assign standard or administrator types.  
- Designate specific permissions levels.  
- Change account names or types.  
- Delete, temporarily disable, or enable accounts.

**Enterprise integration**  
- Active Directory: Directory service for centralised auth/authorisation on Windows networks; manages domain accounts and resources.  
- Azure AD: Cloud-based identity management for user accounts and app access; integrates with on-prem Active Directory for hybrid environments.  
- Domain accounts: Handled by domain controllers; provide controlled access to shared resources like files, printers, applications.

SECTION 5: PREVENTIVE MAINTENANCE  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Preventive maintenance ensures Windows endpoint resilience through routine tasks that close vulnerabilities and maintain performance. Core activities include software updates to patch unknown exploits, data backups for recovery from failures or attacks, antivirus scans to detect threats early, file cleanups to free space especially on constrained drives, and weekly restarts to clear memory leaks while shutting down idle systems to block unauthorised access. Defensive operators prioritise patching as the primary barrier against intrusions; maintain immutable backups offsite; adapt cleanup and restart frequency to usage patterns for optimal security without operational disruption.

**Key tasks**  
- **Software updates**: Apply regularly to fix hidden vulnerabilities; critical for attack prevention.  
- **Data backups**: Create consistent copies; restore minimises impact from infiltration or hardware failure.  
- **Antivirus scans**: Schedule frequent runs; early detection limits virus damage.  
- **File cleanups**: Remove temps and empty Recycle Bin; increase frequency on low-storage devices to avoid clutter.  
- **Device restarts**: Weekly for daily use; clears RAM issues post-app closure; required after installs or slowdowns.

**Security considerations**  
Shutdown when not in use to deny persistence opportunities for threats. Balance tasks with system demands—over-maintenance can disrupt workflows, but under-maintenance exposes risks.

SECTION 6: TROUBLESHOOTING  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Windows includes built-in troubleshooters for common issues like internet connections, audio, printers, and networking, accessed via Settings > System > Troubleshoot > Other troubleshooters to automate diagnostics and fixes. Preventive maintenance reduces frequency of problems; when errors occur (e.g., update failures), run targeted tools followed by restarts. Defensive operators use these for quick resolution while preserving logs for root cause analysis, avoiding manual tweaks that could introduce new vulnerabilities.

**Tools overview**  
- Specific fixers handle frequent categories: internet, audio, printer, networking, Windows Update.  
- Guided walkthroughs from Microsoft provide step-by-step alternatives.  
- Integration with Event Viewer logs helps correlate errors.

**Example workflow**  
1. Navigate to Settings > System > Troubleshoot > Other troubleshooters.  
2. Select relevant fixer (e.g., Windows Update > Run).  
3. Follow prompts; restart system.  
4. Verify resolution (e.g., recheck updates).  

**Defensive considerations**  
Prioritise built-in tools to maintain system integrity; document errors for patterns indicating deeper threats like malware.
