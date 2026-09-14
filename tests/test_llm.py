from types import SimpleNamespace

import pytest

import llm


def test_create_llm_requires_api_key(monkeypatch):
	monkeypatch.delenv("GROQ_API_KEY", raising=False)

	with pytest.raises(
		ValueError,
		match=r"GROQ_API_KEY not found in \.env file",
	):
		llm.create_llm()


def test_create_llm_configures_chatgroq(monkeypatch):
	monkeypatch.setenv("GROQ_API_KEY", "test-api-key")
	mock_chatgroq = lambda **kwargs: kwargs
	monkeypatch.setattr(llm, "ChatGroq", mock_chatgroq)

	result = llm.create_llm()

	assert result == {
		"model": "qwen/qwen3.8-27b",
		"api_key": "test-api-key",
		"temperature": 0,
	}


def test_analyze_data_returns_llm_response_content():
	response = SimpleNamespace(content="The answer is 42.")

	class FakeLLM:
		def __init__(self):
			self.prompt = None

		def invoke(self, prompt):
			self.prompt = prompt
			return response

	fake_llm = FakeLLM()
	result = llm.analyze_data(
		fake_llm,
		"What is the average age?",
		{"statistics": {"age": {"mean": 42}}},
	)

	assert result == "The answer is 42."
	assert "What is the average age?" in fake_llm.prompt
	assert "'mean': 42" in fake_llm.prompt
	assert "Do not invent numbers." in fake_llm.prompt
