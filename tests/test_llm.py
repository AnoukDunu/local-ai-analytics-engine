from ai.llm import get_ollama_client


def test_ollama_client_can_be_created():
    client = get_ollama_client()

    assert client is not None
