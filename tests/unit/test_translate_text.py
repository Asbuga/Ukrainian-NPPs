from notebook.utils.translate_text import get_translation


def test_translate_text():
    # Test the translation of a valid text
    text = "Привіт, як справи?"
    translated_text = get_translation(text)
    assert translated_text == "Hello, how are you?"  

    # Test the translation of an empty string
    text = ""
    translated_text = get_translation(text)
    assert translated_text == ""

    # Test the translation of None
    text = None
    translated_text = get_translation(text)
    assert translated_text == ""
