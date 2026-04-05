#!/usr/bin/env python3
"""
Servidor HTTP com ficheiros estaticos e proxy CORS para networking v86.

Uso:
    python server.py [porta]

Exemplo:
    python server.py 8080
    Abrir http://localhost:8080 no browser
"""
import http.server
import urllib.request
import urllib.parse
import sys


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if parsed.path == "/proxy" and "url" in params:
            self._proxy(params["url"][0])
        else:
            super().do_GET()

    def _proxy(self, url):
        try:
            p = urllib.parse.urlparse(url)
            if p.scheme not in ("http", "https"):
                self.send_error(400, "Apenas http/https permitido")
                return
            if not p.hostname:
                self.send_error(400, "URL invalido")
                return
            req = urllib.request.Request(url, headers={"User-Agent": "v86-proxy/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                self.send_response(resp.status)
                ct = resp.headers.get("Content-Type", "application/octet-stream")
                cl = resp.headers.get("Content-Length")
                self.send_header("Content-Type", ct)
                if cl:
                    self.send_header("Content-Length", cl)
                self.end_headers()
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
        except Exception as e:
            try:
                self.send_error(502, str(e))
            except Exception:
                pass


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print(f"Servidor HTTP:  http://localhost:{port}")
    print(f"Proxy CORS:     http://localhost:{port}/proxy?url=<url>")
    print(f"Ctrl+C para parar")
    http.server.HTTPServer(("", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
