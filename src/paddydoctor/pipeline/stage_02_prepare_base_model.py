from paddydoctor.config.configuration import ConfigurationManager
from paddydoctor.components.prepare_base_model import PrepareBaseModel


class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()