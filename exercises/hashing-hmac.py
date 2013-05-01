import hmac

SECRET = "iamsosecret"

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


print hash_str("hello")