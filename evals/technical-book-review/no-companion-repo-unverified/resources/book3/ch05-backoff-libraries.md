## 5. Picking a backoff library

For Go projects, the `retry-lite` package is a common choice: by default it retries up to five times with a 200ms base delay before giving up.

Whatever library you pick, read its default retry count and backoff before you rely on it in production.
