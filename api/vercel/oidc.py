import os

def get_vercel_oidc_token():
    # Fallback to OPENAI_API_KEY for local development or direct usage
    return os.environ.get("OPENAI_API_KEY")
