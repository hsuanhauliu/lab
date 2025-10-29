# Raspberry Pi - Pi-hole

Raspberry Pi device dedicated for running [Pi-hole](https://docs.pi-hole.net/main/basic-install/), a network-level advertisement and Internet tracker blocking application.

## Installation

[![pihole-setup-tutorial](https://img.youtube.com/vi/cE21YjuaB6o/0.jpg)](https://www.youtube.com/watch?v=cE21YjuaB6o)

1. Have a Raspberry Pi ready to go. Internet should be connected.
1. Run `curl -sSL https://install.pi-hole.net | bash` and follow the instructions to set it up.
1. You should update periodically by running `sudo pihole -up`.

## Configuration

On the Pi-hole device:

1. Make sure the device is configured to use static IP. Use a IP that's not in the range of DHCP.
    1. Modify DHCP config. `sudo nano /etc/dhcpcd.conf`.
    1. Add or modify the file with lines below. If you use a different interface like wifi, it would be something like wlan0. Run `ip a` to look this up.

        ```bash
        interface eth0
        # here we use 192.168.0.200 as Pi-hole's IP as an example.
        static ip_address=192.168.1.200/24
        static routers=192.168.1.1
        static domain_name_servers=127.0.0.1
        ```

    1. Reboot device `sudo reboot now`.
    1. Verify IP `ip a`.
1. Change password. By default, a random password is used. Change it by running `pihole setpassword`, or go to http://< your-pi-hole-ip >/admin and click on "forgot password?" on login page.

On your internet router:

1. Change DNS settings to point to your Pi-hole device, and remove other DNS servers. This will prevent traffic from being routed to other DNS servers.
1. You might want to configure IPv6 DNS, or you could consider disabling IPv6 altogether.

## Blocklist

The default blocklist after installation is probably not enough. Best practice is to add 3 top links from each categories on <https://firebog.net/> to your blocklist.

1. On the Pi-hole UI, go to "Lists" on the left menu.
1. Copy and paste each link to address then click "add blocklist".
1. Once you're done, go to "Update Gravity" under "Tools" on the left menu. Click "Update".

## Resources

- <https://docs.pi-hole.net/main/post-install/#making-your-network-take-advantage-of-pi-hole>
- <https://www.crosstalksolutions.com/the-worlds-greatest-pi-hole-and-unbound-tutorial-2023/#Testing_Ad_Blocking>
