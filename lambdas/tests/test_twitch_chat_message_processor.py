import unittest

from lambdas.twitch_chat_message_processor import lambda_handler

example_sqs_message = {
    "Records": [{"body": "some twitch message", "receiptHandle": "some-guid"}]
}


def test_lambda_works(mocker):
    mocker.patch("lambdas.twitch_chat_message_processor.send_message")
    response = lambda_handler(example_sqs_message, {})

    assert response["statusCode"] == 200
    assert (
        response["body"]
        == "\"Successfully posted record to command queue 'some twitch message'\""
    )


if __name__ == "__main__":
    unittest.main()
