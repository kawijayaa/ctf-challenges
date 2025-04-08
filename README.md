# ctf-challenges

A collection of CTF challenges I have made over the years.

## Directory Structure

```
category/
└── challenge-name/
    ├── public/       # Files that participants would receive
    ├── src/          # Files that are deployed to the server / source code to generate the challenge
    ├── writeup/      # A short writeup/payload and scripts to solve the challenge, if any
    └── README.md     # Contains the challenge description, flag and any other information
```

## Challenge Deployment

If the challenge needs a service, the challenge can be deployed locally using Docker and Docker Compose using the following commands:

```bash
docker-compose up -d
```

## Challenges

### Forensics

<table>
    <tr>
        <th>Challenge Name</th>
        <th>Topics</th>
    </tr>
    <tr>
        <td><a href="forensics/bleu-de-fender/">bleu-de-fender</a></td>
        <td>Disk Forensics, Windows Defender, PNG Steganography</td>
    </tr>
    <tr>
        <td><a href="forensics/collection/">collection</a></td>
        <td>Network Forensics, Clipboard Stealer, Powershell</td>
    </tr>
    <tr>
        <td><a href="forensics/frost/">frost</a></td>
        <td>Active Directory Forensics, Docker Image Analysis, C2, SMB</td>
    </tr>
    <tr>
        <td><a href="forensics/industrialspy/">industrialspy</a></td>
        <td>Memory Forensics, Volatility3, GIMP</td>
    </tr>
    <tr>
        <td><a href="forensics/industrialspy2/">industrialspy2</a></td>
        <td>Wireshark, USB Forensics</td>
    </tr>
    <tr>
        <td><a href="forensics/industrialspy3/">industrialspy3</a></td>
        <td>Network Forensics, Wireshark, Threat Intelligence</td>
    </tr>
    <tr>
        <td><a href="forensics/keepnotes/">keepnotes</a></td>
        <td>Disk Forensics, Notepad Cache</td>
    </tr>
    <tr>
        <td><a href="forensics/loss/">loss</a></td>
        <td>Git Forensics, Git Recovery</td>
    </tr>
    <tr>
        <td><a href="forensics/persistence/">persistence</a></td>
        <td>Disk Forensics, File Association, Keylogger</td>
    </tr>
    <tr>
        <td><a href="forensics/power/">power</a></td>
        <td>Network Forensics, Threat Intelligence, PowerShell</td>
    </tr>
    <tr>
        <td><a href="forensics/protokol/">protokol</a></td>
        <td>Network Forensics</td>
    </tr>
</table>

### Web Exploitation

<table>
    <tr>
        <th>Challenge Name</th>
        <th>Topics</th>
    </tr>
    <tr>
        <td><a href="web/belajar-coding/">belajar-coding</a></td>
        <td>PHP, LFI</td>
    </tr>
    <tr>
        <td><a href="web/copasbin/">copasbin</a></td>
        <td>XSS, Prototype Pollution, CVE</td>
    </tr>
    <tr>
        <td><a href="web/greet-your-friend/">greet-your-friend</a></td>
        <td>SSTI, Jinja2</td>
    </tr>
    <tr>
        <td><a href="web/joewatson/">joewatson</a></td>
        <td>JWT, Nginx Misconfiguration, LFI</td>
    </tr>
    <tr>
        <td><a href="web/pink/">pink</a></td>
        <td>Command Injection</td>
    </tr>
    <tr>
        <td><a href="web/siakgg/">siakgg</a></td>
        <td>SQL Injection</td>
    </tr>
    <tr>
        <td><a href="web/thematrix/">thematrix</a></td>
        <td>Cypher Injection, Neo4j</td>
    </tr>
    <tr>
        <td><a href="web/weebsocks/">weebsocks</a></td>
        <td>Websockets, Broken Access Control</td>
    </tr>
</table>
