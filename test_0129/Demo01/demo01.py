from ldap3 import Server, Connection, ALL

server = Server('ldap://ldap.example.com', get_info=ALL)
conn = Connection(server, user='cn=admin,dc=example,dc=com', password='secret')
conn.bind()

conn.search('dc=example,dc=com', '(objectClass=person)', attributes=['cn', 'sn'])

for entry in conn.entries:
    print(entry.cn, entry.sn)

conn.unbind()
