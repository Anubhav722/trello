

class AuthenticationService:

    def __init__(self, ttl):
        self.tokens = {}  # Map<token_id, user_obj>

    def renew_token(self, token_id):
        pass

    def authenticate_request(self, token_id, timestamp):
        pass

    def register_user(self, ):
        pass
