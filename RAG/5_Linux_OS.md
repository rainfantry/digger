FIELD OPERATIONS MANUAL  
Defensive Operations Guide for LINUX OPERATING SYSTEM  
CLASSIFICATION: PERSONAL USE ONLY  
Operator: 22DIV / Callsign: Digger  
Purpose: Extract and structure core Linux knowledge from provided documentation for defensive system administration and pentesting reference.

**Quick paragraph summary (30-second read)**  
Linux, an open-source Unix-like OS created by Linus Torvalds in 1991, powers embedded devices, servers, and cybersecurity tools like Kali for penetration testing. Its structure includes bootloader, kernel (core management), init system, daemons, graphical server, desktop environment, and applications. Key components: monolithic kernel handles hardware; shells like Bash enable command execution; distributions (distros) bundle kernel with tools. File system is hierarchical from root (/), with permissions, links, and commands for navigation/management. Defensive use emphasises secure permissions, scripting for automation, and monitoring via commands to detect anomalies.

SECTION 1: THE HISTORY OF LINUX  
----------------------------------------------

Linux emerged in the 1990s from hobbyist efforts, created by Linus Torvalds as a MINIX-like Unix system while at University of Helsinki. Version 0.02 released 1991; 1.0 in 1994. Integrated with GNU tools from Free Software Foundation (led by Richard Stallman) to form GNU/Linux. Known for efficiency, stability, open-source versatility—from mobiles to supercomputers. Paired with Apache for dominant internet servers.

SECTION 2: FILE SYSTEM  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
The Linux file system organizes storage data in a hierarchical structure starting from the root directory (/), enabling efficient management of file names, sizes, creation dates, and metadata. It categorizes everything as files—regular (text or executables), directories (containers for other files), special (like pipes for networking), and links (references to files or dirs). Partitions divide drives into data areas (with root for booting) and swap for virtual memory extension. The Filesystem Hierarchy Standard (FHS) defines standard directories like /bin for executables and /etc for configs. Paths are absolute (from root) or relative (from current dir), with strict permissions controlling read/write/execute access across user/group/others. Defensive admins use this structure to isolate sensitive data, enforce least privilege, and monitor for unauthorized changes via commands like ls -l.

**Core mechanics**  
Hierarchical layout from root (/); child directories and partitions mounted under it. Namespace governs naming and organization; metadata tracks size, modification/creation dates, ownership. Built for non-volatile storage control, with data structures for free/used space and regions (volumes/partitions).

**File categories explained**  
- Regular/plain: Standard data files (e.g., text documents or binaries).  
- Directories: System containers holding other files; accessed via paths like /var/log.  
- Special: Admin/programmer interfaces for hardware/network (e.g., pipes for inter-process comms, sockets for networking).  
- Links: Pointers to files/dirs; hard links share inode, soft/symbolic hold paths.

**Partitions and root**  
Data partition: Houses root (/) essential for boot; mounts other filesystems.  
Swap partition: Extends RAM as virtual memory.  
Root (/): Entry point; forward slash denotes absolute paths in commands.

**Directories per FHS**  
Standard top-level: / (boot essentials); /boot (kernel/bootloader); /bin (user executables); /dev (device files); /etc (local configs); /home (user dirs); /lib (shared libs); /media (removable mounts); /mnt (temp mounts); /opt (vendor apps); /sbin (admin executables); /tmp (temporary files, auto-cleared).

**Paths and navigation**  
Absolute: Starts from / (e.g., /var/spool/mail—command example: cd /var/spool/mail changes to that dir).  
Relative: From current (e.g., logs/mail if in /var/spool; command: cd logs/mail).  
Command artifacts: pwd prints working directory (e.g., pwd outputs /home/user); ls lists contents (ls shows files/dirs); cd changes dir (cd .. moves up).

**Naming guidelines**  
Letters/numbers allowed; specials: . , _ - space comma. Forbidden: ? * / (reserved for shell). Max: 256 chars. Extensions: Optional via dot (e.g., file.txt). Hidden: Starts with . (ls -a reveals). Spaces: Quote in commands (e.g., mv "file with space.txt" newdir).

**Permissions and ownership**  
Levels: Read (r—view/copy); write (w—modify); execute (x—run/view dir).  
Groups: Owners (creator); group (members); others/all (everyone else—restrict for security).  
View: ls -l (e.g., ls -l file.txt outputs drwxr-xr-- 1 user group 4096 Jan 20 16:32 file.txt; d=dir, rwx=user, r-x=group, r--=others).  
Command artifacts: chmod changes perms (chmod +rwx file adds all for user); chown changes owner/group (chown user:group file).

**Security implications**  
Enforce via ownership to prevent unauthorized access; multi-user design requires careful group assignments. Use absolute paths in scripts/commands for precision; relative risks context errors in ops.

SECTION 3: THE KERNEL COMPONENT  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
The kernel forms the core of Linux, managing hardware resources like memory and CPU while serving as the foundation for all distributions. As a monolithic design, it runs all operations in kernel space, enabling efficient server updates but posing security risks if compromised. Defensive admins monitor kernel logs for anomalies and apply patches promptly to mitigate exploits.

**Role and function**  
Brain of the system: Controls CPU, memory, peripherals; bridges hardware and software.

**Design characteristics**  
Monolithic: Single address space for ops; fast but vulnerable to full-system attacks.

**Defensive implications**  
Patch regularly; use modules for safe loading/unloading; audit via tools like dmesg.

SECTION 4: THE SHELL COMPONENT  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Shell provides user interface for OS services, enabling command execution, file ops, and I/O. Types range from basic scripting (Bourne) to advanced interactive (Zsh/Fish). Bash dominates as default; defensive use includes scripting for automation while avoiding untrusted input to prevent injection.

**Core purpose**  
Access point: Runs programs, manipulates files, handles input/output.

**Shell types**  
- Bourne (sh): Small, script-friendly.  
- C (csh): Interactive with history/aliases.  
- TENEX C (tcsh): Autocomplete/job mgmt.  
- Korn (ksh): Bourne+C hybrid with math/OOP.  
- Bash: Default; history/tab/scripting.  
- Dash: Fast/compact.  
- Zsh: Arrays/plug-ins/compatibility.  
- Fish: Autosuggest/syntax/web config.

**Defensive use**  
Prefer Bash for consistency; sanitize inputs in scripts; log sessions for audits. Example: mkdir <dir> creates dir; cd <dir> navigates.

SECTION 5: THE DISTRIBUTION VERSION OF THE LINUX OPERATING SYSTEM  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
A Linux distribution (distro) packages the open-source kernel with tools like graphical desktops, terminals, commands, desktop environments, package managers, installers, and services for ready deployment. Distros preconfigure and compile components for specific architectures or environments, catering to varied users—e.g., Debian for stability in servers/enterprise with 59k+ packages. Ubuntu builds on Debian for general use; Kali specializes in cybersecurity pentesting/auditing. Defensive choice depends on mission: Kali for offensive ops, Debian for hardened servers to minimize attack surface.

**Core elements**  
Kernel base; GUI desktop; CLI terminal/commands; env (e.g., Gnome); package mgmt; installer; services. Independent development; source code distributed.

**Common distros**  
Debian: Stable/reliable; community-maintained; basis for Ubuntu/Kali.  
Kali: Debian-derived; pentesting/auditing focus.

**Defensive selection**  
Assess needs: Stability for prod; tools for testing. Verify integrity on download.

SECTION 6: HOW THE FILE SYSTEM WORKS IN LINUX  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Linux file system hierarchically manages storage from root (/), organizing files by name/size/creation with metadata for non-volatile data. Treats all as files: regular (text/exec), directories (containers), special (pipes/sockets), links (refs). Partitions separate data (root for boot) and swap (virtual mem). FHS defines dirs like /bin (execs), /etc (configs), /home (users). Paths absolute (from /) or relative; permissions control read/write/execute across owners/groups/others. Defensive use: Partition isolation against breaches; strict perms to enforce least privilege; absolute paths in scripts for precision.

**Mechanics**  
Hierarchical: Root + children/partitions. Namespace: Naming/org rules. Metadata: Size/mod/creation dates. Data structures: Free/used space; regions (volumes/partitions).

**File categories**  
Regular: Data/text/exec.  
Directories: Hold files; paths like /var/log.  
Special: System access (pipes/sockets).  
Links: Hard (same inode); soft (path refs).

**Partitions**  
Data: Root (/) for boot/mounts.  
Swap: RAM extension.

**FHS directories**  
/ (essentials); /boot (kernel); /bin (execs); /dev (devices); /etc (configs); /home (users); /lib (libs); /media (removable); /mnt (temp); /opt (apps); /sbin (admin); /tmp (temps).

**Paths**  
Absolute: Starts / (e.g., /var/spool/mail).  
Relative: From current (no leading /).

**Naming rules**  
Letters/numbers; . , _ - space comma ok. No ? * /. Max 256 chars. Extensions optional. Hidden: Starts .. Quote spaces.

**Permissions/ownership**  
Levels: r (view); w (modify); x (execute).  
Groups: Owners; group members; others (restrict).  
View: ls -l (mode: -/d + rwx sets; owner/group).

**Defensive implications**  
Isolate via partitions; enforce perms to block unauthorized access; use absolute paths to avoid context errors.
SECTION 7: COMMAND STRUCTURE  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Linux commands follow intuitive, case-sensitive lowercase patterns with options (dash-prefixed) and arguments (targets) for modification. Use man <command> for manuals; w -h shows logged users without headers. Arguments filter results (e.g., w root for specific user). Defensive ops leverage this for precise scripting and auditing, minimizing errors in automation.

**Basic pattern**  
Command + options + arguments; separate multiples with space/tab.

**Key examples**  
man echo (manual); w -h (users no header); w root (filter user).

SECTION 8: FILE NAMING RULES  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Flexible naming: letters/numbers; allow . , _ - space comma. Max 256 chars; no ? * /. Extensions optional via dot. Hidden files start with .; quote spaces in commands. Defensive: Use consistent, non-revealing names to obscure sensitive files; avoid specials to prevent shell conflicts.

**Conventions**  
Any char/number; specials limited; reserved for shell ops.

**Examples**  
Valid: file_with_space.txt (quote: mv "file_with_space.txt" new); hidden: .config.

SECTION 9: THE USE OF THE TOUCH, REDIRECT, AND APPEND COMMANDS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
touch updates timestamps or creates files; > redirects output (overwrites); >> appends. Useful for backups, logging, or null discards (&>/dev/null). Defensive: Redirect logs for auditing; touch for timestamp manipulation in testing without content changes.

**touch**  
Syntax: touch <file>; example: touch example.txt (create/update).

**Redirect/append**  
> : cat file1.txt file2.txt > output.txt (concat/overwrite); >>: cat file3.txt >> output.txt (add end).


SECTION 10: I CAN IDENTIFY THE COMMAND-LINE TEXT EDITORS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Linux offers CLI text editors for scripting, config edits, and notes: Nano suits beginners with simple UI and shortcuts; Vi provides basic visual mode for Unix-standard ops; Vim enhances Vi with advanced features like plugins and multi-mode editing. Defensive admins master at least one for secure, low-overhead file manipulation in isolated envs—prefer Nano for quick tasks to minimize learning curve risks. Select based on distro defaults and mission needs.

**Nano**  
Beginner-friendly; emulates Pico; non-modal. Features: syntax highlighting, word complete, i18n, locking. Shortcuts: Ctrl+G (help), Ctrl+O (save), Ctrl+X (exit). Install: sudo apt-get install nano (Debian/Ubuntu). Use: nano <file>. Version: nano --version.

**Vi**  
Standard Unix visual editor; command/insert modes. Basic text/file cmds using alphabet keys; no arrow reliance. Use: vi <file>.

**Vim**  
Vi improved; normal/insert/visual modes; steep curve but powerful. Features: multi-undo, plugins, lang support, search/replace. Use: vim <file>. Resources: vim.org (docs), OpenVim (learning), Vim Adventures (game).

SECTION 11: THE USE OF THE CAT, MORE, AND LESS COMMANDS  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
cat displays full file contents directly to terminal, ideal for small files or concatenation. more paginates output one screen at a time for large files, with space/enter navigation and q exit. less enhances more with forward/back scrolling, faster load for big files, and pipe compatibility. Defensive ops use these for quick log reviews without editors; cat for scripting output, more/less for controlled viewing to avoid overload.

**cat**  
Concatenates/views files. Syntax: cat <file>. Example: cat example.txt (outputs 'Hello, World!').

**more**  
Paged display; fits screen. Syntax: more <file>. Nav: Space (page), Enter (line), q (exit). Same as cat for small files.

**less**  
Advanced pager; bidirectional. Syntax: less <file>. Nav: Arrows/Page Up/Down; q exit. Faster for large; supports pipes.

**Quick paragraph summary (30-second read)**  
head displays initial file lines (default 10), customizable for previews; tail shows end lines, useful for logs/stream monitoring. Defensive: Use head for quick header checks in configs; tail -f for real-time threat hunting in logs without full reads.

SECTION 12: THE USE OF THE HEAD AND TAIL COMMANDS  
----------------------------------------------

**head**  
Prints first lines. Syntax: head [option] <file>. Example: head file.txt (top 10); head -n 20 file.txt (first 20).

**tail**  
Prints last lines. Syntax: tail <file>. Example: tail -n 20 file.txt (last 20); monitors streams (tail -f log.txt).

**Defensive application**  
head for file integrity scans; tail for live anomaly detection.

**Quick paragraph summary (30-second read)**  
mkdir creates dirs; mv moves/renames; cp copies; rm deletes files (options for force/prompt/recursive); rmdir removes empty dirs. Defensive: Use absolute paths to avoid errors; rm -r with caution to prevent data loss; mv/cp for backups before mods.

SECTION 13: THE USE OF THE MKDIR, MV, CP, RM, AND RMDIR COMMANDS  
----------------------------------------------

**mkdir**  
Creates directories. Syntax: mkdir [option] <dir>. Example: mkdir my_folder.

**mv**  
Moves/renames. Syntax: mv [option] <source> <dest>. Example: mv old.txt new.txt.

**cp**  
Copies. Syntax: cp [option] <source> <dest>. Example: cp file.txt backup/.

**rm**  
Deletes files. Syntax: rm [options] <file>. Options: -f (force), -i (prompt), -r (recursive). Example: rm file.txt.

**rmdir**  
Deletes empty dirs. Syntax: rmdir [options] <dir>. Example: rmdir empty_dir.

**Defensive notes**  
Verify perms before ops; use -i for safety.

**Quick paragraph summary (30-second read)**  
Hard links: Mirror originals, same inode/perms, inherit changes, filesystem-bound; delete all to remove source. Soft/symbolic: Path refs, unique inode, invalid if source deleted, cross-filesystem. Defensive: Hard for redundancy without duplication; soft for flexible refs; check inodes with ls -i.

SECTION 14: I CAN IDENTIFY SOFT AND HARD LINKS  
----------------------------------------------

**Hard links**  
Same inode as original; mirrors content/perms; updates sync; same filesystem only. Command: ln <source> <target>.

**Soft/symbolic links**  
Holds path; unique inode; no content sync; breaks if source gone; dirs/cross-filesystem ok. Command: ln -s <source> <target>.

**View inodes**  
ls -i <file> (displays numbers).

**Defensive use**  
Hard for secure backups; soft for aliases; monitor broken links.

**Quick paragraph summary (30-second read)**  
Soft and hard links in Linux enable efficient file referencing without duplication, crucial for backups and organization while minimizing storage. Hard links share the same inode as the original, syncing changes and permissions but limited to the same filesystem; they're resilient until all links are deleted. Soft (symbolic) links store paths, allowing cross-filesystem refs but break if the source moves or deletes. Defensive admins use hard links for redundant data protection in isolated partitions and soft for flexible aliases in scripts; always verify inodes to detect tampering or broken refs during audits.

**Core distinctions**  
- **Inode sharing**: Hard uses original inode; soft has unique inode.  
- **Content sync**: Hard mirrors all changes; soft only redirects.  
- **Scope**: Hard filesystem-bound, no dirs; soft cross-filesystem/dirs ok.  
- **Deletion impact**: Hard survives until all links gone; soft dangles if source deleted.  
- **Permissions**: Hard inherits original; soft independent, not auto-updated.

**Creation commands**  
- Hard: ln <source> <target> (e.g., ln file.txt hardlink.txt).  
- Soft: ln -s <source> <target> (e.g., ln -s /dir/file.txt symlink.txt).

**Viewing and verification**  
- Inodes: ls -i <file> (compare numbers for hard links).  
- Type: ls -l (hard shows ref count >1; soft shows lrwxrwxrwx -> target).

**Defensive applications**  
- Hard: Redundancy without extra space; use in backups to preserve data integrity.  
- Soft: Script aliases or temp refs; monitor for dangling (find -xtype l) to avoid exploits.  
- Risks: Hard multiplies delete complexity; soft vulnerable to path changes—absolute paths preferred.

**Table: Characteristic comparison**

| Characteristic | Hard Link | Soft Link |
|---------------|-----------|-----------|
| Scope | Same filesystem; no dirs | Cross-filesystem/dirs |
| Inode | Same as original | Unique |
| Permissions | Inherits/updates with original | Independent/no auto-update |
| Content | Mirrors all | Path only |
| On delete | Persists if links remain | Invalid/dangling |

SECTION 15: THE COMMANDS FOR SEARCHING, WHICH ARE FIND, WHICH, LOCATE AND UPDATEDB  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Linux search commands enable precise file/directory location for ops and auditing: find traverses hierarchies by criteria like name/date/owner; which locates executables via $PATH; locate uses fast database for name-based searches; updatedb refreshes locate's database. Defensive use scans for anomalies or misplaced sensitive files; run updatedb pre-locate for accuracy, but note 24-hour auto-update lag—manual refresh critical post-changes. Combine with pipes for filtered results in scripts.

**find**  
Searches file tree by attributes (name/date/owner/perms). Syntax: find [path] [expression]. Example: find /home/user/Documents -name '*.txt' (all .txt in dir/subdirs).

**which**  
Finds command path in $PATH. Syntax: which [options] <command>. Example: which ls (/bin/ls).

**locate**  
Name-based search via database; faster than find but name-only. Syntax: locate [options] <pattern>. Example: locate myfile.txt (paths matching).

**updatedb**  
Updates locate database; run manually for fresh data (auto daily). Syntax: updatedb [options]. Example: sudo updatedb -n (update excluding nets).

**Defensive notes**  
Find for detailed criteria in audits; which verifies tool integrity; locate/updatedb for speed—schedule cron for regular db refresh.

SECTION 16: I CAN IDENTIFY THE FILE PERMISSIONS AND OWNERSHIP LEVELS OF AUTHORISATION  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
Linux enforces multi-user security through ownership and permissions, assigning files to owners/groups/others with read(r)/write(w)/execute(x) levels to control access. View via ls -l showing mode (type + rwx sets), owner, group. Defensive setup restricts others to prevent breaches; owners get full rwx by default, groups share selectively. Use chmod/chown to adjust; absolute paths ensure precise control in scripts.

**Ownership groups**  
- Owners: File creator; full control default.  
- Groups: Members only; collaborative access.  
- Others/all: Everyone else; restrict for high-risk to avoid exploits.

**Permission levels**  
- Read (r): View/copy contents.  
- Write (w): Modify/add/delete.  
- Execute (x): Run files/view dirs.

**Viewing**  
ls -l <file>: Mode e.g., -rwxr-xr-- (regular file, user rwx, group rx, others r--); owner/group columns.

**Defensive application**  
Enforce least privilege; audit changes; chmod +rwx <file> adds; chown user:group <file> reassigns.

SECTION 17: THE USE OF THE CHOWN COMMAND  
----------------------------------------------

**Quick paragraph summary (30-second read)**  
chown transfers file/directory ownership to a new user or group, enabling precise access control in multi-user environments. Root or sudo required to avoid system disruption; supports recursive changes for bulk ops. Defensive admins use it post-creation to lock down sensitive files, enforcing least privilege and isolating threats—always verify before applying to critical paths.

**Core syntax**  
chown [options] [owner][:group] <file/dir>

**Key examples**  
- chown newowner file.txt (user only).  
- chown newowner:newgroup file.txt (user+group).  
- chown -R newowner dir/ (recursive all contents).

**Group-only variant**  
chgrp newgroup file.txt (changes group without user).

**Defensive controls**  
Run as root/sudo only; audit logs post-change; combine with chmod for full isolation. Caution: Wrong ownership breaks system services.

SECTION 18: THE USE OF THE REGEX TOOL (grep)  
---------------------------------------------

**Quick paragraph summary (30-second read)**  
Regular expressions (RegEx) let you search text by pattern instead of exact strings, and `grep` is the primary CLI tool that applies those patterns to files or streams. Used well, it becomes your main filter for logs, configs, and output from other commands. Security work leans heavily on RegEx for spotting IOCs, anomalies, and misconfigurations across huge text datasets.

**Core syntax**  
grep [options] 'pattern' <file>  

**Key examples**  
- grep "error" app.log (simple literal match).  
- grep -i "failed login" auth.log (case-insensitive).  
- grep -E "user[0-9]{3}" users.txt (extended RegEx, user000–user999).  
- grep -v "127.0.0.1" access.log (invert match, exclude local).  
- dmesg | grep -i "usb" (pipe kernel messages into grep).

**Pattern basics**  
- . matches any single character (e.g., `a.c` → abc, acc).  
- * repeats previous token 0+ times (`fo*` → f, fo, foo).  
- ^ and $ anchor start/end of line (`^root` or `bash$`).  
- [] character classes (`[0-9]`, `[A-Za-z_]`).  
- [^...] negated class (`[^0-9]` non-digits).  
- \ escapes metacharacters (`\.` to match a literal dot).

**Defensive controls**  
Quote patterns to avoid shell expansion; prefer `grep -F` when you do not need RegEx to prevent unintended matches; cap input size or combine with `head`/`tail` to avoid performance hits on massive logs. Caution: overly broad or unanchored patterns can miss true positives or generate noisy false positives in security triage.

***

SECTION 19: THE USE OF THE PATH VARIABLE  
----------------------------------------

**Quick paragraph summary (30-second read)**  
PATH is an environment variable listing directories the shell searches—left to right—when you type a command. It’s why you can run `ls` without typing `/bin/ls`. Tuning PATH lets you prioritise your toolchains, custom scripts, and security binaries, but misconfigurations can break core commands or open the door to binary hijacking.

**Core syntax**  
export PATH=<dir1>:<dir2>:...:<dirN>  

**Key examples**  
- echo $PATH (inspect current search path).  
- export PATH=$PATH:/opt/tools (append tools for current shell).  
- export PATH=/opt/redteam/bin:$PATH (prepend to take priority).  
- echo $0 (discover active shell to know which rc file to edit).  

**Making changes persistent**  
- bash: add `export PATH=...` to `~/.bashrc`.  
- zsh: add to `~/.zshrc`.  

**Defensive controls**  
Never add `.` (current directory) to PATH; avoid writable-by-others directories early in PATH; restrict PATH in service accounts and cron to minimal, known-safe directories. Caution: if a malicious binary named `ls` or `sudo` appears earlier in PATH, it can transparently hijack user actions.

***

SECTION 20: THE USE OF DF AND DU COMMANDS  
-----------------------------------------

**Quick paragraph summary (30-second read)**  
`df` reports free/used space per filesystem, while `du` shows how much space specific directories and files actually consume. Together they answer “is the disk full?” and “what’s filling it?”. Ops and security teams use them constantly to prevent outages, track log growth, and spot suspicious storage spikes from attacks or runaway processes.

**Core syntax**  
- df [options] [path]  
- du [options] <path>  

**Key examples (df)**  
- df -h (all filesystems, human-readable).  
- df -h /var (check specific mount only).  
- df -i (inode usage, critical on mail/log servers).  

**Key examples (du)**  
- du -h /var/log (recursive sizes).  
- du -sh /var/log (single summary size).  
- du -h --max-depth=1 /home | sort -rh | head (top space hogs).  

**Defensive controls**  
Alert when critical mounts exceed thresholds (e.g., 80–90%); use `du` to find and rotate/delete huge logs or dumps; monitor inode usage to avoid “disk full” despite free blocks. Caution: a full `/` or `/var` can crash services, break package management, and hide attacker activity if logs can no longer be written.

***

SECTION 21: THE USE OF PS AND KILL COMMANDS  
-------------------------------------------

**Quick paragraph summary (30-second read)**  
`ps` snapshots running processes—who owns them, what they’re doing, and how much CPU/RAM they consume. `kill` sends signals to those processes, usually to stop or restart them. Together they’re your basic process triage tools for spotting rogue binaries, hung services, or resource hogs before they impact availability or security.

**Core syntax**  
- ps [options]  
- kill [signal] <PID>  

**Key examples (ps)**  
- ps aux (all processes, user-oriented view).  
- ps aux | grep sshd (locate specific process).  
- ps auxf (tree view; parent/child relationships).  

**Key examples (kill)**  
- kill 1234 (default SIGTERM – graceful stop).  
- kill -9 1234 (SIGKILL – force, no cleanup).  
- killall nginx (signal all processes named nginx).  

**Useful signals**  
- SIGTERM (15): ask process to exit cleanly.  
- SIGKILL (9): immediate hard kill.  
- SIGHUP (1): often used to reload configs.  

**Defensive controls**  
Restrict process control to admins via sudo and RBAC; log all kill operations; prefer SIGTERM before SIGKILL to allow proper shutdown and logging. Caution: killing the wrong root-owned process (e.g., PID 1 equivalents or DB engines) can crash the system or corrupt data.

***

SECTION 22: THE USE OF SORT AND WC COMMANDS  
-------------------------------------------

**Quick paragraph summary (30-second read)**  
`sort` orders lines in text (alphabetical, numerical, by field), while `wc` counts lines, words, and bytes. Combined with pipes, they form a powerful mini-analytics stack for log review and data munging, letting you find top talkers, deduplicate entries, and get quick stats without leaving the shell.

**Core syntax**  
- sort [options] [file]  
- wc [options] [file]  

**Key examples (sort)**  
- sort file.txt (basic ascending sort).  
- sort -r file.txt (reverse order).  
- sort -n numbers.txt (numeric sort).  
- sort -u ips.txt (sort + deduplicate).  

**Key examples (wc)**  
- wc file.txt (lines, words, bytes).  
- wc -l access.log (just line count).  
- wc -w report.md (word count).  

**Combining them**  
- sort urls.txt | uniq -c | sort -rn | head (top URLs).  
- grep "ERROR" app.log | wc -l (error count).  

**Defensive controls**  
Use them to detect log flooding or brute-force attempts (huge line counts, repeated IPs); be careful when sorting very large files—consider sampling first. Caution: sorting multi-GB logs can thrash memory and I/O; run heavy operations off-peak or on copies.

***

SECTION 23: THE USE OF THE HISTORY COMMAND  
-------------------------------------------

**Quick paragraph summary (30-second read)**  
`history` exposes the shell’s record of previously run commands, making it trivial to rerun, edit, or audit your actions. Great for productivity and incident review, but also a potential leak of sensitive data if passwords or keys are typed directly into commands instead of using safer input methods.

**Core syntax**  
history [n]  

**Key examples**  
- history (show full list with line numbers).  
- history 20 (last 20 commands).  
- !42 (rerun command #42).  
- !! (rerun last command).  
- sudo !! (rerun last command with sudo).  
- !grep (rerun last command starting with `grep`).  

**Editing and cleaning**  
- history -d 50 (delete entry #50).  
- history -c (clear current session history).  

**Defensive controls**  
Avoid putting secrets on the command line; restrict permissions on `~/.bash_history`; consider `HISTCONTROL=ignorespace` to skip logging commands that start with a space. Caution: history files are valuable artifacts in incident response and equally valuable targets for attackers—monitor and back them up appropriately.

***
