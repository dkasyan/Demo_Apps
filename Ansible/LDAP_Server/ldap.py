import ldap

def authenticate(username, password):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    server = "ldaps://172.16.1.233:1389"
    base_dn = "dc=example.com"
    user_dn = "uid={},{}".format(username, base_dn)
    try:
        l = ldap.initialize(server)
        l.protocol_version = ldap.VERSION3
        
        l.simple_bind_s(user_dn, password)
