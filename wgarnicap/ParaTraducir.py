from googletrans import Translator

translator = Translator()
print(translator.translate('안녕하세요.'))
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
print(translator.translate('안녕하세요.', dest='es'))
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
print(translator.translate('veritas lux mea', dest='es'))
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>


translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='es')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)

