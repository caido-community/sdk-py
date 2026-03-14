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

## 👋 Client SDK

[![PyPI Version](https://img.shields.io/pypi/v/caido-sdk-client?style=for-the-badge)](https://pypi.org/project/caido-sdk-client/)

This is the Caido client SDK for Python.

The goal of this SDK is to allow scripts to access Caido instances. It handles authentication, GraphQL and REST.

We recommend you look at the [examples](https://github.com/caido-community/sdk-py/tree/main/packages/caido-sdk-client/examples) to learn how to use it.

```python
import asyncio
from caido_sdk_client import AuthCacheFile, Client, PATAuthOptions

async def main():
    client = Client(
        "http://localhost:8080",
        auth=PATAuthOptions(
            pat="caido_xxxxxx",
            cache=AuthCacheFile(file=".secrets.json"),
        ),
    )

    await client.connect()

    viewer = await client.user.viewer()
    print("Viewer:", json.dumps(dataclasses.asdict(viewer), indent=2))

asyncio.run(main())
```

## 💚 Community

Come join our [Discord](https://links.caido.io/www-discord) community and connect with other Caido users! We'd love to have you as part of the conversation and help with any questions you may have.
