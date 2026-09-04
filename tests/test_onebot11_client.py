import io
import unittest
from contextlib import redirect_stdout

from mvp import MessageMapper, OneBot11Client


class TestOneBot11ClientPrintMessage(unittest.TestCase):
    def render(self, msg_type: str, payload: dict) -> str:
        mapped = MessageMapper.map_event(payload)
        client = OneBot11Client()
        stream = io.StringIO()

        with redirect_stdout(stream):
            client._print_message(msg_type, payload, mapped)

        return stream.getvalue()

    def test_prints_message_event_details(self):
        payload = {
            "post_type": "message",
            "time": 1700000000,
            "self_id": 10001,
            "message_type": "private",
            "sub_type": "friend",
            "message_id": 1,
            "user_id": 42,
            "message": "hello",
            "raw_message": "hello",
            "font": 0,
            "sender": {"nickname": "Alice"},
        }

        output = self.render("MESSAGE [private]", payload)

        self.assertIn("MESSAGE [private]", output)
        self.assertIn("Message Type: private", output)
        self.assertIn("User ID: 42", output)
        self.assertIn("Message: hello", output)
        self.assertIn("Timestamp: 1700000000", output)
        self.assertIn("Self ID: 10001", output)

    def test_prints_notice_event_details(self):
        payload = {
            "post_type": "notice",
            "time": 1700000001,
            "self_id": 10001,
            "notice_type": "group_increase",
            "user_id": 43,
        }

        output = self.render("NOTICE [group_increase]", payload)

        self.assertIn("NOTICE [group_increase]", output)
        self.assertIn("Notice Type: group_increase", output)
        self.assertIn("User ID: 43", output)
        self.assertIn("Timestamp: 1700000001", output)
        self.assertIn("Self ID: 10001", output)

    def test_prints_meta_event_details(self):
        payload = {
            "post_type": "meta_event",
            "time": 1700000002,
            "self_id": 10001,
            "meta_event_type": "heartbeat",
            "sub_type": "normal",
        }

        output = self.render("META_EVENT [heartbeat]", payload)

        self.assertIn("META_EVENT [heartbeat]", output)
        self.assertIn("Meta Event Type: heartbeat", output)
        self.assertIn("Sub Type: normal", output)
        self.assertIn("Timestamp: 1700000002", output)
        self.assertIn("Self ID: 10001", output)


if __name__ == "__main__":
    unittest.main()
