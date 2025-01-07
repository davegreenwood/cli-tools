"""
python wol.py 00:11:22:33:44:55
python wol.py --help
"""

import socket
import typer

app = typer.Typer()


def wake_on_lan(mac_address: str, broadcast_addr: str = '255.255.255.255', port: int = 9) -> None:
    mac = mac_address.replace(':', '').replace('-', '')
    if len(mac) != 12:
        raise ValueError('Invalid MAC address format')
    
    magic = b'FF' * 6 + (bytes.fromhex(mac) * 16)
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic, (broadcast_addr, port))
        print(f"Packet sent to: {mac_address}")


@app.command()
def wake(
    mac: str = typer.Argument(..., help="MAC address of target machine (XX:XX:XX:XX:XX:XX)"),
    broadcast: str = typer.Option('255.255.255.255', help="Broadcast address"),
    port: int = typer.Option(9, help="Port number")
) -> None:
    """Send Wake-on-LAN magic packet to wake up a networked device."""
    wake_on_lan(mac, broadcast, port)


if __name__ == "__main__":
    app()