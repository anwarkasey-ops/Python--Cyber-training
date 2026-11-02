# 04_port_inspector.py
# simple SOC  script to inspect open ports and flag insecure services 
open_ports =  [ 22, 80, 443, 21,3389,23]
print("=== Network port security Audit===")
for port in open_ports:
    if port ==21:
        print (f"port{port}:FTP detected [FLAG]-unencrypted file transfer!")
    elif port==23:
        print (f"port {port}:Telnet detected [FLAG]-high risk! unencryptedshell.")
    elif port ==80:
      print (f"port{port}:HTTP detected [WARNING]-Plaintext web traffic.")
    else:   
        print(f"port {port}: standard service running [OK].")