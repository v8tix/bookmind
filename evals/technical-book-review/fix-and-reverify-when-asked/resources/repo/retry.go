package queue

// MaxRetries is the most attempts Send makes before it gives up.
const MaxRetries = 3

// Send keeps one connection open across every attempt instead of
// reconnecting each time.
func (c *Client) Send(msg []byte) error {
	conn := c.dial()
	defer conn.Close()
	for attempt := 0; attempt < MaxRetries; attempt++ {
		if err := conn.write(msg); err == nil {
			return nil
		}
	}
	return errSendFailed
}
