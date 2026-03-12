"""Example: Basic authentication flow with Caido."""

import asyncio
from caido_auth import CaidoAuth, AuthenticationRequest, AuthenticationToken


def on_auth_request(request: AuthenticationRequest):
    """Callback when user needs to authorize."""
    print("\n" + "=" * 60)
    print("🔐 Caido Authentication Required")
    print("=" * 60)
    print(f"\n📋 User Code: {request.user_code}")
    print(f"🔗 Verification URL: {request.verification_url}")
    print(f"⏰ Expires at: {request.expires_at}")
    print("\nPlease visit the URL above and enter the code to authorize.")
    print("Waiting for authorization...\n")


async def main():
    """Run the authentication flow."""
    # Initialize the auth client with your Caido instance URL
    auth = CaidoAuth("http://localhost:8080")

    try:
        # Start the authentication flow
        print("Starting authentication flow...")
        token = await auth.start_authentication_flow(on_request=on_auth_request)

        print("\n✅ Authentication successful!")
        print(f"Access Token: {token.access_token[:20]}...")
        print(f"Expires at: {token.expires_at}")
        print(f"Scopes: {[scope.value for scope in token.scopes]}")

        if token.refresh_token:
            print(f"Refresh Token: {token.refresh_token[:20]}...")

            # Demonstrate token refresh
            print("\n🔄 Refreshing token...")
            new_token = await auth.refresh_token(token.refresh_token)
            print("✅ Token refreshed successfully!")
            print(f"New Access Token: {new_token.access_token[:20]}...")
            print(f"New Expires at: {new_token.expires_at}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(asyncio.run(main()))
