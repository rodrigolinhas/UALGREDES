import socket
import struct

def build_dns_query(domain):
    # Header: ID (2 bytes) + Flags (2 bytes) + QDCOUNT (2 bytes) + ANCOUNT (2 bytes) + NSCOUNT (2 bytes) + ARCOUNT (2 bytes)
    header = struct.pack("!HHHHHH", 0x1234, 0x0100, 1, 0, 0, 0)
    
    # Question: QNAME + QTYPE (2 bytes) + QCLASS (2 bytes)
    qname = b"".join(bytes([len(part)]) + part.encode() for part in domain.split(".")) + b"\x00"
    qtype = struct.pack("!H", 1)  # Type A (IPv4 Address)
    qclass = struct.pack("!H", 1)  # Class IN (Internet)
    
    return header + qname + qtype + qclass

def send_dns_query(domain, server="8.8.8.8", port=53):
    query = build_dns_query(domain)
    
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    
    try:
        sock.sendto(query, (server, port))
        response, _ = sock.recvfrom(512)  # Max UDP DNS response size is 512 bytes
        print("DNS Response Received:", response)
    except socket.timeout:
        print("Request timed out.")
    finally:
        sock.close()

if __name__ == "__main__":
    domain = input("Enter domain name: ")
    send_dns_query(domain)