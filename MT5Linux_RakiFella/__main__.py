"""Command-line entrypoint for the MT5Linux_RakiFella RPyC classic server."""

from __future__ import annotations

from rpyc.cli.rpyc_classic import ClassicServer

# Hosts that are always allowed, regardless of what's passed via --host
ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1"}


class SafeClassicServer(ClassicServer):
    """
    Same as RPyC's ClassicServer, but refuses to bind to anything other than
    localhost, even if --host is explicitly passed with a different value.
    This is a deliberate safety net against accidental network exposure.
    """

    def main(self):
        if self.host and self.host not in ALLOWED_HOSTS:
            print(
                f"[MT5Linux_RakiFella SAFETY] Ignoring '--host {self.host}'. "
                f"This server only binds to localhost by design. "
                f"Forcing host to 127.0.0.1."
            )
            self.host = "127.0.0.1"
        super().main()


if __name__ == "__main__":
    SafeClassicServer.run()