@app.route("/basic-protected", methods=["GET"])
@basic_auth.login_required
def basic_protected():
    """Protected route using HTTP Basic authentication."""
    return "Basic Auth: Access Granted", 200

