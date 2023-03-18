import ldap
#连接到 LDAP 服务器：
# Connect to the LDAP server
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
l = ldap.initialize("ldap://ldap.example.com:389")
l.protocol_version = ldap.VERSION3

# Bind to the LDAP server
username = "cn=admin,dc=example,dc=com"
password = "secret"
l.simple_bind_s(username, password)

# Add a new entry
#增加：
dn = "cn=newuser,ou=people,dc=example,dc=com"
attrs = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
    'cn': 'newuser',
    'sn': 'User',
    'givenName': 'New',
    'mail': 'newuser@example.com',
    'userPassword': 'secret'
}
l.add_s(dn, ldap.modlist.addModlist(attrs))


# Delete an entry
dn = "cn=newuser,ou=people,dc=example,dc=com"
l.delete_s(dn)


# Modify an entry
dn = "cn=user,ou=people,dc=example,dc=com"
mod_attrs = [(ldap.MOD_REPLACE, 'mail', 'newuser@example.com')]
l.modify_s(dn, mod_attrs)


# Search for entries
base_dn = "ou=people,dc=example,dc=com"
search_filter = "(objectClass=person)"
result = l.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
for dn, entry in result:
    print(dn, entry)




