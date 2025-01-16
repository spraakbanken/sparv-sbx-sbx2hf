from sparv.api import Config

from . import exporters

__config__ = [
    Config("sbx_sbx2hf.config", None, "Configuration variables for sbx2hf"),
]

__description__ = "A Sparv plugin for uploading export files to HuggingFace."