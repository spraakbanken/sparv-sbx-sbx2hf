from sparv.api import (
    Config,
    AnnotationAllSourceFiles,
    AllSourceFilenames,
    Export,
    exporter
)

from sbx2hf import sbx2hf

@exporter("Upload corpus to Hugging Face using the sbx2hf tool", language="swe")
def upload_to_huggingface(
    source_files: AllSourceFilenames = AllSourceFilenames(),
    sentence: AnnotationAllSourceFiles = AnnotationAllSourceFiles("<sentence>"),
    sbx2hf_config = Config("sbx_sbx2hf.config"),
    out: Export = Export("sbx_sbx2hf.hf_repository/"),
    id = Config("id")
):
   default_sbx2hf_args = {}
   if sbx2hf is not None:
      merged_config = sbx2hf_config | default_sbx2hf_args
   sbx2hf(**merged_config)