<div align="center">
  <img width="1000" alt="image" src="https://github.com/caido-community/.github/blob/main/content/banner.png?raw=true">

  <br />
  <br />
  <a href="https://github.com/caido-community" target="_blank">Github</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://developer.caido.io/" target="_blank">Documentation</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://links.caido.io/www-discord" target="_blank">Discord</a>
  <br />
  <hr />
</div>

## 👋 Server Auth

[![Pypi Version](https://img.shields.io/pypi/v/caido-server-auth?style=for-the-badge)](https://pypi.org/project/caido-server-auth/)

Authenticate with a Caido instance using device code flow.

```python
import asyncio
import os

from caido_server_auth import (
    AuthClient,
    AuthClientOptions,
    AuthenticationRequest,
    BrowserApprover,
)


def on_request(request: AuthenticationRequest) -> None:
    print(f"Visit: {request.verification_url}")
    print(f"Expires at: {request.expires_at.isoformat()}")


async def main() -> None:
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")
    auth = AuthClient(
        AuthClientOptions(
            instance_url=instance_url,
            approver=BrowserApprover(on_request),
        )
    )
    token = await auth.start_authentication_flow()
    print(token.access_token)


asyncio.run(main())
```

## Examples

See the `examples` directory for complete working examples:

- `examples/browser_auth.py` - Manual approval via browser
- `examples/pat_auth.py` - Automated approval using Personal Access Token

## 💚 Community

Come join our [Discord](https://links.caido.io/www-discord) community and connect with other Caido users! We'd love to have you as part of the conversation and help with any questions you may have.
