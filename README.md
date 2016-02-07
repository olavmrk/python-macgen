mac_gen
=======

A trivial Python script that generates a random MAC address.

About
-----

This script generates a random MAC address.
The generated MAC address will have the "locally administered" bit set and the multicast bit cleared.

Usage
-----

Simply invoke the script with no arguments:

```
$ mac_gen.py
c6:70:06:fc:5a:61
```

The generated MAC address will be written to standard output.

The script also takes an optional parameter `--separator`, which allows you to select what character to use to separate the bytes of the MAC address:

`colon`:

```
$ ./mac_gen.py --separator=colon
ba:d2:6a:dc:43:52
```

`dash`:

```
$ ./mac_gen.py --separator=dash
be-d0-8e-cf-15-e9
````

`none`:

```
$ ./mac_gen.py --separator=none
96f2b323b2f1
```

`space`:

```
$ ./mac_gen.py --separator=space
76 68 ff 31 0c 86
```
