from googletrans import Translator

translator = Translator()


async def get_translation(text: str) -> str:
    """Translate text from Ukrainian to English using Google Translate API."""
    try:
        # Check if the text is empty or None
        if not text:
            return ""

        # Translate the text from Ukrainian to English
        translation = await translator.translate(text, src="uk", dest="en")
        return translation.text

    except Exception as e:
        # Handle any exceptions that occur during translation
        print(f"Error during translation: {e}")
        return text
