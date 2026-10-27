#!/usr/bin/python3
"""Create a simple API using Python's http.server module."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlsplit


class MyHTTPServer(BaseHTTPRequestHandler):
    """Handle GET requests for the simple API."""

    def do_GET(self):
        """Return a response according to the requested endpoint."""
        path = urlsplit(self.path).path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        elif path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        else:
            response = b"Endpoint not found"
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)


def main():
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHTTPServer)

    print("Server running on port 8000...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
