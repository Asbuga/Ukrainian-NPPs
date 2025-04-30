import pytest

from common.translate_text import get_translation


@pytest.mark.asyncio
async def test_translate_text():
    # Test the translation of a valid text
    text = "Привіт, як справи?"
    translated_text = await get_translation(text)
    assert translated_text == "Hi, how are you?"  

    # Test the translation of an empty string
    text = ""
    translated_text = await get_translation(text)
    assert translated_text == ""

    # Test the translation of None
    text = None
    translated_text = await get_translation(text)
    assert translated_text == ""
