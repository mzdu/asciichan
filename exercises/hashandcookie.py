        
# #setup cookies
# 
# visits = self.request.cookies.get('visits', '0')
# visits = int(visits) + 1
# self.response.headers.add_header('Set-cookie', 'visits=%s' % visits)
# self.write("you have been here %s times." % visits)

# 
# # CRC32 - checksums, fast to prevent cookies from modification
# # MD5 - fast, secure kind of, for limited input
# # SHA1 - secure
# # SHA256 - pretty good, but slower
'''
import hashlib
hashlib.md5("hello").hexdigit()
==> '23u2839280380023...'
'''
        