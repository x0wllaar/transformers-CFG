from transformers import (BartTokenizerFast, CodeGenTokenizerFast,
                          GemmaTokenizerFast, GPT2TokenizerFast,
                          LlamaTokenizerFast, PreTrainedTokenizerFast,
                          T5TokenizerFast)

SUPPORTED_TOKENIZERS = {
    GPT2TokenizerFast,
    BartTokenizerFast,
    LlamaTokenizerFast,
    T5TokenizerFast,
    CodeGenTokenizerFast,
    PreTrainedTokenizerFast,
    GemmaTokenizerFast,
}

# This might not be supported everywhere
try:
    from transformers import Qwen2TokenizerFast

    SUPPORTED_TOKENIZERS.add(Qwen2TokenizerFast)
except ImportError:
    pass
