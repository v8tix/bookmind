## 2. Safety limits

Before the writer accepts a batch, it checks **four** safety limits: the batch is not empty, every record fits the schema, the batch is under the byte cap, and the batch's sequence number is in order.

A batch that fails any one of the four is rejected whole; nothing in it is partially written.
