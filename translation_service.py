from transformers import MarianMTModel, MarianTokenizer
import torch

class TranslationService:
    def __init__(self):
        self.models = {}
        self.tokenizers = {}
        
        # Pre-load common language pairs
        self.load_model('en', 'fr')
        self.load_model('fr', 'en')
        self.load_model('en', 'es')
        self.load_model('es', 'en')
    
    def load_model(self, src_lang, tgt_lang):
        model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        try:
            self.tokenizers[(src_lang, tgt_lang)] = MarianTokenizer.from_pretrained(model_name)
            self.models[(src_lang, tgt_lang)] = MarianMTModel.from_pretrained(model_name)
        except:
            # If direct model doesn't exist, try through English
            self.tokenizers[(src_lang, tgt_lang)] = None
            self.models[(src_lang, tgt_lang)] = None
    
    def translate(self, text, src_lang, tgt_lang):
        # Check if direct model exists
        if (src_lang, tgt_lang) in self.models and self.models[(src_lang, tgt_lang)]:
            tokenizer = self.tokenizers[(src_lang, tgt_lang)]
            model = self.models[(src_lang, tgt_lang)]
        else:
            # Translate through English as intermediate
            if (src_lang, 'en') in self.models and self.models[(src_lang, 'en')] and \
               ('en', tgt_lang) in self.models and self.models[('en', tgt_lang)]:
                # First translate to English
                intermediate = self.translate(text, src_lang, 'en')
                # Then to target language
                return self.translate(intermediate, 'en', tgt_lang)
            else:
                raise ValueError(f"No translation model available for {src_lang} to {tgt_lang}")
        
        # Tokenize and translate
        batch = tokenizer([text], return_tensors="pt", truncation=True)
        gen = model.generate(**batch)
        translated = tokenizer.batch_decode(gen, skip_special_tokens=True)[0]
        
        return translated