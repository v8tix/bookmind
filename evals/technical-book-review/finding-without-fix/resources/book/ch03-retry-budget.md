## 3. The retry budget

When a send fails, the client retries automatically. It makes at most **five** attempts in all before it gives up, and across every attempt it keeps the same TCP connection open instead of reconnecting each time.

The retry budget exists so that a flaky network degrades a call instead of hanging it forever.
