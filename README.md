docker-port-introspect
======================

Docker API (socket) wrapper to get ports inside of a container. Plus serf -tags to expose mapped 49XXX ports.

It is intended to be used with Serf (not needed for Consul).

A common use case is to make your dockerized services ports available for a Serf cluster. This script will format -tags
field so you'll be able to fetch port information from other cluster members.

I hope when libswarm becomes stable enough and some issues preventing Consul from working correctly (like flapping state
due to tcp/udp binding in the wrong way, as well as problem with advertising the Consul client ports).